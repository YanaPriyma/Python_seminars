# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
#  в массиве A[0..N-1]. Пользователь в первой строке вводит натуральное число 
#  N – количество элементов в массиве. В последующих строках записаны N целых чисел A[i].
#   Последняя строка содержит число X
  
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
n = int(input("Введите число элементов массива: "))
 
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,4))
print(rand_list)

x = int(input("Введите элемент для подсчета: "))

print(rand_list.count(x))

# counter = 0
# for c in rand_list:
#     if c == x:
#         counter += 1
# print(counter)
