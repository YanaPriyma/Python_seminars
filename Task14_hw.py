# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число N: "))
numbers = []

for i in range(n):
    x = 2**i
    if x <= n:
        numbers.append(x)

print(f"{n} -> {numbers}")