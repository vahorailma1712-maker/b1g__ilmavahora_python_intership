import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def extract_video_id(url: str) -> str:
    """Extracts the unique video ID from various YouTube URL formats."""
    pattern = r'(?:v=|\/embed\/|\/11\/|\/v\/|https:\/\/youtu\.be\/|\/shorts\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL provided.")

def get_clean_transcript(video_url: str) -> str:
    """Fetches the video transcript and formats it into plain paragraph text."""
    try:
        # 1. Parse out the 11-character video identifier
        video_id = extract_video_id(video_url)
        
        # 2. Fetch the raw transcript from YouTube
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # 3. Clean up the chunks into plain paragraphs without timestamps
        formatter = TextFormatter()
        clean_text = formatter.format_transcript(raw_transcript)
        
        return clean_text
        
    except Exception as e:
        return f"An error occurred while fetching the transcript: {e}"

# Example Usage
if __name__ == "__main__":
    # Replace with any valid YouTube URL
    youtube_link = "https://www.youtube.com/watch?v=TwJX9AHdnQg"
    
    transcript = get_clean_transcript(youtube_link)