a = input("Введите слова через пробел: ").split()
for i in range(len(a)):
    print((i + 1), ") ", str(a[i])[:10])
