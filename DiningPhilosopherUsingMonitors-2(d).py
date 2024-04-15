import threading
import time
import random

class Monitor:
    def __init__(self, num_philosophers):
        self.num_philosophers = num_philosophers
        self.locks = [threading.Condition() for _ in range(num_philosophers)]
        self.states = ['thinking'] * num_philosophers
        self.available = [True] * num_philosophers

    def pick_up_forks(self, philosopher_id):
        with self.locks[philosopher_id]:
            self.available[philosopher_id] = False
            self.test(philosopher_id)
            while not self.available[philosopher_id]:
                self.locks[philosopher_id].wait()

    def put_down_forks(self, philosopher_id):
        with self.locks[philosopher_id]:
            self.available[philosopher_id] = True
            self.test((philosopher_id + 1) % self.num_philosophers)
            self.test((philosopher_id - 1) % self.num_philosophers)

    def test(self, philosopher_id):
        left = (philosopher_id - 1) % self.num_philosophers
        right = (philosopher_id + 1) % self.num_philosophers

        if self.states[philosopher_id] == 'hungry' and \
           self.states[left] != 'eating' and \
           self.states[right] != 'eating':
            self.states[philosopher_id] = 'eating'
            self.available[philosopher_id] = True
            self.locks[philosopher_id].notify()

def philosopher(monitor, philosopher_id):
    while True:
        print(f'Philosopher {philosopher_id} is thinking.')
        time.sleep(random.uniform(1, 3))
        print(f'Philosopher {philosopher_id} is hungry.')
        monitor.states[philosopher_id] = 'hungry'
        monitor.pick_up_forks(philosopher_id)
        print(f'Philosopher {philosopher_id} is eating.')
        time.sleep(random.uniform(1, 3))
        monitor.put_down_forks(philosopher_id)

if __name__ == "__main__":
    num_philosophers = 5
    monitor = Monitor(num_philosophers)
    philosophers = [threading.Thread(target=philosopher, args=(monitor, i)) for i in range(num_philosophers)]

    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()
