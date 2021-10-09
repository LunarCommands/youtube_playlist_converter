from pytube import Playlist
from pytube import StreamQuery
import os


folder = ""
bad_extension = ".mp4"
good_extension = ".mp3"


def check_folder():
    """Creates a folder where files will be downloaded"""
    path = input("Enter the name of the folder to store the playlist: ")
    global folder
    # Change the folder path to your wish
    folder = f"M:\Muza\mp3\YoutubePlaylists\{path}"
    checking_folder = os.path.isdir(folder)
    if not checking_folder:
        os.makedirs(folder)
        print(f"The {path} folder has been created.")
    else:
        print(f"The {path} folder already exists.")


def get_rid_of_symbols(path):
    """Gets rid of the symbols in the name of downloading video that StreamQuery deletes"""
    return ''.join(c for c in path if (c != '.') and (c != '|') and (c != ':')
                   and (c != '"') and (c != '\'') and (c != '\\') and (c != '/')
                   and (c != ',') and (c != '?') and (c != ';') and (c != '/<')
                   and (c != '>') and (c != '$') and (c != '#'))


def run():
    """Downloads each file in the playlist as a .mp4 and changes it to a .mp3 extension."""
    check_folder()
    playlist = input("Paste a link to your playlist: ")
    p = Playlist(playlist)
    print(f"Downloading: {p.title}")

    for file in p.videos:
        try:
            StreamQuery.filter(file.streams, type="audio", adaptive=True).first().download(folder)
            print(file.title)
            bad_file = get_rid_of_symbols(file.title) + bad_extension
            good_file = get_rid_of_symbols(file.title) + good_extension
            os.chdir(folder)
            os.rename(bad_file, good_file)
        except FileExistsError:
            print("File already exists.\n")
            os.remove(folder + "\\" + get_rid_of_symbols(file.title) + bad_extension)


if __name__ == "__main__":
    run()
