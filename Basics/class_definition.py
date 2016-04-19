class MyClass:
    variable = 10

    def foo(self):   # we'll explain self parameter later in task 4
        print("Hello from function foo")

my_object = MyClass()  # variable "my_object" holds an object of the class "MyClass" that contains the variable and the "foo" function

class MyClass:
    variable1 = 1
    variable2 = 2

    def foo(self):     # we'll explain self parameter later in task 4
        print("Hello from function foo")

my_object = MyClass()
my_object1 = MyClass()

my_object.variable2 = 3     # change value stored in variable2 in my_object

print(my_object.variable2)
print(my_object1.variable2)

my_object.foo()   # call method foo() of object my_object

print(my_object.variable1)


class Car:
    color = ""
    def description(self):
        description_string = "This is a %s car." % self.color    # we'll explain self parameter later in task 4
        return description_string

car1 = Car()
car2 = Car()

car1.color = "blue"
car2.color = "red"

print(car1.description())
print(car2.description())


class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):


    def get_current(self):
        return self.current


class Square:

    def __init__(self):    # special method __init__
        self.sides = 4

square = Square()
print(square.sides)

class Car:
    def __init__(color):
        self.color = color

car = Car("blue")    # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)