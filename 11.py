elements = ["abc", 123, True, False, None, 228, "hello"]
for i in range(0, len(elements)-1, 2):
    elements[i], elements[i+1] = elements[i+1], elements[i]
print(elements)
