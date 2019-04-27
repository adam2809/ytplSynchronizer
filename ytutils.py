from pytube import YouTube
from bs4 import BeautifulSoup
import requests

class YoutubeAudioFilesDownloader:
    def __init__(self, urls, dest_path):
        # urls get zipped with an array of Falses to keep track of which files were
        # already downloaded (False if not True if yes)
        self.url_isdownloaded_pairs = ziplist(urls,[False for i in range(len(urls))])
        self.dest_path = dest_path


    def ziplist(a,b):
        return [list(x) for x in zip(a,b)]


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



class YouTubePlaylistInfo:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text,'lxml')
        self.update_info()


    def get_new_and_deleted_urls(self):
        old_content_urls = content_urls[:]
        self.update_info()
        return (list_diff(self.content_urls, old_content_urls),
                list_diff(old_content_urls - self.content_urls))


    def update_info(self):
        self.update_content_urls()
        self.update_title()


    def update_content_urls(self):
        wanted_class = 'pl-video-title-link'
        found_links = []
        for a in self.soup.find_all('a'):
            try:
                curr_class = a['class']
            except:
                continue
            if wanted_class in curr_class:
                found_links.append(a['href'])
        self.content_urls = found_links.copy()


    def update_title(self):
        self.title = self.soup.find('h1',attrs={'class':'pl-header-title'}).text.strip()


def list_diff(a, b):
    return list(set(a) - set(b))
