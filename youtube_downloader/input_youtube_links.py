import pytube

video_list = []

print("Enter URLS ('STOP' to stop input)")

while True:
    url = input("")
    if url == 'STOP':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(22)
    print(f"Downloading video {x+1}...")
    stream.download()
    print("Done")