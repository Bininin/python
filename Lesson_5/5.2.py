"""Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке."""
import codecs

with codecs.open("text_5.2.txt", encoding='utf-8') as a:
    content=list(a.readlines())
    stoka=0

    for i in content:
        b=i.count(" ")+1
        stoka+=1
        print(f"В строке {stoka} - {b} слов(а) :",i)

