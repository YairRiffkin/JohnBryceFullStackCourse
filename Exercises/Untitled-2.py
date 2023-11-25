from time import sleep
from datetime import datetime, timedelta
import random


def task(name, seconds):
    start_time = datetime.now()
    while start_time + timedelta(seconds=seconds) > datetime.now():
        print(f"Task {name} is working...")
        sleep(0.3)  # Simulate work being done
        yield None  # Yield control, indicating the task is not done
    result = random.randint(10000, 20000)
    print(f"Task {name} completed with result: {result}")
    yield result  # Yield the final result

def event_loop(tasks):
    results = {}
    while tasks:
        for task in tasks.copy():
            try:
                result = next(task)
                if result is not None:
                    tasks.remove(task)
                    results[task] = result
            except StopIteration:
                tasks.remove(task)
    return results

# Creating tasks
task1 = task("A", 2)
task2 = task("B", 3)

# Starting the event loop with the tasks
results = event_loop([task1, task2])

# Display the results
print("All tasks completed. Results:", results)