import os
try:
    from pytube import YouTube
except ModuleNotFoundError:
    os.system("python -m pip install pytube")
    print("PyTube installed on your device!")
    from pytube import YouTube
    print("Let's countinue!!! ;)")

def runDownloader(yt):
    print(yt.title,"is downloading! ⏳")
    video = yt.streams.filter(only_audio=True).last()
    out_file = video.download(output_path="Music")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully download! ✅\n---------------")

# Read files only!
try:
    music_note = open("list.txt","r")
except FileNotFoundError:
    open("list.txt","w")
    print("list.txt has created! Please insert any URLs from YouTube!")
    exit()
file_note = []
for fNotes in music_note.readlines():
    file_note.append(fNotes.strip('\n'))

for noFiles in file_note:
    runDownloader(YouTube(noFiles))
