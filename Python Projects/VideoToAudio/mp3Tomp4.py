import moviepy.editor
from tkinter.filedialog import *


vid=askopenfilename()
video=moviepy.editor.VideoFileClip(vid)

aud=video.audio
aud.write_audiofile("demo.mp3")

print("Video converted to audio")


path="C:\Users\Valeska\Desktop\Learn Valeska\Python Projects\YoutubeDownload"
des=""
mp3(path,des)