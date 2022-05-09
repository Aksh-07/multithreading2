import concurrent.futures
from threading import Lock, get_ident, Thread
import queue
import time

s = time.time()
q = queue.Queue()

for i in range(1, 101):
    q.put(i)


def print_no(a, lock, t_id):
    with lock:
        while not q.empty():
            print(f"Thread_{t_id}: {a.get()}")


lock_ = Lock()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for _ in range(4):
        id_ = get_ident()
        executor.submit(print_no, a=q, lock=lock_, t_id=id_)

# threads = [Thread(target=print_no, args=(q, lock_, get_ident())) for _ in range(4)]
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#

f = time.time()
print(f"Total time: {f-s}")
