This is a simple program for streaming music and background to youtube 24/7
# Install
First, install required module.
```bash
pip install -r requirements.txt
```
Now create a .env file, and write
```
KEY = (your stream key)
```

# Configure
## Background
You can see `bkg.gif` and `bkg.png` in the folder, and you can change them to what you want
The default is to use GIF, but it can be switched to PNG or by uncommenting this area
If you want to use JPG, just change .png to .jpg
```python
# video = ffmpeg.input('bkg.png',loop=1).video
video = ffmpeg.input('bkg.gif',stream_loop=-1).video
```
## Music
In `/music/`, you can put in music files you want
I put some Sky:cotl music for you to test

# Start Streaming
Run `stream.py` and it will start streaming
You may have to wait for seconds or restart the program a few times to connect to Youtube.