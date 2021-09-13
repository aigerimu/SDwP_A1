import inspect
import time
import contextlib
import io
from inspect import signature


def decorator_2(fun):

    """The function decorator returns the characteristics of the function.
    It shows the Name, Type, Sign, Args, Doc, Source and Output."""

    count = 0

    def wrapper(*args, **kwargs):
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

    return wrapper





