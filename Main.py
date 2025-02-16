# №1
# line = "danastroka"
# print(line[0])
# print(line[-2])
# print(line[:5])
# print(line[:-2])
# print(line[::2])
# print(line[1::2])
# print(line[::-1])
# print(line[::-2])
# print(len(line))

# №2
# line = "c0o0l$tr1ng"
# mid = (len(line) + 1) // 2
# newline = line[mid:] + line[:mid]
# print(newline)

# №3
# line = list("qwe Heh llo worl h d")
# first = line.index("h")
# line.reverse()
# last = line.index("h")
# print(*line[last+1:-first-1])

# №4
# line = "sdfdfghiigfuidfhhhh"
# if line.count("f") > 0:
#     print(line.find("f"))
# if line.count("f") > 1:
#     print(line.rfind("f"))

# №7
command = input()
length = 1
space = 0
last = ""
s = command[0]
for i in range(len(command)):
    if  command[i] in "<>":
        length+=1
    if i == len(command)-1 or command[i] == "V":
        if command[i-1] == "<":
            space -= length - 1
        print(" " * space, s * length, sep="")
        if command[i-1] == ">":
            space += length - 1
        length = 1