from threading import Event, Thread
import time
import queue

s = time.time()
q = queue.Queue()
event1 = Event()
event2 = Event()
event3 = Event()
event4 = Event()

for i in range(1, 101):
    q.put(i)


class PrintNo1(Thread):
    def __init__(self, a, name):
        Thread.__init__(self)
        self.queue = a
        self.name = name

    def run(self):
        event1.set()
        while not self.queue.empty():
            event1_set = event1.wait()
            if event1_set:
                v = self.queue.get()
                print(f"Thread_{self.name}: {v}")
                event1.clear()
                event2.set()
                if v == 97:
                    break
        print(f"Thread_{self.name} finished")


class PrintNo2(Thread):
    def __init__(self, a, name):
        Thread.__init__(self)
        self.queue = a
        self.name = name

    def run(self):
        while not self.queue.empty():
            event2_set = event2.wait()
            if event2_set:
                v = self.queue.get()
                print(f"Thread_{self.name}: {v}")
                event2.clear()
                event3.set()
                if v == 98:
                    break
        print(f"Thread_{self.name} finished")


class PrintNo3(Thread):
    def __init__(self, a, name):
        Thread.__init__(self)
        self.queue = a
        self.name = name

    def run(self):
        while not self.queue.empty():
            event3_set = event3.wait()
            if event3_set:
                v = self.queue.get()
                print(f"Thread_{self.name}: {v}")
                event3.clear()
                event4.set()
                if v == 99:
                    break
        print(f"Thread_{self.name} finished")


class PrintNo4(Thread):
    def __init__(self, a, name):
        Thread.__init__(self)
        self.queue = a
        self.name = name

    def run(self):
        while not self.queue.empty():
            event4_set = event4.wait()
            if event4_set:
                v = self.queue.get()
                print(f"Thread_{self.name}: {v}")
            event4.clear()
            event1.set()
        print(f"Thread_{self.name} finished")


t1 = PrintNo1(q, "1st")
t2 = PrintNo2(q, "2nd")
t3 = PrintNo3(q, "3rd")
t4 = PrintNo4(q, "4th")

t_list = [t1, t2, t3, t4]

for t in t_list:
    t.start()


for t in t_list:
    t.join()


f = time.time()

print(f"Total time: {f - s}")
