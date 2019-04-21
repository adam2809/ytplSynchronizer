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




def get_yt_playlist_contents(playlist_url):
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.text,'lxml')
    wanted_class = 'pl-video-title-link'
    found_links = []
    for a in soup.find_all('a'):
        try:
            curr_class = a['class']
        except:
            continue
        if wanted_class in curr_class:
            found_links.append(a['href'])
    return found_links


def get_tracked_playlists():
    trackedPlaylists = {}
    with open(TRACKED_PLAYLISTS_FILE_PATH) as trackedPlaylistsFile:
        for line in trackedPlaylistsFile:
            title, url = line.split()
            trackedPlaylists[title] = url
    return trackedPlaylists


class YoutubeAudioFilesDownloader:
    def __init__(self, urls, dest_path_on_device, dest_path_local):
        self.urls = urls
        self.dest_path_on_device = dest_path_on_device
        self.dest_path_local = dest_path_local


    def add_url(self):
        pass


    def download_all_files_from_urls(self):
        pass


    def download_file_from_url(self, url):
        pass


if __name__ == '__main__':
    trackedPlaylists = get_tracked_playlists()
