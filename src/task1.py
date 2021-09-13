import time
import io
import contextlib


def decorator_1(fun):
    """The following function decorator returns the execution time of functions and its trace (the number of its calls)."""

    count = 0

    def wrapper(*args):
        nonlocal count
        count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f: fun(*args)
        duration = time.time() - start
        print(f'{fun.__name__}' + f' call {count}' + ' executed in ' + f'{duration}' + ' sec')
    return wrapper





