# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с 
# шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

num = str (input("enter the ticket number: "))
lst = [int(i) for i in str(num)]
a = lst[0] + lst[1] + lst[2]
b = lst[3] + lst[4] + lst[5]
if (a == b):
    print("lucky ticket!")
else: 
    print ("ordinary ticket")