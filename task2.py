import concurrent.futures
from threading import get_ident, Event, BoundedSemaphore
import time
import queue

s = time.time()
q = queue.Queue()
events_q = queue.Queue()
bs = BoundedSemaphore(4)

for i in range(1, 101):
    q.put(i)


def print_no(a, e, eq):
    while not a.empty():
        bs.acquire()
        id_ = get_ident()
        e1 = eq.get()
        e1.set()
        e_set = e.wait()
        if e_set:
            print(f"Thread_{id_}: {a.get()}")
            e1.clear()
            eq.put(e1)
        bs.release()


event1 = Event()
event2 = Event()
event3 = Event()
event4 = Event()

event_list = [event1, event2, event3, event4]
for event in event_list:
    events_q.put(event)


with concurrent.futures.ThreadPoolExecutor() as executor:
    threads = [executor.submit(print_no, q, event, events_q) for event in event_list]


f = time.time()

print(f"Total time: {f - s}")
