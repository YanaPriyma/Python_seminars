# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input("Введите количество элементов: "))
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(-10,10))     
print(*rand_list)

min_number = int(input())
max_number = int(input())

for i in range(len(rand_list)):
    if min_number <= rand_list [i] <= max_number:
        print(i)