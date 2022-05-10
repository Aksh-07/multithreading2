import concurrent.futures
from threading import get_ident, Condition, BoundedSemaphore
import time
import queue

s = time.time()
q = queue.Queue()
# cv = Condition()
bs = BoundedSemaphore(4)

for i in range(1, 101):
    q.put(i)


def print_no(a):
    id_ = get_ident()
    while not a.empty():
        bs.acquire()
        # cv.acquire()
        # cv.notify_all()
        print(f"Thread_{id_}: {a.get()}")
        bs.release()
        # cv.wait()
        # cv.release()


with concurrent.futures.ThreadPoolExecutor() as executor:
    threads = [executor.submit(print_no, q) for _ in range(4)]


f = time.time()

print(f"Total time: {f-s}")

