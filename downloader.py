from pytube import Playlist
from pytube import YouTube

previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
     
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(liveprogress)

 
playlist_url = 'https://www.youtube.com/playlist?list=PLlyCyjh2pUe9wv-hU4my-Nen_SvXIzxGB'

p = Playlist(playlist_url)
for i, url in enumerate(p.video_urls):
    # if i<35:
    #     continue
    try:
        yt = YouTube(url)
    except VideoUnavailable:
        print(f'{i} Video {url} is unavaialable, skipping.')
    else:
        print(f'{i} Downloading video: {url}')
        previousprogress = 0
        yt.register_on_progress_callback(on_progress)
        print(yt.title)
        yt.streams.first().download()
        
# yt = YouTube('https://www.youtube.com/watch?v=4zqKJBxRyuo&ab_channel=SleepEasyRelax-KeithSmith')
# yt.register_on_progress_callback(on_progress)
# yt.streams.filter(only_audio=True).first().download()