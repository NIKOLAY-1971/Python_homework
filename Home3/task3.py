# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
list = []
list1 = []
for i in range(0, n+1):
        if i == 0:
            list.append(0)
        elif i == 1 or i ==2:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])
for i in range(1,n+1):
    list1.append(-1*list[n+1-i])
print(list1+list) 