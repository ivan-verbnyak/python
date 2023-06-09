# напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * degree(a, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
result = degree(a, b)
print(result)