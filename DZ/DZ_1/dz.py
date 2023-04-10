# Найдите сумму цифр трехзначного числа

number = int (input("input number: "))
a = number % 10
b = number // 10
c = b % 10
d = b // 10
print(a + c + d)
