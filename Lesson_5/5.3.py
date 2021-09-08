"""Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников."""
import codecs

pers = {}
sum1 = 0
with codecs.open("text_3.txt", encoding='utf-8') as a:
    for line in a:
        (key, val) = line.split()
        pers[(key)] = val
        if float(val) < 20000:
            print(f"Оклад менее 20000р: {key} {val}р")
        sum1 = sum1 + float(val)
print(f"Cрединй оклад {sum1 / len(pers)}р")
print(pers, "\n", )