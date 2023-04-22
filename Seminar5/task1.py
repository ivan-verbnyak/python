# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 2

def fib(n):
    if n [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

#n = input('введите N-e число ')
list1 = []
for i in range(1, 10):
    list1.append(fib(i))
print(list1)
