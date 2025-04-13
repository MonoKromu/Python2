numbers = [10, -10, -20, 30, 40]
for i, n in enumerate(numbers):
    if (n < 0) == (numbers[i-1] < 0) and i != 0:
        print(numbers[i-1], n)
        break
