def hello_world():  # function named my_function
    print("Hello, World!")

for i in range(5):
    hello_world()   # call function defined above 5 times

def fun():
    print('I want to be a function')
    print('I want to be a function')
    print('I want to be a function')

for i in range(3):
    fun()


def foo(x):                 # x is a function parameter
    print("x = " + str(x))

foo(5)   # pass 5 to foo(). Here 5 is an argument passed to function foo.


def square(x):
    print(x ** 2)

square(4)
square(8)
square(15)
square(23)
square(42)

def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 0
    b = initialize variable b
    while a < n:
        result.append(a)
        tmp_var = b
        update variable b
        update variable a
    return result

print(fib(10))

def multiply_by(a, b=2):
    return a * b

print(multiply_by(3, 47))
print(multiply_by(3))    # call function using default value for b parameter


def hello(add parameters for function, set default value for name):
    print("Hello %s! My name is %s" % (subject, name))

hello("PyCharm", "Jane")    # call 'hello' function with "PyCharm as a subject parameter and "Jane" as a name
hello("PyCharm")            # call 'hello' function with "PyCharm as a subject parameter and default value for the name