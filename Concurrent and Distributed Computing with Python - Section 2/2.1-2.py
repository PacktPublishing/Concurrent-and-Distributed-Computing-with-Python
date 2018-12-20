import urllib3
import threading
urllib3.disable_warnings()

class TestThread:
    def __init__(self, file_name, url):
        self.file_name = file_name
        self.url = url

    def download_url(self):

        print("Downloading the contents of {} into {} from {}".format(self.url, self.file_name, threading.current_thread().name))
        http = urllib3.PoolManager()

        response = http.request(method="GET", url=self.url)
        with open(self.file_name, "wb") as f:
            f.write(response.data)

        print("Download of {} done".format(self.url))


if __name__ == "__main__":
    test_dict = {
        "Google": "http://www.google.com",
        "Python": "http://www.python.org",
        "Bing": "http://www.bing.com",
        "Yahoo": "http://www.yahoo.com"
    }
    for key in test_dict:
        test = TestThread(key, test_dict[key])
        test.download_url()
