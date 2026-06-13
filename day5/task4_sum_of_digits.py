import re
fm youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    """Extracts the 11-character YouTube video ID from a URL."""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_youtube_transcript(video_id):
    """Fetches and cleans the transcript from YouTube."""
    try:
        # Fetch the raw transcript chunks
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Clean text: Loop through chunks and join them into a single paragraph
        text_list = [chunk['text'] for chunk in raw_transcript]
        clean_text = " ".join(text_list)
        return clean_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

def save_to_txt(text, filename="transcript.txt"):
    """Saves the final clean text into a .txt file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Success! Transcript saved to {filename}")

# --- Execution ---
if __name__ == "__main__":
    # Input your YouTube URL here
    youtube_url = "https://youtube.com" 
    
    # Step 1: Get ID
    video_id = extract_video_id(youtube_url)
    
    if video_id:
number_str = input("enter a number:")

digit_sum = 0
for char in number_str:
    digit_sum = digit_sum + int(char)

print("sum of digits(Loop):",digit_sum)

num_val = int(number_str)
math_sum = 0

while num_val > 0:
    last_digit = num_val % 10
    math_sum = math_sum + last_digit
    num_val = num_val // 10

print("sum of digits(Mathematical):",math_sum)    