# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

numbers = [1, 1, 2, 0, -1, 3, 4, 4]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)
# print(len(unique))

print(len(set(numbers)))

# list1 = list(map(int, input('Введите числа: ').split(' ')))
# print(list1)