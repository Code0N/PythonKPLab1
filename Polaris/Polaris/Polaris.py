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

#Задание 4
def z4():
    userstr = (str(input("Введите любую, желательно - осмысленную, строку\n"))).split(' ')
    print('Слова длинее семи символов:\n')
    for i in userstr:
        if len(i) > 7:
            print(userstr.pop(userstr.index(i)))
    print("Слова длиною от 4 до 7 символов\n")
    for i in userstr:
        if 4 <= len(i) <= 7:
            print(userstr.pop(userstr.index(i)))
    print('Остальные слова\n')
    for i in userstr:
        print(i)

def z5():
    userstr = (str(input('Введите свою бесполезную строку:\n'))).split(' ')
    for i in range(len(userstr)):
        if ((userstr[i])[0]).isupper():
            userstr[i] = userstr[i].upper()
    print(' '.join(userstr))

def z6():
    tempstr = [] #Пустота и тлен
    userstr = str(input('Введите ваш бесполезный текст\n')).lower()
    for i in userstr:
        if userstr.count(i) == 1:
            tempstr.append(i)
    print(' '.join(tempstr))

def z7():
    templist = []
    tempstr = ''
    filevar = open('urllist.txt', 'r')
    for i in filevar:
        if i.startswith('www.'):
            tempstr = 'http://' + i
            if  not tempstr.endswith('.com'):
                tempstr = tempstr + '.com'
            templist.append(tempstr)
    for i in templist:
        print(i)

z7()