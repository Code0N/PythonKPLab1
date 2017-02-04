# -*- coding: cp1251 -*-

#Задание №1:
def z1():
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
def z2():
    rangelist = range(int(input('Введите некое число: ')))
    isup = True
    temp = -1
    for i in rangelist:
        if i <= temp:
            rangelist = False
            break
        else:
            temp = i
    print(isup)

#Задание №3
def z3():
    userstr = str(input('Введите номер вашей кредитки, если хотите повысить нам настроение: '))
    print('{} **** **** {}'.format(userstr[0:4], userstr[12:16]))


#z1()
#z2()
#z3()
