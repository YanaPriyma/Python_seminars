# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих
#   наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
#  элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

import random

n = int(input("Введите число элементов  #1: "))
m = int(input("Введите число элементов  #2: "))

rand_list1=[]
rand_list2=[]
for i in range(n):
    rand_list1.append(random.randint(1,10))
for i in range(m):
    rand_list2.append(random.randint(1,10)) 
print(*rand_list1)       
print(*rand_list2)

result = set(rand_list1).intersection(rand_list2)
res = sorted(result)
print("пересечение -> ", *res)