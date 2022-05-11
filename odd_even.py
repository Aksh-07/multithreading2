from threading import Thread, get_ident, Event
import time

s = time.time()
event1 = Event()
event2 = Event()


class EvenNo(Thread):
    def run(self):
        for i in range(1, 101):
            event1_set = event1.wait()
            if event1_set:
                if i % 2 == 0:
                    id_ = get_ident()
                    print(f"Thread_{id_}: {i}\n")
                event1.clear()
                event2.set()


class OddNo(Thread):
    def run(self):
        event2.set()
        for i in range(1, 101):
            event2_set = event2.wait()
            if event2_set:
                if i % 2 != 0:
                    id_ = get_ident()
                    print(f"Thread_{id_}: {i}")
                event2.clear()
                event1.set()


odd_no = OddNo()
even_no = EvenNo()

odd_no.start()
even_no.start()

odd_no.join()
even_no.join()

f = time.time()
print(f"Total time: {f - s}")
