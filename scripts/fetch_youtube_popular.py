#!/usr/bin/env python3
"""
Fetch most popular videos from YouTube channel using YouTube Data API v3.
Writes to static/data/youtube-popular.json

Requires:
- YOUTUBE_API_KEY environment variable
- YOUTUBE_CHANNEL_ID environment variable (or uses default from script)

Output format:
{
  "videos": [
    {
      "id": "VIDEO_ID",
      "title": "Video Title",
      "description": "Video description...",
      "thumbnail": "https://i.ytimg.com/vi/VIDEO_ID/maxresdefault.jpg",
      "url": "https://www.youtube.com/watch?v=VIDEO_ID",
      "publishedAt": "2025-01-01T00:00:00Z",
      "viewCount": 12345,
      "likeCount": 123,
      "commentCount": 45
    },
    ...
  ],
  "fetched_at": "2025-11-19T20:00:00Z"
}
"""
import json
import os
import sys
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration
API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID', 'UCM_8Mv-0S1LnnJpRJLjahaw')
OUTPUT_PATH = os.getenv('OUTPUT_PATH', 'data/youtube_popular.json')
MAX_VIDEOS = int(os.getenv('MAX_VIDEOS', '3'))
DAYS_AGO = int(os.getenv('DAYS_AGO', '180'))  # Look back 6 months for popular videos

if not API_KEY:
    print("ERROR: YOUTUBE_API_KEY environment variable not set", file=sys.stderr)
    sys.exit(1)

if not CHANNEL_ID:
    print("ERROR: YOUTUBE_CHANNEL_ID environment variable not set", file=sys.stderr)
    sys.exit(1)

def fetch_popular_videos():
    """Fetch most popular videos from the channel."""
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        
        # Calculate date for filtering recent videos
        published_after = (datetime.utcnow() - timedelta(days=DAYS_AGO)).strftime('%Y-%m-%dT%H:%M:%SZ')
        
        # Step 1: Get the uploads playlist ID for the channel
        channel_response = youtube.channels().list(
            part='contentDetails',
            id=CHANNEL_ID
        ).execute()
        
        if not channel_response.get('items'):
            print(f"ERROR: Channel {CHANNEL_ID} not found", file=sys.stderr)
            sys.exit(1)
        
        uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        # Step 2: Get videos from the uploads playlist
        videos = []
        next_page_token = None
        
        while len(videos) < 50:  # Fetch up to 50 videos to sort by popularity
            playlist_response = youtube.playlistItems().list(
                part='snippet,contentDetails',
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()
            
            for item in playlist_response.get('items', []):
                video_id = item['contentDetails']['videoId']
                published_at = item['snippet']['publishedAt']
                
                # Filter by date
                if published_at >= published_after:
                    videos.append(video_id)
            
            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break
        
        if not videos:
            print(f"WARNING: No videos found in the last {DAYS_AGO} days", file=sys.stderr)
            # Fall back to all videos
            videos = []
            playlist_response = youtube.playlistItems().list(
                part='contentDetails',
                playlistId=uploads_playlist_id,
                maxResults=50
            ).execute()
            
            for item in playlist_response.get('items', []):
                videos.append(item['contentDetails']['videoId'])
        
        # Step 3: Get video statistics
        video_details = []
        for i in range(0, len(videos), 50):  # API allows max 50 IDs per request
            batch = videos[i:i+50]
            stats_response = youtube.videos().list(
                part='snippet,statistics',
                id=','.join(batch)
            ).execute()
            
            for video in stats_response.get('items', []):
                video_id = video['id']
                snippet = video['snippet']
                stats = video['statistics']
                
                # Robust thumbnail selection with graceful fallback
                thumbs = snippet.get('thumbnails', {})
                thumb_url = None
                for key in ['maxres', 'standard', 'high', 'medium', 'default']:
                    if key in thumbs:
                        thumb_url = thumbs[key]['url']
                        break
                if not thumb_url:
                    # Fallback pattern (may not exist for all videos, hqdefault is common)
                    thumb_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"

                video_details.append({
                    'id': video_id,
                    'title': snippet['title'],
                    'description': snippet.get('description', '')[:200],  # Truncate description
                    'thumbnail': thumb_url,
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'publishedAt': snippet['publishedAt'],
                    'viewCount': int(stats.get('viewCount', 0)),
                    'likeCount': int(stats.get('likeCount', 0)),
                    'commentCount': int(stats.get('commentCount', 0))
                })
        
        # Sort by view count (descending)
        video_details.sort(key=lambda x: x['viewCount'], reverse=True)
        
        # Return top N videos
        return video_details[:MAX_VIDEOS]
        
    except HttpError as e:
        print(f"ERROR: YouTube API error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function."""
    print(f"Fetching popular videos from channel {CHANNEL_ID}...")
    
    popular_videos = fetch_popular_videos()
    
    output = {
        'videos': popular_videos,
        'fetched_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    # Write to file
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✓ Wrote {len(popular_videos)} videos to {OUTPUT_PATH}")
    for i, video in enumerate(popular_videos, 1):
        print(f"  {i}. {video['title']} ({video['viewCount']:,} views)")

if __name__ == '__main__':
    main()
