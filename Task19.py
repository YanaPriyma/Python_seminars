# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]
k = 3

# new_numbers = []
# for i in range(k, len(numbers)):
#     new_numbers.append(numbers[i])
#     for j in range(0, k):
#         new_numbers.append(numbers[j])
# print(new_numbers)

print(numbers[-k+1:] + numbers[:k])