import subprocess
import os
import pprint
from pytube import YouTube
from bs4 import BeautifulSoup
import requests

TRACKED_PLAYLISTS_FILE_PATH = 'trackedPlaylists.txt'

prnt = pprint.PrettyPrinter(indent=4).pprint

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # Returns a (output, error) pair
    return process.communicate()


def put_file_on_connected_device(source, dest):
    output, error = run_command(f"adb push {source} {dest}")
    output, error = str(output), str(error)
    if error:
        print(f"An error ocurred:")
        print(error)
    print("Output of the command:")
    print(output)





def get_tracked_playlists():
    trackedPlaylists = {}
    with open(TRACKED_PLAYLISTS_FILE_PATH) as trackedPlaylistsFile:
        for line in trackedPlaylistsFile:
            title, url = line.split()
            trackedPlaylists[title] = url
    return trackedPlaylists


def ziplist(a,b):
    return [list(x) for x in zip(a,b)]



class YoutubeAudioFilesDownloader:
    def __init__(self, urls, dest_path):
        # urls get zipped with an array of Falses to keep track of which files were
        # already downloaded (False if not True if yes)
        self.url_isdownloaded_pairs = ziplist(urls,[False for i in range(len(urls))])
        self.dest_path = dest_path


    def download_all_files_from_urls(self):
        list(map(self.download_error_checks,self.url_isdownloaded_pairs))


    def download_error_checks(self, url_isdownloaded_pair):
        url, is_downloaded = url_isdownloaded_pair
        if is_downloaded:
            print(f"{url} has already been downloaded")
            return
        try:
            self.download_file_from_url(url)
        except:
            print(f"Error while downloading {url}")
        else:
            url_isdownloaded_pair[1] = True


    def download_file_from_url(self, url):
        yt_video = YouTube(url)
        audio_files = yt_video.streams.filter(only_audio=True).all()
        print(f"Downloading {yt_video.title}...")
        audio_files[1].download(self.dest_path)
        print(f"{yt_video.title} was downloaded successfully!")


if __name__ == '__main__':
    urls = [
    'https://www.youtube.com/watch?v=nsufd9Ckiko',
    'https://www.youtube.com/watch?v=oG0XcvGLoq0',
    'https://www.youtube.com/watch?v=u7kaOntQbsw',
    ]
    dest_local = 'downloadedAudioFiles'
    test_batch = YoutubeAudioFilesDownloader(urls, dest_local)
    test_batch.download_all_files_from_urls()
