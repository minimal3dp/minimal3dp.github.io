#!/usr/bin/env python3
"""
Post Hugo content to Medium with canonical URL back to minimal3dp.com.

This script:
1. Parses Hugo markdown front matter and content
2. Converts Hugo shortcodes to Medium-compatible HTML/markdown
3. Uploads content to Medium via API with canonical_url
4. Returns Medium post URL and publication status

Usage:
    python scripts/post_to_medium.py content/blog/posts/my-post/index.md

Requirements:
    - MEDIUM_API_TOKEN environment variable
    - Post must have title and be published (draft: false)
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import requests


def parse_front_matter(content: str) -> Tuple[Dict, str]:
    """
    Parse YAML front matter and markdown content.
    
    Returns:
        Tuple of (front_matter_dict, markdown_content)
    """
    # Match YAML front matter between --- delimiters
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        raise ValueError("No valid front matter found")
    
    front_matter_str = match.group(1)
    markdown_content = match.group(2)
    
    # Simple YAML parser (handles basic key: value pairs)
    front_matter = {}
    for line in front_matter_str.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            # Handle boolean values
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            front_matter[key] = value
    
    return front_matter, markdown_content


def convert_shortcodes_to_html(content: str, post_url: str) -> str:
    """
    Convert Hugo shortcodes to Medium-compatible HTML.
    
    Medium supports basic HTML but strips complex elements.
    We'll convert common shortcodes to simple equivalents.
    """
    # Convert youtube-embed to iframe
    def replace_youtube(match):
        video_id = match.group(1)
        return f'<iframe src="https://www.youtube.com/embed/{video_id}" width="560" height="315" frameborder="0" allowfullscreen></iframe>'
    
    content = re.sub(
        r'{{\s*<\s*youtube-embed\s+id="([^"]+)"[^>]*>\s*}}',
        replace_youtube,
        content
    )
    
    # Convert imgproc to simple img tags with absolute URLs
    def replace_imgproc(match):
        img_name = match.group(1)
        # Construct absolute URL to your site
        return f'![Image]({post_url.rsplit("/", 1)[0]}/{img_name})'
    
    content = re.sub(
        r'{{\s*<\s*imgproc\s+([^\s]+)[^>]*>\s*}}',
        replace_imgproc,
        content
    )
    
    # Convert alert shortcode to blockquote
    content = re.sub(
        r'{{\s*<\s*alert[^>]*>\s*}}(.*?){{\s*</\s*alert\s*>\s*}}',
        r'> \1',
        content,
        flags=re.DOTALL
    )
    
    # Remove unsupported shortcodes (popular-videos, cta, etc.)
    # Replace with a note
    content = re.sub(
        r'{{\s*<\s*popular-videos[^>]*>\s*}}',
        '\n\n*[More content available on minimal3dp.com]*\n\n',
        content
    )
    
    content = re.sub(
        r'{{\s*<\s*cta[^>]*>\s*}}.*?{{\s*</\s*cta\s*>\s*}}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove faq shortcodes (Medium doesn't support structured data)
    content = re.sub(
        r'{{\s*<\s*faq[^>]*>\s*}}.*?{{\s*</\s*faq\s*>\s*}}',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content


def add_footer(content: str, canonical_url: str) -> str:
    """
    Add footer with link back to original post.
    """
    footer = f"""

---

*Originally published at [minimal3dp.com]({canonical_url})*
"""
    return content + footer


def post_to_medium(
    title: str,
    content: str,
    canonical_url: str,
    tags: Optional[list[str]] = None,
    publish_status: str = "draft"
) -> Dict:
    """
    Post content to Medium via API.
    
    Args:
        title: Post title
        content: Post content (markdown or HTML)
        canonical_url: URL of original post on your site
        tags: List of tags (max 5)
        publish_status: "public", "draft", or "unlisted"
    
    Returns:
        API response with post URL and ID
    """
    api_token = os.getenv('MEDIUM_API_TOKEN')
    if not api_token:
        raise ValueError("MEDIUM_API_TOKEN environment variable not set")
    
    # Get authenticated user ID
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    user_response = requests.get('https://api.medium.com/v1/me', headers=headers)
    user_response.raise_for_status()
    user_id = user_response.json()['data']['id']
    
    # Prepare post data
    post_data = {
        'title': title,
        'contentFormat': 'markdown',
        'content': content,
        'canonicalUrl': canonical_url,
        'publishStatus': publish_status
    }
    
    if tags:
        # Medium limits to 5 tags
        post_data['tags'] = tags[:5]
    
    # Create post
    post_response = requests.post(
        f'https://api.medium.com/v1/users/{user_id}/posts',
        headers=headers,
        json=post_data
    )
    post_response.raise_for_status()
    
    return post_response.json()['data']


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/post_to_medium.py <path-to-post>")
        print("Example: python scripts/post_to_medium.py content/blog/posts/my-post/index.md")
        sys.exit(1)
    
    post_path = Path(sys.argv[1])
    
    if not post_path.exists():
        print(f"Error: File not found: {post_path}")
        sys.exit(1)
    
    # Read post content
    with open(post_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse front matter
    try:
        front_matter, markdown_content = parse_front_matter(content)
    except ValueError as e:
        print(f"Error parsing front matter: {e}")
        sys.exit(1)
    
    # Validate required fields
    if 'title' not in front_matter:
        print("Error: Post must have a 'title' in front matter")
        sys.exit(1)
    
    if front_matter.get('draft', False):
        print("Warning: Post is marked as draft. It will be posted as draft on Medium.")
        publish_status = 'draft'
    else:
        publish_status = 'public'
    
    # Construct canonical URL
    # Extract post slug from path (e.g., content/blog/posts/my-post/index.md -> my-post)
    post_slug = post_path.parent.name
    canonical_url = f"https://minimal3dp.com/blog/posts/{post_slug}/"
    
    # Convert Hugo shortcodes
    processed_content = convert_shortcodes_to_html(markdown_content, canonical_url)
    
    # Add footer with link back
    processed_content = add_footer(processed_content, canonical_url)
    
    # Extract tags if present
    tags = None
    if 'tags' in front_matter:
        tags_str = front_matter['tags']
        if isinstance(tags_str, str):
            # Handle YAML array format: [tag1, tag2] or plain string
            tags = [t.strip().strip('[]"\'') for t in tags_str.split(',')]
    
    # Post to Medium
    print(f"Posting '{front_matter['title']}' to Medium...")
    print(f"Canonical URL: {canonical_url}")
    print(f"Publish status: {publish_status}")
    
    try:
        result = post_to_medium(
            title=front_matter['title'],
            content=processed_content,
            canonical_url=canonical_url,
            tags=tags,
            publish_status=publish_status
        )
        
        print("\n✅ Successfully posted to Medium!")
        print(f"Medium URL: {result['url']}")
        print(f"Post ID: {result['id']}")
        print(f"Status: {result['publishStatus']}")
        
        # Save result to output for GitHub Actions
        github_output = os.getenv('GITHUB_OUTPUT')
        if github_output:
            with open(github_output, 'a') as f:
                f.write(f"medium_url={result['url']}\n")
                f.write(f"medium_id={result['id']}\n")
        
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ Error posting to Medium: {e}")
        print(f"Response: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
