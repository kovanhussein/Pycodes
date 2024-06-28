import functools
import logging

# Decorator for logging
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

# Decorator for repeating a function
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@log_decorator
def greet(name):
    print(f"Hello, {name}!")
