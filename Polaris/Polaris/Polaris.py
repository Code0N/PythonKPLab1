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

