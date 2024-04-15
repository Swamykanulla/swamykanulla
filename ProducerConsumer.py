from threading import Thread, Semaphore

# Shared buffer and its size
buffer = []
CAPACITY = 10

# Semaphores for synchronization
mutex = Semaphore(1)  # Mutual exclusion for buffer access
full = Semaphore(0)   # Number of items in the buffer
empty = Semaphore(CAPACITY)  # Number of empty slots in the buffer

def producer():
  for i in range(10):
    item = produce_item(i)  # Simulate producing an item

    empty.acquire()  # Wait for an empty slot
    mutex.acquire()  # Acquire lock for mutual exclusion

    buffer.append(item)  # Add item to the buffer
    print(f"Producer produced item: {item}")

    mutex.release()  # Release lock
    full.release()  # Signal a full slot

def consumer():
  for i in range(10):
    full.acquire()  # Wait for a full slot
    mutex.acquire()  # Acquire lock for mutual exclusion

    item = buffer.pop()  # Remove item from the buffer
    print(f"Consumer consumed item: {item}")

    mutex.release()  # Release lock
    empty.release()  # Signal an empty slot

def produce_item(i):
  # Simulate producing an item
  return f"Item {i}"

# Create producer and consumer threads
producer_thread = Thread(target=producer)
consumer_thread = Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Wait for threads to finish
producer_thread.join()
consumer_thread.join()

print("All items produced and consumed.")
