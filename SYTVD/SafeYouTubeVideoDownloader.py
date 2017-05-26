import important_dont_delete
video_link = 'https://www.youtube.com/watch?v=ze5k5TG2bmA'
yt = important_dont_delete.YouTube(video_link)
videos = yt.get_videos()
print('Information about video:')
print('FORMATS & SIZES:')
for v in videos:
    print(v)


first_video = videos[0]
print(first_video)

first_video.extension


audio_bitrate = first_video.audio_bitrate
video_bitrate = first_video.video_bitrate
print('audio bitrate: ',audio_bitrate)
print('video bitrate: ',video_bitrate)


videos = yt.videos
video = yt.get('.mp4', '360p')

path = '/Users/Fazan/Desktop'
video.download(path)
