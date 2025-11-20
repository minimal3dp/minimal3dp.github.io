#!/usr/bin/env python3
"""Post a Hugo markdown file to Dev.to via API.

Requires environment variable DEVTO_API_KEY.

Usage:
  python scripts/post_to_devto.py content/blog/posts/my-post/index.md --publish draft

Dev.to API docs: https://developers.forem.com/api
"""
from __future__ import annotations
import os
import sys
import re
import json
import argparse
from pathlib import Path
from typing import Tuple, Dict, List
import requests

FRONT_MATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*\n(.*)$', re.DOTALL)

SHORTCODE_PATTERNS = [
    (re.compile(r'{{\s*<\s*youtube-embed\s+id="([^"]+)"[^>]*>\s*}}'),
     lambda m: f'https://www.youtube.com/watch?v={m.group(1)}'),
    (re.compile(r'{{\s*<\s*alert[^>]*>\s*}}(.*?){{\s*</\s*alert\s*>\s*}}', re.DOTALL),
     lambda m: '> ' + m.group(1).strip().replace('\n', '\n> ')),
]

REMOVE_SHORTCODES = [
    re.compile(r'{{\s*<\s*(popular-videos|faq|cta)[^>]*>.*?{{\s*</\s*\1\s*>\s*}}', re.DOTALL),
    re.compile(r'{{\s*<\s*(popular-videos|faq|cta)[^/>]*>\s*}}', re.DOTALL),
]

IMGPROC_RE = re.compile(r'{{\s*<\s*imgproc\s+([^\s]+)[^>]*>\s*}}')


def parse_front_matter(raw: str) -> Tuple[Dict, str]:
    m = FRONT_MATTER_RE.match(raw)
    if not m:
        raise ValueError('Front matter missing')
    fm_block, body = m.group(1), m.group(2)
    fm: Dict[str, str] = {}
    for line in fm_block.splitlines():
        if ':' in line:
            k,v = line.split(':',1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def convert_shortcodes(body: str, canonical_url: str) -> str:
    for pattern, repl in SHORTCODE_PATTERNS:
        body = pattern.sub(repl, body)
    # imgproc -> standard image markdown (assumes images served at canonical path)
    def repl_img(m):
        img = m.group(1)
        base = canonical_url.rstrip('/')
        return f'![{img}]({base}/{img})'
    body = IMGPROC_RE.sub(repl_img, body)
    for pattern in REMOVE_SHORTCODES:
        body = pattern.sub('\n\n*Additional dynamic content available at original post.*\n\n', body)
    return body


def build_footer(canonical_url: str) -> str:
    return f"\n---\nOriginally published at {canonical_url}\n"


def post_to_devto(fm: Dict, content: str, canonical_url: str, publish: str) -> Dict:
    api_key = os.getenv('DEVTO_API_KEY')
    if not api_key:
        raise ValueError('DEVTO_API_KEY not set')
    url = 'https://dev.to/api/articles'
    tags: List[str] = []
    raw_tags = fm.get('tags') or ''
    if raw_tags.startswith('['):
        tags = [t.strip().strip('"').strip("'") for t in raw_tags.strip('[]').split(',') if t.strip()][:4]
    elif raw_tags:
        tags = [t.strip() for t in raw_tags.split(',')[:4]]
    payload = {
        'title': fm.get('title','Untitled'),
        'published': publish == 'public',
        'canonical_url': canonical_url,
        'body_markdown': content + build_footer(canonical_url),
    }
    if tags:
        payload['tags'] = tags
    headers = {'api-key': api_key, 'Content-Type':'application/json'}
    resp = requests.post(url, headers=headers, data=json.dumps({'article': payload}))
    if resp.status_code >= 300:
        raise RuntimeError(f'Dev.to error {resp.status_code}: {resp.text}')
    return resp.json()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('post_path')
    p.add_argument('--publish', choices=['draft','public'], default='draft')
    args = p.parse_args()
    post_file = Path(args.post_path)
    if not post_file.exists():
        print('File not found:', post_file)
        sys.exit(1)
    raw = post_file.read_text(encoding='utf-8')
    fm, body = parse_front_matter(raw)
    slug = post_file.parent.name
    canonical = f'https://minimal3dp.com/blog/posts/{slug}/'
    converted = convert_shortcodes(body, canonical)
    try:
        result = post_to_devto(fm, converted, canonical, args.publish)
    except Exception as e:
        print('Failed:', e)
        sys.exit(1)
    print('✅ Posted to Dev.to')
    print('URL:', result.get('url'))
    gh_out = os.getenv('GITHUB_OUTPUT')
    if gh_out and result.get('url'):
        with open(gh_out,'a') as f:
            f.write(f"devto_url={result['url']}\n")

if __name__ == '__main__':
    main()
