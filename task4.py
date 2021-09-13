import inspect
import time
import contextlib
import io
from inspect import signature
from datetime import datetime
import logging


logging.basicConfig(filename="task4.log")

def func_decorator(fun):
    """The function decorator prints the characteristics of the function.
        Its Name, Type, Sign, Args, Doc, Source and Out. Also, it handles errors using try/except and shows the date by
        using timestamp."""
    count = 0

    def wrapper(*args, **kwargs):
        try:
            nonlocal count
            count += 1
            start = time.time()
            with contextlib.redirect_stdout(io.StringIO()) as f: fun(*args)
            duration = time.time() - start
            print(f'{fun.__name__}' + f' call {count}' + ' executed in ' + f'{duration}' + ' sec')
            print('Name:  ' + f' {fun.__name__}')
            print('Type:  ' + f' {type(fun)}')
            sig = signature(fun)
            print('Sign:  ' + f' {sig}')
            print('Args:  ' + ' positional ' + f'{args}' '\n\t    key=worded ' + f'{kwargs}')
            doc = fun.__doc__
            doc = doc.splitlines()[1:-1]
            doc = '\n\t'.join(map(str, doc))
            print('Doc:' + f'{doc}')
            source = inspect.getsource(fun)
            source = source.splitlines()
            source = '\n\t\t'.join(map(str, source))
            print('Source: ' + f'{source}')
            output = f.getvalue().splitlines()
            output = '\n\t\t'.join(map(str, output))
            print('Output: ' + f'{output}')

        except:
            logging.exception(f'timestamp: {datetime.now()}')
            pass

    return wrapper


class class_decorator:
    """The function decorator creates a task4.txt file with function characteristics and used a timestamp to show the
    date. Also, it handles errors using try/except. """

    def __init__(self, fun):
        self.count = 0
        self.fun = fun
        self.elapsed_time = []

    def __call__(self, *args, **kwargs):
        try:
            self.count += 1
            start = time.time()
            with contextlib.redirect_stdout(io.StringIO()) as f:
                self.fun(*args)
            duration = time.time() - start

            with open('task4.txt', 'a') as f1:
                f1.write('{self.fun.__name__}' + f' call {self.count}' + ' executed in ' + f'{duration}' + ' sec' + '\n')
                f1.write('Name:  ' + f' {self.fun.__name__}' + '\n')
                f1.write('Type:  ' + f' {type(self.fun)}' + '\n')
                sig = signature(self.fun)
                f1.write('Sign:  ' + f' {sig}' + '\n')
                f1.write('Args:  ' + ' positional ' + f'{args}' '\n\t    key=worded ' + f'{kwargs}' + '\n')
                doc = f'{self.fun.__doc__}'
                doc = doc.splitlines()[1:-1]
                doc = '\n\t'.join(map(str, doc))
                f1.write('Doc:' + f'{doc}' + '\n')
                source = inspect.getsource(self.fun)
                source = source.splitlines()
                source = '\n\t\t'.join(map(str, source))
                f1.write('Source: ' + f'{source}' + '\n')
                output = f.getvalue().splitlines()
                output = '\n\t\t'.join(map(str, output))
                f1.write('Output: ' + f'{output}' + '\n')
        except:
            logging.exception(f'timestamp: {datetime.now()}')
            pass









