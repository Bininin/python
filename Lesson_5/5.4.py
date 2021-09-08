"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл."""
import codecs
content=[]
text={"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
with codecs.open("text_4.txt", encoding='utf-8') as a:
    for y in a:
        content.append(y.split())
content_out=content
for i in range(len(content_out)):
    for y in range(3):
        if  y!=1 and y!=2 and content_out[i][y] in text:
            content_out[i][y]=text.get(str(content_out[i][y]))
with codecs.open("text_5.4_out.txt", "w",encoding='utf-8') as b:
    for i in range(len(content_out)):
        if i>0:
            b.write(f"\n")
        for y in range(3):
            b.write(f"{content_out[i][y]} ")
