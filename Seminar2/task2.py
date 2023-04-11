# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

#number = input('Enter a number: ')
#numPrev = 0
#numCur = 1
#numNext = 0
#fibo = str(numPrev) + ' ' + str(numCur)
#while int(number) >= numNext:
#    numNext = numCur + numPrev
#    fibo = fibo + ' ' + str(numNext)
#    numPrev = numCur
#    numCur = numNext
#fibo = fibo.split(' ')
#if number in fibo:
#    print(fibo.index(number) + 1)
#else:
#    print(-1)

#n = int(input("Введите число: "))
#f_i = 2
#f_1 = 0
#f_2 = 1

while f_2 < n:
    f_1, f_2 = f_2, f_1 + f_2
    f_i += 1

if (f_2 == n): 
    print(f"Номер {f_i}")
else:
    print(f"Номер -1")