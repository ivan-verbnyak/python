import random

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

a = []
n = int(input('введите длину списка: '))
for i in range(n):
    a.append(random.randint(1,100))
    # a.append(i)
print(a)
x = int(input('введите число для поиска: '))
miin = abs(x - a[0])
nearest = a[0]
for i in range(1, n):
    diff = abs(x - a[i]) 
    if diff < miin: 
        miin = diff 
        nearest = a[i] 
print(nearest) 
