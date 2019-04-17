import subprocess
import os
import pprint
from pytube import YouTube
from bs4 import BeautifulSoup
import requests

DOWNLOADED_FILES_PATH = 'downloadedAudioFiles'
DEST_PATH_ON_DEVICE = '/sdcard/testPlaylist'

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


def download_audio_files_from_yt(urls):
    for url in urls:
        try:
            ytVideo = YouTube(url)
        except:
            raise Exception('An error ocurred while creating YouTube object')
        audioFiles = ytVideo.streams.filter(only_audio=True).all()
        print("Downloading video...")
        try:
            audioFiles[1].download(DOWNLOADED_FILES_PATH)
        except:
            print("Error while downloading video!")
        print("Video downloaded!")


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


if __name__ == '__main__':
    # Test for downloading audio from a video and putting in on the connected device
    # urls = ['https://www.youtube.com/watch?v=xWOoBJUqlbI']
    # download_audio_files_from_yt(urls)
    # put_file_on_connected_device(DOWNLOADED_FILES_PATH, DEST_PATH_ON_DEVICE)

    # Test for getting a list of video urls from a playlist
    url = 'https://www.youtube.com/playlist?list=PL1WyaSvUwdxcXb-V08h4rsRLjGCjKoUVd'
    print(get_yt_playlist_contents(url))
