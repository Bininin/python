"""Создайте собственный класс-исключение, обрабатывающий ситуацию
деления на ноль. Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой."""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data1 = input("Введите делимое: ")
inp_data2 = input("Введите частное: ")


try:
    inp_data1 = int(inp_data1)
    inp_data2 = int(inp_data2)
    if inp_data2 == 0:
        raise OwnError("Деление на ноль!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {(inp_data1/inp_data2):0.2f}")