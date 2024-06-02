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
    api_key = 'AIzaSyC6SzB_mkZDD8aG-Htq0xyBzl9VrCO6cMU'
    
    # List of songs to search for
    songs = [
        "Chand se parda kijiye",
    "Zara fir se kehna",
    "Phool mangu na bahaar mangu",
    "Tuze na dekhu toh chain",
    "Dheere dheere se",
    "Ek tere hi chehre pr pyar aaya",
    "Dil kehta hai",
    "Haan ek sanam chaiye",
    "Mera dil bhi kitna pagal hai",
    "Tumhe apna banane ki kasam",
    "Tum Dil ki dhadkan mein",
    "Dekh ne walo'n ne",
    "Is tarha aashiqi ka",
    "Zindgi badal di",
    "Teri ummeed tera intezaar",
    "Aaye ho meri zindgi mein",
    "Kaash koi ladki",
    "Beshaq tum meri mohabbat ho",
    "Aksar is duniyan mein",
    "Ek yesi ladki thii",
    "Mujhe jeene nahi deti hai",
    "Sheesha ho ya Dil ho",
    "Mera chand muze aaya hai",
    "Aankh hai bhari bhari",
    "Tu meri zindagi hai",
    "Aane se uske aaye bahaar",
    "Gawah hai chand tare",
    "Shikwa nahi kisi se",
    "Bepanah pyar hai",
    "Chand ke paar chalo",
    "Sochenge tumhe pyar",
    "Kasam kha ke kaho",
    "Chand taron me nazar aaye",
    "Kisi se tum pyar karo",
    "Tere naam humne kiya hai",
    "Aaye mere humsafar",
    "Jab se tumko dekha hai",
    "Har dil jo pyar karega",
    "Dil ke badley sanam",
    "Jhanjhariy",
    "Hoshwalon ko khabar kya",
    "Raja ko Rani se pyar",
    "Kitaben bahut si padhi hogi",
    "Laal dupatta",
    "Pyar ki ek kahaani",
    "Paas woh aane lage",
    "Dil hai ki manta nahi",
    "Aapke pyar mein",
    "Barsaat ke Mausam mein",
    "Chand chupa badal me",
    "Surili Akhiyon Wale",
    "Aaj kehna jaroori hai ki",
    "Saajan saajan teri dulhan",
    "Pehla pehla pyar hai",
    "Tu Shayar hai me Teri",
    "Badi mushkil hai",
    "Humko Aaj kal hai intezaar",
    "Ore Piya",
    "Tumse milne ki tamnna hai",
    "Ek ajnabi Haseena se",
    "Tere Ishq me pagal",
    "Pehli pehli baar mohabbat",
    "Kyoki itna pyar tumko",
    "Jeena sirf mere liye",
    "Dil hai tumhara",
    "Wada raha sanam",
    "Sathiya ye tune kya kiyan",
    "Ye dua hai meri rab se",
    "Ghoonghat ki aad mein",
    "Chori chori dil tera",
    "Aankho me base ho tum",
    "Dil me dard sa",
    "Har Dil Jo pyar karega",
    "Tu dharti pe chaahe jaha",
    "Pucho jara pucho",
    "Rab kare tuzko bhi",
    "Oodhni",
    "Meri mehbooba",
    "Kyun kisi ko",
    "Mere rang me rangne wali",
    "Choori maza na degi",
    "O o jaane jaana",
    "Choti choti raten",
    "Chand taren phool shabnam",
    "Tere dar par sanam",
    "Tauba tumhare ye ishare",
    "Jise dekh mera dil",
    "Suno na suno na",
    "Is pyar se meri taraf na dekho",
    "Aise deewangi dekhi nahi"
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

                
