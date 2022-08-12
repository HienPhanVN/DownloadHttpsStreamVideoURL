import os
import string
from urllib.request import urlretrieve
from threading import Thread
import requests
import sys

class DownloadThread():

    def __init__(self, Thread, parent, url, name, fsize):
        """Constructor"""
        Thread.__init__(self)
        self.fsize = fsize
        self.url = url
        self.parent = parent
        self.name = name
        self.temp = ""
        self.run()
        self.reporthook()

    def run(self):
        local_fname = name + ".mp4"
        try:
            urlretrieve(self.url, local_fname, self.reporthook)
        except Exception as e: 
            for x in range(0, 100):
                if(os.path.isfile('./default'+ string(x) +'.mp4')):
                    self.temp = './default'+ string(x+1) +'.mp4'
                    urlretrieve(self.url, './default'+ string(x+1) +'.mp4', self.reporthook)

    def reporthook(self, blocknum, blocksize, totalsize):
        print(blocknum, blocksize, totalsize)
        if blocknum is None or blocksize is None or totalsize is None:
            exit()
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = int((readsofar / totalsize) * 100)
        else: # total size is unknown
            percent = 0
        # Initial call to print 0% progress
        print(percent)
        if(percent == 100):
            os.rename(self.temp , name+'.mp4')
        exit()


class MyPanel():
    def __init__(self, url, name):
        self.url = url
        self.data = []
        self.name = name
        self.download_number = 1
        self.onDownload()

    def onDownload(self):
        """
        Update display with downloading gauges
        """
        try:
            header = requests.head(self.url, allow_redirects=True)
            fsize = int(header.headers["content-length"]) / 1024
            # start thread
            print(self.url)
            DownloadThread(Thread, self.download_number, self.url, self.name, fsize)
        except Exception as e:
            print("Error: ", e)

def main(url_video, name):
    panel = MyPanel(url_video, name)


if __name__ == "__main__":
    url = sys.argv[1]
    name = sys.argv[2]
    main(url, name)