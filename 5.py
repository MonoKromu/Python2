word = input()
while True:
    new_word = input()
    if new_word[0] == word[-1]:
        word = new_word
    else:
        print(new_word)
        break
