import functools
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    """
    Decorator that logs the call and result of a function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: A wrapper function that logs the call and result of the original function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that logs before and after calling the original function.

        Args:
            *args: Positional arguments to pass to the original function.
            **kwargs: Keyword arguments to pass to the original function.

        Returns:
            The result of the original function call.
        """
        logging.info(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

def repeat(num_times):
    """
    Decorator that repeats the execution of a function a specified number of times.

    Args:
        num_times (int): The number of times to repeat the function call.

    Returns:
        function: A decorator that wraps the original function and repeats its execution.
    """
    def decorator_repeat(func):
        """
        Inner decorator function that wraps the original function.

        Args:
            func (function): The function to be decorated.

        Returns:
            function: A wrapper function that repeats the execution of the original function.
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that executes the original function multiple times.

            Args:
                *args: Positional arguments to pass to the original function.
                **kwargs: Keyword arguments to pass to the original function.

            Returns:
                None
            """
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@log_decorator
def greet(name):
    """
    Prints a greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None
    """
    print(f"Hello, {name}!")

# Example usage:
# This will log the call and result of the greet function.
greet("Alice")
