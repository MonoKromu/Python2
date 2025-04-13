numbers = input().split()
words = input().lower().split()
print(words[int(numbers[0])-1].title(), end=" ")
for i in numbers[1:]:
    print(words[int(i) - 1], end=" ")
