# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Задайте размерность списка: '))
list = [float(input(f'Введите {i} элемент списка: ')) for i in range(n)]
xmin = list[0] - int(list[0])
xmax = list[0] - int(list[0])
for i in range(n):
    if xmin > list[i] - int(list[i]):
        xmin = list[i] - int(list[i])
    if xmax < list[i] - int(list[i]):
        xmax = list[i] - int(list[i])
print('Разница между максимальным и минимальным значением дробной части составит:', xmax - xmin)
