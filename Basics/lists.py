#list

squares = [1, 4, 9, 16, 25]   # create new list
print(squares)

print(slice)

animals = ['elephant', 'lion', 'tiger', "giraffe"]  # create new list
print(animals)

animals += ["monkey", 'dog']    # add two items to the list
print(animals)

animals.append("dino")   # add one more item to the list using append() method
print(animals)

animals[4] = 'dinosaur'

print(animals)

animals = ['elephant', 'lion', 'tiger', "giraffe", "monkey", 'dog']   # create new list
print(animals)

animals[1:3] = ['cat']    # replace 2 items -- 'lion' and 'tiger' with one item -- 'cat'
print(animals)

animals[1:3] = []     # remove 2 items -- 'cat' and 'giraffe' from the list
print(animals)

animals = []
print(animals)
