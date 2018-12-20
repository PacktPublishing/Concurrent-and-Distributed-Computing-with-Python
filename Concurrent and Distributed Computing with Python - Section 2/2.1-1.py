from threading import Thread
import threading

def run_in_a_thread():
    print("Name of the current thread is {}".format(threading.current_thread().name))

new_thread = Thread(target=run_in_a_thread)
new_thread.start()

run_in_a_thread()