import random
from threading import Thread, Lock

# Shared variable
x = 0

# Lock object for synchronization
lock = Lock()

def Reader():
    print("Reader is reading...")
    lock.acquire()  # Acquire lock for mutual exclusion
    print(f"Value of x: {x}")
    lock.release()  # Release lock
    print()

def Writer():
    global x  # Declare x as global to modify its value
    print("Writer is writing...")
    lock.acquire()  # Acquire lock for mutual exclusion
    x += 1
    print(f"New value of x: {x}")
    lock.release()  # Release lock
    print()

if __name__ == '__main__':
    # Loop to create reader and writer threads
    for _ in range(10):
        random_number = random.randint(0, 100)
        if random_number > 50:
            reader_thread = Thread(target=Reader)
            reader_thread.start()
        else:
            writer_thread = Thread(target=Writer)
            writer_thread.start()

    # Wait for all threads to finish
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()

    print("All items have been produced and consumed.")
