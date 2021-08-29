def div(a=int(input("Введите числитель:")), b=int(input("Введите знаменатель: "))):
    try:
        div_ = a / b
    except ZeroDivisionError:
        print("Error. Деление на 0")
        return
    return div_


div_ = div()
print("Результат деления: ", div_)
