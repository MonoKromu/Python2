line = "c0o0l$tr1ng"
mid = (len(line) + 1) // 2
newline = line[mid:] + line[:mid]
print(newline)
