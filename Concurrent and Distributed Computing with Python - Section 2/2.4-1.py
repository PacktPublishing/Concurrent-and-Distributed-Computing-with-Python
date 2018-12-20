import gevent
import time

import threading
def synchronous_task(pid):
    """
    Some non-deterministic task
    """
    print("Starting {} in thread name {}".format(pid, threading.current_thread().name))
    time.sleep(0.2)
    print('Task %s done' % pid)

def asynchronous_task(pid):
    """
    Some non-deterministic task
    """
    print("Starting {} in thread name {}".format(pid, threading.current_thread().name))
    gevent.sleep(0.2)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1, 5):
        synchronous_task(i)

def asynchronous():
    threads = [gevent.spawn(asynchronous_task, i) for i in range(5)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
