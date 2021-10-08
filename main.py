from pytube import Playlist
from pytube import StreamQuery
import os


folder = ""
bad_extension = ".mp4"
good_extension = ".mp3"


def checking_folder():
    """Creates a folder where files will be downloaded"""
    path = input("Enter the name of the folder to store the playlist: ")
    global folder
    # Change the folder path to your wish
    folder = f"M:\Muza\mp3\YoutubePlaylists\{path}"
    check_folder = os.path.isdir(folder)
    if not check_folder:
        os.makedirs(folder)
        print(f"The {folder} folder has been created.")
    else:
        print(f"The {folder} folder already exists.")


def run():
    checking_folder()
    playlist = input("Paste a link to your playlist: ")
    p = Playlist(playlist)
    print(f"Downloading: {p.title}")
    for file in p.videos:
        StreamQuery.filter(file.streams, type="audio", adaptive=True).first().download(folder)
        print(file.title)
        bad_file = file.title + bad_extension
        good_file = file.title + good_extension
        os.chdir(folder)
        os.rename(bad_file, good_file)


if __name__ == "__main__":
    run()
