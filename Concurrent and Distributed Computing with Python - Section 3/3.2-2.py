from multiprocessing import Process, Value

def increment(num):
    for _ in range(1000):
        num.value = num.value + 1


def decrement(num):
    for _ in range(1000):
        num.value = num.value - 1


if __name__ == "__main__":
    num = Value('i', 0)
    print(num.value)

    p1 = Process(target=increment, args=(num,))
    p2 = Process(target=decrement, args=(num,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(num.value)
