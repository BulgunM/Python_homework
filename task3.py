"""
Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""

number = int(input('Введите номер билета: '))

if (number // 100000) + (number // 10000 % 10) + (number // 1000 % 10) == (number // 100 % 10) + (number // 10 % 10) + (number % 10):
    print('Yes')

else:
    print('No')
