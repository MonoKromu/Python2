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

# №5
# word = input()
# while True:
#     new_word = input()
#     if new_word[0] == word[-1]:
#         word = new_word
#     else:
#         print(new_word)
#         break

# №6
# for n, c in enumerate(input()):
#     print(c * (n + 1), end="")

# №7
# command = input()
# length = 1
# space = 0
# s = command[0]
# for n, c in enumerate(command):
#     if c in "<>":
#         length += 1
#     if n == len(command) - 1 or c == "V":
#         if command[n - 1] == "<":
#             space -= length - 1
#         print(" " * space, s * length, sep="")
#         if command[n - 1] == ">":
#             space += length - 1
#         length = 1

# №8
# word = input()
# even = not bool(len(word) % 2)
# space_before = len(word) // 2 - (1 if even else 0)
# space_between = 1 + even
# print(" " * space_before, word[space_before], (word[-space_before-1] if even else ""), sep="")
# for i in range(space_before)[::-1]:
#     print(" " * i, word[i], " " * space_between, (word[-i-1]), sep="")
#     space_between+=2

# №9
# numbers = [12, 14, 1, 150, 171, 132, 92, 17, 18, 15, 20]
# for i, n in enumerate(numbers):
#     if n > numbers[i-1] or i == 0:
#         print(n, end=", ")

# №10
# numbers = [10, -10, -20, 30, 40]
# for i, n in enumerate(numbers):
#     if (n < 0) == (numbers[i-1] < 0) and i != 0:
#         print(numbers[i-1], n)
#         break

# №11
# elements = ["abc", 123, True, False, None, 228, "hello"]
# for i in range(0, len(elements)-1, 2):
#     elements[i], elements[i+1] = elements[i+1], elements[i]
# print(elements)

# №12
# elements = [1, "abc", 1, 123, 123, "ab", 8, 95, 8, 114, 8]
# for i in elements:
#     if elements.count(i) == 1:
#         print(i, end=", ")

# №13
# numbers = input().split()
# words = input().lower().split()
# print(words[int(numbers[0])-1].title(), end=" ")
# for i in numbers[1:]:
#     print(words[int(i) - 1], end=" ")

# №14
# cords = [(4, 1), (1, 2), (5, 3), (8, 4), (2, 5), (7, 6), (3, 7), (6, 8)]
# intersection = False
# for n, queen in enumerate(cords):
#     for target in cords[n+1:]:
#         diff = (abs(queen[0] - target[0]), abs(queen[1] - target[1]))
#         if queen[0] == target[0] or queen[1] == target[1] or diff[0] == diff[1]:
#             intersection = True
#             break
# if intersection:
#     print("YES")
# else:
#     print("NO")

# №15
# messages = []
# clients = []
# last = "Кто последний?"
# first = "Я только спросить!"
# Next = "Следующий!"
# N = int(input())
# for _ in range(N):
#     messages.append(input())
# for text in messages:
#     if last in text:
#         clients.append(str(text.split("- ")[1].split(".")[0]))
#     elif first in text:
#         clients.insert(0, str(text.split("- ")[1].split(".")[0]))
#     elif Next in text:
#         if len(clients) > 0:
#             print(f"Заходит {clients.pop(0)}!")
#         else:
#             print("В очереди никого нет.")
"""
7
Кто последний? Я - Кузнецов.
Кто последний? Я - Поливанов.
Следующий!
Я только спросить! Я - Иванова.
Следующий!
Следующий!
Следующий!
"""