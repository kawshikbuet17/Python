#pip install pytube

import pytube

url = "https://www.youtube.com/watch?v=rUWxSEwctFU"

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(22) #22 for 720p
print("downloading...")
stream.download(filename="kkp_download_"+str(video.title))
print("downloaded...")


"""
for stream in video.streams:
    if "video" in str(stream) and "mp4" in str(stream):
        print(stream)
"""

# itag="22" is for 720p videos
# printing stream from video.streams will print itags. we can use itag=22 for 720p for any videos in youtube (if 720 exists).