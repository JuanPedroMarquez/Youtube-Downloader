# https://pytubefix.readthedocs.io/en/latest/
# There is a library called pytubefix that seems to correct some pytube problems. It is a library that allows you to download videos from YouTube.
import pytubefix
from pytubefix import YouTube
from pytubefix.cli import on_progress

# Create a video variable that will access to the YouTube video you want to download with the URL of the video.
video = YouTube(url="https://www.youtube.com/watch?v=KVjBCT2Lc94", on_progress_callback=on_progress)

# Here you can print some information about the video you want to download. This is good to check that you are downloading the right video.
print("Author: ", video.author)
print("Title: ", video.title)
print("Length of the video in seconds: ", video.length)
print("Number of views: ", video.views)
print("Other information: ", video.video_id, video.watch_url)
print("Thumbnail: ", video.thumbnail_url)

# In case there are more than one download stream available, you should check the option and choose the one that fits your needs. 
# For example, you can check the progressive streams available (both audio and video in the same file) or audio only.
# In this case, this will not provide anything because there is only one stream available. Check the documentation for further information.
video.streams

# To download the video, one quick way to do it is to get the highest resolution stream and automatically download video and audio at the highest quality.
stream = video.streams.get_highest_resolution() # Get the highest resolution stream that is a progressive video (both audio and video available
                                                # in the same file). It may not be the BEST resolution video, but the video and audio files
                                                # may be separated in higher quality streams (adaptive videos). 

# And finally set the path where you want to save the video.
stream.download(r"Your path goes here") # Go to the folder where you want to save the video and paste the path here

# If you want to download the audio only, you can use the following code:
# stream = video.streams.get_audio_only()
# stream.download(r"Your path goes here") 
# This will download the highest bitrate audio stream available, audio only. 
# Notice that uncommenting the above lines and running the whole code will result in the highest quality file
# being substituted by the audio-only file, so be careful!
