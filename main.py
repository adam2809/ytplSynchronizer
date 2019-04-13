import subprocess
import os
import pprint
from pytube import YouTube

AUDIO_FILES_DEST_PATH = 'downloadedAudioFiles'

def run_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    # Returns a (output, error) pair
    return process.communicate()


def put_file_on_connected_device(source, dest):
    output, error = run_command(f"adb push {source} {dest}")
    if error:
        print(f"An error ocurred:\n\n{error}\n\n")
    print("Output of the command:\n\n")
    print(output)


def downloadedAudioFilesFromYT(urls):
    for url in urls:
        try:
            ytVideo = YouTube(url)
        except:
            raise Exception('An error ocurred while creating YouTube object')
        audioFiles = ytVideo.streams.filter(only_audio=True).all()
        print("Downloading video...")
        try:
            audioFiles[1].download(AUDIO_FILES_DEST_PATH)
        except:
            print("Error while downloading video!")
        print("Video downloaded!")


if __name__ == '__main__':
    urls = ['https://www.youtube.com/watch?v=xWOoBJUqlbI']
    downloadedAudioFilesFromYT(urls)
