a = int(input("Введите натуральное число: "))
b = [7, 5, 3, 3, 2]
print("Рейтинг до: ", b)
b.append(0)
for i in range(len(b)):
    if a > b[i]:
        b.insert((i), a)
        break
    elif a == 0:
        b.append(0)
        break
b.pop(-1)
print("Рейтинг после: ")
print(b)
