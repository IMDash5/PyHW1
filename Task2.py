from queue import Empty

spisok = []
N = int(input("Введите число: "))
i = 1
while i <= N:
    spisok.append(f"{i}: {3 * i + 1}")
    i = i + 1
print(spisok)
