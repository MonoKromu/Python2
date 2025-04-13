elements = [1, "abc", 1, 123, 123, "ab", 8, 95, 8, 114, 8]
for i in elements:
    if elements.count(i) == 1:
        print(i, end=", ")
