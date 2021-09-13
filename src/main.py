import cmath

#function1
f1 = lambda a,b: a+b

#function2
f2 = lambda n: n**2

#function3
def quad(a,b,c):
    d = b**2 - 4*a*c
    x1 = (-b+cmath.sqrt(d))/2*a
    x2 = (-b-cmath.sqrt(d))/2*a
    return x1,x2

print('Quadratic function is: a = 1, b = 5, c = 6')
x1, x2 = quad(1, 5, 6)
print('x1 is ' f'{x1}', 'x2 is ' f'{x2}')



#function4
def pascal(n):
    cur_row = [1]
    x = [0]
    for i in range(0,n+1):
        for el in cur_row:
            print(el, end=" ")
        print()
        cur_row = [left + right for left, right in zip(cur_row+x, x+cur_row)]

print('n for Pascal function is 6')
pascal(6)


#task1

def task1():
    import random
    from task1 import decorator_1

    @decorator_1
    def func():
        print("I am ready to Start")
        result = 0
        n = random.randint(10, 751)
        for i in range(n):
            result += (i ** 2)


    @decorator_1
    def funx():
        print("I am ready to do serious stuff")
        max_val = float('-inf')
        n = random.randint(10, 751)
        res = [pow(i, 2) for i in range(n)]
        for i in res:
            if i > max_val:
                max_val = i


    if __name__ == "__main__":
        func()
        funx()
        func()
        funx()
        func()

task1()

#task2
def task2():
    from task2 import decorator_2

    @decorator_2
    def funh(bar1, bar2=""):
        """
        This function does something useful
        :param bar1: description
        :param bar2: description
        """
        print("some\nmultiline\noutput")


    if __name__ == "__main__":
        funh(None, bar2="")

task2()

#task3
def task3():
    from task3 import decorator_3
    import random

    @decorator_3
    def func():
        print("I am ready to Start")
        result = 0
        n = random.randint(10, 751)
        for i in range(n):
            result += (i ** 2)

    @decorator_3
    def funx():
        print("I am ready to do serious stuff")
        max_val = float('-inf')
        n = random.randint(10, 751)
        res = [pow(i, 2) for i in range(n)]
        for i in res:
            if i > max_val:
                max_val = i

    @decorator_3
    def funh(bar1, bar2=""):
        """
        This function does something useful
        :param bar1: description
        :param bar2: description
        """
        print("some\nmultiline\noutput")

    if __name__ == "__main__":
        func()
        funx()
        func()
        funx()
        func()
        funh(None, bar2="")

    from task3 import ranking
    import time
    def f1():
        time.sleep(random.uniform(0,1))

    def f2():
        time.sleep(random.uniform(0,1))

    def f3():
        time.sleep(random.uniform(0,1))

    def f4():
        time.sleep(random.uniform(0,1))

    ranking(f1, f2, f3, f4)

task3()

#task4
def task4():
    from task4 import func_decorator

    @func_decorator
    def f1():
        print('Hello')

    f1()

    from task4 import class_decorator

    @class_decorator
    def f2():
        print('Hello, Aigerim')

    f2()

task4()

