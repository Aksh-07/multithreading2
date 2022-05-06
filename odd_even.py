from threading import Thread
import time


class EvenNo(Thread):
    def run(self):
        for i in range(1, 101):
            if i % 2 == 0:
                print(f"{i}\n")
            time.sleep(0.1)


class OddNo(Thread):
    def run(self):
        for i in range(1, 101):
            if i % 2 != 0:
                print(f"{i}\n")
            time.sleep(0.1)


odd_no = OddNo()
even_no = EvenNo()

odd_no.start()
even_no.start()



