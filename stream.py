import ffmpeg
import os
import random
import time
from dotenv import load_dotenv

load_dotenv()

# video = ffmpeg.input('bkg.png',loop=1).video
video = ffmpeg.input('bkg.gif',stream_loop=-1).video

output = f'rtmp://a.rtmp.youtube.com/live2/{os.environ["KEY"]}'

songs = os.listdir('./music/')

while True:
    audio_path = './music/' + random.choice(songs)
    audio = ffmpeg.concat(ffmpeg.input(audio_path),v=0,a=1)
    
    filename = os.path.basename(audio_path).rsplit('.', 1)[0]

    print(f"Now Playing >> {filename}")

    
    video_with_text = video.drawtext(
        text=filename,
        fontfile='./font.ttf',
        fontsize=48,
        fontcolor='white',
        x='(w-text_w)/2', 
        y='(h-text_h)-48',
    )
    (
        ffmpeg
        .output(
            video_with_text,audio,
            output,
            format='flv',
            video_bitrate='6800k',
            bufsize='5000k',
            audio_bitrate='128k',
            vcodec='libx264',
            acodec='aac',
            preset='veryfast',
            framerate = 30,
            shortest=None
        )
        .run(quiet=True)
    )