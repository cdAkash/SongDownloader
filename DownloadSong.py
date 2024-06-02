import os
from googleapiclient.discovery import build
import yt_dlp as youtube_dl


def get_youtube_links(api_key, search_queries):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    links = {}
    
    for query in search_queries:
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=1
        )
        response = request.execute()
        
        if response['items']:
            video_id = response['items'][0]['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            links[query] = video_url
        else:
            links[query] = "No results found"
    
    return links

def download_youtube_as_mp3(youtube_url, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'quiet': True
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    # Set your YouTube Data API key here
    api_key = 'AIzaSyDTo74dfntklvGIj7GmfnnC9XXSuGchmJI'
    
    # List of songs to search for
    # if(len(sys.argv)==1):
    #     songs =[ input("enter the song name ")]
    # else:
    #     songs=sys.argv[1::]
    # you can use either this part to take input directly from CLI or use the list to download in bulk.
    songs = [
        "Chand se parda kijiye",
    "Zara fir se kehna",
    "Phool mangu na bahaar mangu"
    ]
    #^^ put all your search key(songs)inside the third bracket under double quotes and separated by comma


    # Output directory for downloaded MP3 files
    output_directory = "/home/heckerrr/Documents/SongDownloader/songs"


    # Get YouTube video links for the songs
    links = get_youtube_links(api_key, songs)

    for song, link in links.items():
        if link != "No results found":
                # Download the video as MP3
                download_youtube_as_mp3(link, output_directory)
                print(f"Downloaded {song}")

                
