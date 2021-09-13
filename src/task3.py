import inspect
import time
import contextlib
import io
from inspect import signature

class decorator_3:
    """The class decorator creates a task3.txt file that contains the characteristics of the function.
    Also, it ranks the functions by their execution time."""

    def __init__(self, fun):
        self.count = 0
        self.fun = fun

    def __call__(self, *args, **kwargs):
        self.count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            self.fun(*args)
        duration = time.time() - start
        self.elapsed_time = duration


        with open('task3.txt', 'a') as f1:
            f1.write(f'{self.fun.__name__}' + f' call {self.count}' + ' executed in ' + f'{duration}' + ' sec' + '\n')
            f1.write('Name:  ' + f' {self.fun.__name__}'+ '\n')
            f1.write('Type:  ' + f' {type(self.fun)}'+ '\n' )
            sig = signature(self.fun)
            f1.write('Sign:  ' + f' {sig}'+ '\n')
            f1.write('Args:  ' + ' positional ' + f'{args}' '\n\t    key=worded ' + f'{kwargs}'+ '\n')
            doc = f'{self.fun.__doc__}'
            doc = doc.splitlines()[1:-1]
            doc = '\n\t'.join(map(str, doc))
            f1.write('Doc:' + f'{doc}'+ '\n')
            source = inspect.getsource(self.fun)
            source = source.splitlines()
            source = '\n\t\t'.join(map(str, source))
            f1.write('Source: ' + f'{source}'+ '\n')
            output = f.getvalue().splitlines()
            output = '\n\t\t'.join(map(str, output))
            f1.write('Output: ' + f'{output}'+ '\n')

ranking_dic = {}

def ranking(*funs):
    global ranking_list
    for fun in funs:
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            fun()
        duration = time.time() - start
        ranking_dic[fun.__name__] = duration

    ranking_list = sorted(ranking_dic, key=lambda item: item[1])
    print('Function | RANK | TIME ELAPSED')

    count = 0
    for i in ranking_list:
        count +=1
        print(f'{i} \t\t {count} \t  {ranking_dic[i]}')

