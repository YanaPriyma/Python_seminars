#Задача №1. Общее обсуждение
#За день машина проезжает n километров. Сколько
#дней нужно, чтобы проехать маршрут длиной m
#километров? При решении этой задачи нельзя
#пользоваться условной инструкцией if и циклами.
#Input:
#n = 700
#m = 750
#Output:
#2

n = int(input("Введите количество км. проезжаемых автомобилем за день :"))
m = int(input("Введите длину маршрута в км.: "))

print('Количество дней:', (m//n + (n % m != 0)))