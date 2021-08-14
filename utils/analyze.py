from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken for Packing the knapsack (Execution): {(end - start)}s")

# capture the start and end of an event then give the total time taken for execution