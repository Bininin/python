"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""

with open("text_5.5.txt", "w", encoding='utf-8') as a:
    b = (input("Введите числа через пробел: "))
    a.write(f"{b} \n")
with open("text_5.5.txt", "r", encoding='utf-8') as c:
    d = c.readline().split()
    sum1 = 0
    for i in d:
        sum1 = sum1 + float(i)
print(f"Сумма цифр{d}: {round(sum1, 2)}")
