# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#  Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
#  собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
#  собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной 
#  во входном файле грядки.
# 4 -> 1 2 3 4
# 9

import random

n = int(input("Введите количество кустов: "))
rand_list=[]
for i in range(n):
    rand_list.append(random.randint(1,10))     
print(*rand_list)

sum = 0
rnd_range= rand_list + rand_list[:2]

for i in range(n):
       sum = max(sum, rnd_range[i]+rnd_range[i+1]+rnd_range[i+2])
print(f"Максимальное число ягод {sum}")

