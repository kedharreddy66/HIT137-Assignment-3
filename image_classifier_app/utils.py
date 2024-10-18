import functools
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(func):
    """Decorator to log the execution of functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing {func.__name__}.")
        return result
    return wrapper

def handle_errors(func):
    """Decorator to handle errors in functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred in {func.__name__}: {e}")
            if hasattr(args[0], 'display_result'):
                args[0].display_result("Error during processing.", 0)
            return None
    return wrapper

