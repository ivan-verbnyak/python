# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list = [1, 3, 3, 4]
min = list[0]
max = list[0]
for i in list:
    if i < min:
        min = i
    elif i >max:
        max = i
for j in range(len(list)):
    if list[j] == max:
        list[j] = min

print(list)
