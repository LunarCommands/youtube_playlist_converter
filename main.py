from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re


folder = ""


def check_folder():
    """Creates a folder where files will be downloaded."""
    path = input("Enter the name of the folder to store the playlist: ")
    global folder
    # Change the folder path to your wish
    folder = f"/Users/lunar_commands/Music/{path}"
    checking_folder = os.path.isdir(folder)
    if not checking_folder:
        os.makedirs(folder)
        print(f"The {path} folder has been created.")
    else:
        print(f"The {path} folder already exists.")


def rename():
    """Changes all .mp4 files to .mp3."""
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder, file)
            mp3_path = os.path.join(folder, os.path.splitext(file)[0] + '.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)


def run():
    """Downloads each file in the playlist as a .mp4 and changes it to a .mp3 extension."""
    check_folder()
    playlist = input("Paste a link to your playlist: ")
    p = Playlist(playlist)

    for url in p:
        YouTube(url).streams.filter(adaptive=True, only_audio=True).first().download(folder)
        print(f"Downloading: {url}")

    rename()


if __name__ == "__main__":
    run()
