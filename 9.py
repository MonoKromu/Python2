numbers = [12, 14, 1, 150, 171, 132, 92, 17, 18, 15, 20]
for i, n in enumerate(numbers):
    if n > numbers[i-1] or i == 0:
        print(n, end=", ")
