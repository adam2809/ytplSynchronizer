import subprocess
import os
import pprint

from ytutils import YouTubePlaylistInfo, YoutubeAudioFilesDownloader

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


class PlaylistSynchronizer:
    BASE_PATH_LOCAL = 'synchedPlaylistsLocalPath'
    BASE_PATH_ON_DEVICE = '/sdcard/'


    def __init__(self, url):
        self.playlist_info = YouTubePlaylistInfo(url)
        self.curr_synched_urls = []
        self.urls_to_delete = []
        self.urls_to_download = playlist_info.content_urls


    def synchronize(self):
        pass


    def update_which_to_delete_and_download(self):
        pass


    def delete(self):
        pass


    def download(self):
        pass


    def put_downloaded_files_on_device(self):
        pass



'An error ocurred while extracting the playlists info. Make sure the URL is correct. The synchronizer initialization is aborted'

if __name__ == '__main__':
    test_playlist = YouTubePlaylist('https://www.google.com/')
    print(test_playlist.title)
    print(test_playlist.content_urls)
