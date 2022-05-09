from threading import Thread, get_ident
import time


class EvenNo(Thread):
    def run(self):
        for i in range(1, 101):
            if i % 2 == 0:
                id_ = get_ident()
                print(f"Thread_{id_}: {i}\n")
            time.sleep(0.1)


class OddNo(Thread):
    def run(self):
        for i in range(1, 101):
            if i % 2 != 0:
                id_ = get_ident()
                print(f"Thread_{id_}: {i}\n")
            time.sleep(0.1)


odd_no = OddNo()
even_no = EvenNo()

odd_no.start()
even_no.start()

odd_no.join()
even_no.join()

