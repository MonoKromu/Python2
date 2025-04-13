word = input()
even = not bool(len(word) % 2)
space_before = len(word) // 2 - (1 if even else 0)
space_between = 1 + even
print(" " * space_before, word[space_before], (word[-space_before - 1] if even else ""), sep="")
for i in range(space_before)[::-1]:
    print(" " * i, word[i], " " * space_between, (word[-i - 1]), sep="")
    space_between += 2
