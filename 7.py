command = input()
length = 1
space = 0
s = command[0]
for n, c in enumerate(command):
    if c in "<>":
        length += 1
    if n == len(command) - 1 or c == "V":
        if command[n - 1] == "<":
            space -= length - 1
        print(" " * space, s * length, sep="")
        if command[n - 1] == ">":
            space += length - 1
        length = 1
