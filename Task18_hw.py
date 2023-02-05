# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i].
#  Последняя строка содержит число X
#  5
# 1 2 3 4 5
# 6
# -> 5

import random
n = int(input("Введите число элементов массива: "))
 
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,100))
print(*rand_list)

x1 = int(input("Задайте число X: "))

f_num = min(rand_list, key=lambda x: abs(x-x1))
print(f' -> {f_num}')

# Вариант2
# f_num = rand_list[0]
# for number in rand_list:
#     if abs(number - x1) < abs(f_num - x1):
#         f_num = number
# print(f' -> {f_num}')