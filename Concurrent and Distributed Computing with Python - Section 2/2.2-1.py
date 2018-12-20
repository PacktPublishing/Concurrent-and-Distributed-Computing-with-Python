import urllib3
import time
import threading

urllib3.disable_warnings()
from threading import Thread

class TestThread(Thread):
    def __init__(self, file_name, url):
        Thread.__init__(self, name=file_name)
        self.file_name = file_name
        self.url = url

    def run(self):
        time.sleep(1)

        curr_thread = threading.currentThread()
        print("State of thread {} in run: {}. Is the Thread alive? {} ".format(threading.currentThread().name, repr(curr_thread),
                                                                                  curr_thread.isAlive()))

        print("Downloading the contents of {} into {} from {}".format(self.url, self.file_name, threading.currentThread().name))
        http = urllib3.PoolManager()

        response = http.request(method="GET", url=self.url)
        with open(self.file_name, "wb") as f:
            f.write(response.data)

        print("Download of {} done".format(self.url))


if __name__ == "__main__":
    test_dict = {
        "Python": "http://www.python.org"
    }
    for key in test_dict:
        test = TestThread(key, test_dict[key])
        test.start()