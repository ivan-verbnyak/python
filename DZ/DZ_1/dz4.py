# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("input n: "))
m = int(input("input m: "))
k = int(input("input k: "))
if n > m and k < m:
    print("No")
elif n < m and k < n:
    print("No")
elif (n * m) <= k :
    print("No")
elif k % n == 0 or k % m == 0:
    print ("Yes")
else:
    print("No")