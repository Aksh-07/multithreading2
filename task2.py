import concurrent.futures
import queue

q = queue.Queue()

for i in range(1, 101):
    q.put(i)


def print_no(a):
    print(a.get())


with concurrent.futures.ThreadPoolExecutor() as executor:
    while not q.empty():
        for _ in range(4):
            t = executor.submit(print_no, q)

