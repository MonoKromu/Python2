cords = [(4, 1), (1, 2), (5, 3), (8, 4), (2, 5), (7, 6), (3, 7), (6, 8)]
intersection = False
for n, queen in enumerate(cords):
    for target in cords[n+1:]:
        diff = (abs(queen[0] - target[0]), abs(queen[1] - target[1]))
        if queen[0] == target[0] or queen[1] == target[1] or diff[0] == diff[1]:
            intersection = True
            break
if intersection:
    print("YES")
else:
    print("NO")
