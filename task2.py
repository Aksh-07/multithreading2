import concurrent.futures
from threading import get_ident, Event, BoundedSemaphore
import time
import queue

s = time.time()
q = queue.Queue()
bs = BoundedSemaphore(4)

for i in range(1, 101):
    q.put(i)


def print_no(a, es):
    id_ = get_ident()
    while not a.empty():
        # bs.acquire()
        for ix, e in enumerate(es):
            e_set = e.wait()
            if e_set:
                print(f"Thread_{id_}: {a.get()}")
                e.clear()
                if ix != len(es):
                    es[ix+1].set()
                else:
                    es[0].set()

        # bs.release()


events = [Event() for _ in range(4)]
events[0].set()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # threads = [executor.submit(print_no, q, event) for event in events]
    # for event in events:

    executor.submit(print_no, q, events)

f = time.time()

print(f"Total time: {f - s}")
