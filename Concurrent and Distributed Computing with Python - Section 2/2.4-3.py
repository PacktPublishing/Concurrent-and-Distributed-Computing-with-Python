import gevent

import gevent.monkey
gevent.monkey.patch_socket()

import requests
import threading


def download_url(url):
    print("Downloading the contents of {} from {}".format(url, threading.current_thread().name))
    requests.get(url)
    print("Download of {} done".format(url))


if __name__ == "__main__":
    test_dict = {
        "Google": "http://www.google.com",
        "Python": "http://www.python.org",
        "Bing": "http://www.bing.com",
        "Yahoo": "http://www.yahoo.com"
    }

    threads = [gevent.spawn(download_url, test_dict[key]) for key in test_dict]

    print("No. Of active threads = {}".format(threading.active_count()))

    gevent.joinall(threads)
