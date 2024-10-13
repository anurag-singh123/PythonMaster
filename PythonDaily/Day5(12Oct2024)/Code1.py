# Write a Python decorator that logs the execution time of a function.

import time
import functools

def log_execution_time(func):
    @functools.wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate duration
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result  # Return the result of the original function
    return wrapper

# Example usage
@log_execution_time
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Calling the example function
result = example_function(1000000)