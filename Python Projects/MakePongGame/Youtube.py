from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
def download_video(url,savepath):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=savepath)
        print("Video Downloaded successfully")

    except Exception as e:
        print(e)

url="https://youtu.be/AUtwSy-CqE8?si=RBvaBA4Zu9-6DjiB"
savepath="C:/Users/Valeska/Desktop/Learn Valeska/Python Projects/YoutubeDownload"

download_video(url,savepath)