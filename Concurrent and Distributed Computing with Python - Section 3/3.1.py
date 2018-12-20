from multiprocessing import Process
import time

num_processes = 2
processes = []
number = 10000
def calculate_factorial(number):
    factorial = 1

    for n in range(1, number + 1):
        factorial *= n

    return factorial

if __name__ == "__main__":
    start = time.time()
    for i in range(num_processes):
        process_name = "Process {}".format(i)
        p = Process(target=calculate_factorial, args=(number,), name=process_name)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    end= time.time()
    print("With {} Processes, we took {} seconds to calculate Factorial of {}".format(num_processes, end-start, number))
