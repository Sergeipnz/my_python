print('Задача 1')
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(long_phrase) > len(short_phrase):
    print("True")
else: print("False")

#Определите какая из двух букв встречается в нем чаще - 'а' или 'и'.
print('Задача 2')
text = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'

schet_a = 0
schet_i = 0
for i in text:
    if i == "а":
        schet_a += 1
    elif i == "и":
        schet_i += 1
print('Кол-во "а" - ', schet_a)
print('Кол-во "и" - ', schet_i)

print('Задача 2 2-ой способ')
print(text.count('а'))
print(text.count('и'))

#3. Дано значение объема файла в байтах. Напишите перевод этого значения в мегабайты в формате: 'Объем файла равен 213.68Mb'
print('Задача 3')
znach = input('Введите значение в байтах - ')
print('Объем файла равен ', int(znach)/1024/1024 ,'Mb')

#Выведите на экран значение синуса 30 градусов с помощью метода math.sin.
print('Задача 4')
import math
print('SIN(30) = ', math.sin(math.radians(30)))

