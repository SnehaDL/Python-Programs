f = open("input.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                             # Note: if you want to write to the file use "w" as second argument
print(f.readlines())
f.close()                   # It's important to close the file to free up any system resources.

f1 = open("input1.txt", "r")
print(f1.readline())
zoo = ['lion', "elephant", 'monkey']
if __name__ == "main":
    f = open("output.txt")

    for i in zoo:
        f.write(i)

    f.close()