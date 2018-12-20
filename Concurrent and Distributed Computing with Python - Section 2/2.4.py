
from greenlet import greenlet

def test1():
    print("test1: Started")
    gr2.switch()
    print("test1: Started Again")
    gr2.switch()


def test2():
    print("test2: Started")
    gr1.switch()
    print("test2: Started Again")

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()