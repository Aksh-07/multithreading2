from threading import Thread, get_ident, Condition
import time

s = time.time()
cv = Condition()


class EvenNo(Thread):
    def run(self):
        for i in range(1, 101):
            cv.acquire()
            cv.notify_all()
            if i % 2 == 0:
                id_ = get_ident()
                print(f"Thread_{id_}: {i}\n")
                cv.wait()
            cv.release()


class OddNo(Thread):
    def run(self):
        for i in range(1, 101):
            cv.acquire()
            cv.notify_all()
            if i % 2 != 0:
                id_ = get_ident()
                print(f"Thread_{id_}: {i}")
                cv.wait()
            cv.release()


odd_no = OddNo()
even_no = EvenNo()

odd_no.start()
even_no.start()

odd_no.join()
even_no.join()

f = time.time()
print(f"Total time: {f-s}")
