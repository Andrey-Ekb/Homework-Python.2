# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по 
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для 
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате 
# отгадать задуманные Петей числа.

print()
x = int(input('Введите первое число до 1000 - '))
y = int(input('Введите второе число до 1000 - '))

if x+y!=x*y:
        print()
        print('заданные переменные не подходят для решения задачи')
        print()
else:
    pr=x+y
    print()
    print(pr,' - число, которое дает Петя')
    print()
    i=j=1
    stop = 0
    while i<1000:
        if stop == 0:
            while j<1000:
                if stop == 0:
                    if i+j==pr and i*j==pr:
                        print('числа Кати x = ',i,' y = ', j)
                        print()
                        stop=1
                    j=j+1   
                else: j=1001    
            j=0    
            i=i+1  
        else: i=1001   

