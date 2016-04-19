for i in range(5):    # for each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    print(i)          # this line is executed 5 times. First time i equals 0, then 1, ...


primes = [2, 3, 5, 7]   # create new list

for val in primes:
    print(val)


hello_world = "Hello, World!"

for ch in hello_world:    # print each character from hello_world
    print(ch)

length = 10      # initialize length variable
print(len(hello_world) == length)

square = 1

while square <= 10:
    print(square)    # This code is executed 10 times
    square += 1      # This code is executed 10 times

print("Finished")  # This code is executed once

square = 0
number = 1

for number in range(99):
    square = number ** 2
    print(square)
    number += 1

count = 0

while True:  # this condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # exit loop if count >= 5


zoo = ["lion", 'tiger', 'elephant']
while True:                         # this condition cannot possibly be false
    animal = zoo.pop()       # extract one element from the list end
    print(animal)
    if animal is 'elephant':
        break # exit loop
    else:
        continue

