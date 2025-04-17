#from pytube import Search
#from pytube import YouTube
#   youtubeObject = YouTube(link)
  #  youtubeObject = youtubeObject.streams.get_highest_resolution()
 #    youtubeObject = youtubeObject.streams.filter(progressive=True).first()

  #
  #    print("an Error has occurred")
    #print("Download is completed successfully")
#
#link =input("enter the link of the video you want to download")
#Download(link)
from pytube import YouTube
from urllib.error import HTTPError

def Download(link):
    try:
        youtubeObject = YouTube(link)
        stream = youtubeObject.streams.get_highest_resolution()
        stream.download()
        print("Download successful")
    except HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

link = input("enter the link")
Download(link)