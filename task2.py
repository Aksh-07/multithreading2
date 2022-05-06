import concurrent.futures
import queue

q = queue.Queue()

for i in range(1, 101):
    q.put(i)


def print_no(a):
    while not q.empty():
        print(a.get())


with concurrent.futures.ThreadPoolExecutor() as executor:
    for _ in range(4):
        executor.submit(print_no, q)

