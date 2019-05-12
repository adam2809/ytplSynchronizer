import unittest
from ytplsynch import YouTubeAudioFilesDownloader
from os import listdir, remove
from io import StringIO
import sys

class DownloaderClassTests(unittest.TestCase):

    TEST_DEST = './downloadedTestFiles'

    def setUp(self):
        try:
            self.clearTestDestDirectory()
        except FileNotFoundError:
            print('TEST_DEST not yet created')
        sys.stdout = self.teststdout = StringIO()


    def clearTestDestDirectory(self):
        for file in listdir(self.TEST_DEST):
            try:
                os.remove(file)
            except e:
                self.fail(f'One of the files in {self.TEST_DEST} could not have been removed.')


    def tearDown(self):
        sys.stdout = sys.__stdout__


    def test_downloads_all_files_correct_urls(self):
        urls = [
        'https://www.youtube.com/watch?v=oG0XcvGLoq0',
        'https://www.youtube.com/watch?v=nsufd9Ckiko',
        'https://www.youtube.com/watch?v=u7kaOntQbsw',
        ]
        downloader = YouTubeAudioFilesDownloader(urls, self.TEST_DEST)
        downloader.download_all_files_from_urls()

        self.assertTrue(all(pair[1] for pair in downloader.url_isdownloaded_pairs),f'Actual pairs are:\n{downloader.url_isdownloaded_pairs}')

        files_in_test_dest = listdir(self.TEST_DEST)
        target_files = [
        'Alexander Robotnick - Undicidisco (Justin VanDerVolgen Edit).webm',
        'Tiger & Woods - Balloon.webm',
        'William Onyeabor - Better Change Your Mind (Official).webm'
        ]
        self.assertEqual(files_in_test_dest,target_files)


    def test_downloads_one_file_and_displays_msgs(self):
        downloader = YouTubeAudioFilesDownloader([],self.TEST_DEST)

        url = 'https://www.youtube.com/watch?v=oG0XcvGLoq0'
        downloader.download_file_from_url(url)

        target_msgs = [
        'Downloading Alexander Robotnick - Undicidisco (Justin VanDerVolgen Edit)...',
        '% downloaded'
        'Alexander Robotnick - Undicidisco (Justin VanDerVolgen Edit) was downloaded successfully!'
        ]
        self.assertTrue(self.teststdout_contains_all_elements_of_list(target_msgs),f'Actual output is:\n{self.teststdout.getvalue()}')


    def test_wrong_urls(self):
        wrong_urls = [
        'https://www.youtube.com/watch?v=u7kaOntQbsw&list=PL1WyaSvUwdxcXb-V08h4rsRLjGCjKoUVd&index=3'
        'blablabla'
        ]
        downloader = YouTubeAudioFilesDownloader(wrong_urls,self.TEST_DEST)
        downloader.download_all_files_from_urls()


        target_msgs = [
        f'Could not find {wrong_urls[0]}'
        ]
        self.assertTrue(self.teststdout_contains_all_elements_of_list(target_msgs),f'Actual output is:\n{self.teststdout.getvalue()}')


    def teststdout_contains_all_elements_of_list(self,lst):
        teststdoutstr = self.teststdout
        return all(s in teststdoutstr for s in lst)


if __name__ == '__main__':
    unittest.main()
