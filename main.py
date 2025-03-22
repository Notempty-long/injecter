import time
import requests
import sys
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Example usage:
@timer
def main():
    func = requests.get(sys.argv[-1]).content
    func()