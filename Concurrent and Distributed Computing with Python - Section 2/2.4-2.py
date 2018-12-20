
import threading
import time
import requests

def download_url(url):
    print("Downloading the contents of {} from {}".format(url, threading.current_thread().name))
    requests.get(url)
    print("Download of {} done".format(url))


if __name__ == "__main__":
    threads = []
    test_dict = {
        "Google": "http://www.google.com",
        "Python": "http://www.python.org",
        "Bing": "http://www.bing.com",
        "Yahoo": "http://www.yahoo.com"
    }
    for key in test_dict:
        threads = [threading.Thread(target=download_url, args=(test_dict[key],)) for key in test_dict]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
