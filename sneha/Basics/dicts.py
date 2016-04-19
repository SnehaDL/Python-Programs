# create new dictionary.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" are keys and numbers are values
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book
del phone_book['John']

print('phone_book')

grocery_list = ["fish", "tomato", 'apples']   # create new list

print("tomato" in grocery_list)    # check that grocery_list contains "tomato" item

grocery_dict = {"fish": 1, "tomato": 6, 'apples': 3}   # create new dictionary

print('fish' in grocery_dict.keys())

name = "John"
age = 17

print(name == "John" or age == 17)    # checks that either name equals to "John" OR age equals to 17


name = "John"
age = 17

print(name == "John" or not age > 17)

name = "John"
age = 17

if name == "John" or age == 17:   # check that name is "John" or age is 17. If so print next 2 lines.
    print("name is John")
    print("John is 17 years old")

tasks = ['task1', 'task2']    # create new list

print(len(tasks))

x = 28

if x < 0:
    print('x < 0')                      # executes only if x < 0
elif x == 0:
    print('x is zero')                 # if it's not true that x < 0, check if x == 0
elif x == 1:
    print('x == 1')                    # if it's not true that x < 0 and x != 0, check if x == 1
else:
    print('non of the above is true')

name = "John"

if name is "John":
    print(True)
else:
    print(False)