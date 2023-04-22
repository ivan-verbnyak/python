# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_it_simple_or_not(number):
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return 'No'
    return 'Yes'
N = int(input('input number: '))
print(is_it_simple_or_not(N))