import os
import threading
try:
    from pytube import YouTube
    import pygame
    import tkinter as tk
except ModuleNotFoundError:
    os.system("python -m pip install pytube")
    print("PyTube installed on your device!")
    os.system("python -m pip install pygame")
    print("Pygame installed on your device!")

    if os.name != "nt":
        os.system("sudo apt-get install python3-tk")

    print("Run this script again! ;)")
    exit()

def runDownloader(yt):
    try:
        music_dwn.configure(text=f"{yt.title} is downloading!")
        print(yt.title,"is downloading! ⏳")
        video = yt.streams.filter(only_audio=True).last()
        out_file = video.download(output_path="Music")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully download! ✅\n---------------")
    except:
        music_dwn.configure(text="[Error!] - Check in console")
        print("[Error!] - Please check your URLs or Folder and try again")
        print("[Error!] - If can't download again please try to use runDownloader_debug() to download.")
        print("[Error!] - You can edit code on line 39 to debug error")
        btn_submit.configure(state="normal")
        exit()

def runDownloader_debug(yt):
    music_dwn.configure(text=f"{yt.title} is downloading!")
    print(yt.title,"is downloading! ⏳")
    video = yt.streams.filter(only_audio=True).last()
    out_file = video.download(output_path="Music")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully download! ✅\n---------------")


pygame.init()
os.system('cls' if os.name=='nt' else 'clear')
complete_sound = pygame.mixer.Sound("complete.mp3")

def startDownload(link: list):
    for l in link:
        runDownloader(YouTube(l))
        # runDownloader_debug(YouTube(l))
    os.system('cls' if os.name=='nt' else 'clear')
    print("=================== [✅] ===================")
    print("Download successfully!")
    print("=================== [✅] ===================")
    complete_sound.play()
    music_dwn.configure(text="Successfully!")
    os.system('explorer Music' if os.name=='nt' else '')
    btn_submit.configure(state="normal")

def start_cli():
    btn_submit.configure(state="disabled")
    link_all = link.get("1.0", "end-1c")
    link_note = link_all.splitlines()
    thr = threading.Thread(target=startDownload, args=[link_note])
    thr.start()

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("720x600")
root.resizable(0,0)

root.configure(bg="#6C3428")
title = tk.Label(
    root, 
    text="Music Downloader",
    font=('',20),
    bg="#C38154",
    fg="#FFFFFF"
)

link = tk.Text(
    root,
    width=80
)

music_dwn = tk.Label(
    root,
    text="Wating for downloading!",
    bg="#7D7463",
    fg="#FFFFFF"
)

btn_submit = tk.Button(
    root,
    text="Download!",
    bg="#C38154",
    fg="#FFFFFF",
    font=('',18),
    command=start_cli
)

credit = tk.Label(
    root,
    text="Council PCSHSST (2565-2566) - IT Department",
)

title.pack(pady=20)
link.pack()
music_dwn.pack(pady=4)
btn_submit.pack(pady=15)
credit.pack(side=tk.BOTTOM)

root.mainloop()