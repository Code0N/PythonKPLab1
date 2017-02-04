# -*- coding: cp1251 -*-

#Задание №1:
try:
    userinput = float(input('Введите своё бесполезное число в вещественном виде: '))
    if userinput < 0:
        raise ValueError('Число отрицательное')
    print('{} руб. {} коп.'.format(str(userinput).split('.')[0], str(userinput).split('.')[1])) #Костыль-мастер
except ValueError as ex:
    print('An error occured: ValueError')
except:
    print('Ваш ввод слишком криворукий для этого скрипта')

#Задание №2
userinput = int(input('Введите некое число: '))
rangelist = range(userinput)
isup = True
temp = -1
for i in rangelist:
    if i <= temp:
        rangelist = False
        break
    else:
        temp = i
print(isup)

