# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие 
# числа N.

print()
n=int(input('Введите число N - '))
print()

a = 2
i=1
while i<=100 and a<n:
    print('двойка в степени ', i,'равна - ', a)
    i=i+1
    a=a*2
print()