from functools import wraps


def only_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f"Attempting to acquire lock {func_name}")
        func_lock_name = 


