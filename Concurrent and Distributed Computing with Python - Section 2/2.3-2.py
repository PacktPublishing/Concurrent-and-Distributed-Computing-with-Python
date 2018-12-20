__author__ = "Mithun"
from threading import Thread, current_thread
import urllib.request
import sys
import timeit


def download_file(url):
    urllib.request.urlretrieve(url, "7zip{}.zip".format(str(current_thread().name)))


def download_file_using_threads(threads):
    for t in threads:
        t.start()

    for t in threads:
        t.join()


number_of_threads = int(sys.argv[1])

threads = []
for _ in range(number_of_threads):
    threads.append(Thread(target=download_file, args=("http://www.7-zip.org/a/7z1701.msi",)))

print(timeit.timeit("download_file_using_threads(threads)", "from __main__ import download_file_using_threads, threads",
                    number=1))
