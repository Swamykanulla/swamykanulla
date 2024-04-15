import threading
import time
import random

class Semaphore:
    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def acquire(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1

    def release(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, semaphore):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.semaphore = semaphore

    def run(self):
        for i in range(3):  # Each philosopher will eat three times
            self.think()
            self.dine()

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(random.uniform(1, 3))

    def dine(self):
        self.semaphore.acquire()
        self.left_fork.acquire()
        print(f"Philosopher {self.index} has acquired left fork.")
        time.sleep(random.uniform(1, 3))
        self.right_fork.acquire()
        print(f"Philosopher {self.index} has acquired right fork.")
        print(f"Philosopher {self.index} is eating.")
        time.sleep(random.uniform(1, 3))
        self.right_fork.release()
        print(f"Philosopher {self.index} has released right fork.")
        self.left_fork.release()
        print(f"Philosopher {self.index} has released left fork.")
        self.semaphore.release()

def main():
    num_philosophers = 5
    forks = [threading.Semaphore(1) for _ in range(num_philosophers)]
    semaphore = Semaphore(num_philosophers - 1)
    philosophers = [Philosopher(i, forks[i], forks[(i + 1) % num_philosophers], semaphore) for i in range(num_philosophers)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    main()
