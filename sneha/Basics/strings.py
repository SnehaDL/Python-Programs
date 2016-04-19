hello = "Hello"
world = 'World'

hello_world = hello + world
print(hello_world)      # Note: you should print "Hello World"


hello = "hello"
ten_of_hellos = hello*10
print(ten_of_hellos)

python = "Python"
print("h " + python[3])     # Note: string indexing starts with 0

p_letter = python[0]
print(p_letter)


monty_python = "Monty Python"
monty = monty_python[:5]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[:-2]
print(python)

ice_cream = "ice cream"
print("cream" in ice_cream)    # print boolean result directly

phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
print(len(phrase))

dont_worry = "Don't worry about apostrophes"
print(dont_worry)
print("The name of this ice-cream is \"Sweeet\"")
print('text')


monty_python = "Monty Python"
print(monty_python)

print(monty_python.lower())    # print lower-cased version of the string

print(monty_python.upper())


name = "John"
print("Hello, PyCharm! My name is %s!" % name)     # Note: %s is inside the string, % is after the string
years = 30
print("I'm %s years old" % years)