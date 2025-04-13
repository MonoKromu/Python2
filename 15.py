messages = []
clients = []
last = "Кто последний?"
first = "Я только спросить!"
Next = "Следующий!"
N = int(input())
for _ in range(N):
    messages.append(input())
for text in messages:
    if last in text:
        clients.append(str(text.split("- ")[1].split(".")[0]))
    elif first in text:
        clients.insert(0, str(text.split("- ")[1].split(".")[0]))
    elif Next in text:
        if len(clients) > 0:
            print(f"Заходит {clients.pop(0)}!")
        else:
            print("В очереди никого нет.")

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
