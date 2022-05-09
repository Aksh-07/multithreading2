import concurrent.futures
from threading import get_ident, Lock
import time
import queue

s = time.time()
q = queue.Queue()

for i in range(1, 101):
    q.put(i)


def print_no(a, lock):
    id_ = get_ident()
    while not a.empty():
        lock.acquire()
        print(f"Thread_{id_}: {a.get()}")
        lock.release()
        time.sleep(0.01)


lock_ = Lock()

with concurrent.futures.ThreadPoolExecutor() as executor:
    threads = [executor.submit(print_no, q, lock=lock_) for _ in range(4)]


f = time.time()

print(f"Total time: {f-s}")

