# -*- coding: cp1251 -*-

#������� �1:
def z1():
    try:
        userinput = float(input('������� ��� ����������� ����� � ������������ ����: '))
        if userinput < 0:
            raise ValueError('����� �������������')
        print('{} ���. {} ���.'.format(str(userinput).split('.')[0], str(userinput).split('.')[1])) #�������-������
    except ValueError:
        print('An error occured: ValueError')
    except:
        print('��� ���� ������� ���������� ��� ����� �������')

#������� �2
def z2(): # �� ����� ����, �� ���� ��������
    rangelist = range(int(input('������� ����� �����: ')))
    isup = True
    temp = -1
    for i in rangelist:
        if i <= temp:
            rangelist = False
            break
        else:
            temp = i
    print(isup)

#������� �3
def z3():
    userstr = str(input('������� ����� ����� ��������, ���� ������ �������� ��� ����������: '))
    if not userstr.isdigit():
        print('����� ��������� ����� ����� �������� ������ �� ����')
    elif len(userstr) < 16 or len(userstr) > 16:
        print('������ ����� ������ �����: ��������� ������ 16 ����')
    else:
        print('{} **** **** {}'.format(userstr[0:4], userstr[12:16]))

#������� 4
def z4():
    userstr = (str(input("������� �����, ���������� - �����������, ������\n"))).split(' ')
    print('����� ������ ���� ��������:\n')
    for i in userstr:
        if len(i) > 7:
            print(userstr.pop(userstr.index(i)))
    print("����� ������ �� 4 �� 7 ��������\n")
    for i in userstr:
        if 4 <= len(i) <= 7:
            print(userstr.pop(userstr.index(i)))
    print('��������� �����\n')
    for i in userstr:
        print(i)

def z5():
    userstr = (str(input('������� ���� ����������� ������:\n'))).split(' ')
    for i in range(len(userstr)):
        if ((userstr[i])[0]).isupper():
            userstr[i] = userstr[i].upper()
    print(' '.join(userstr))

def z6():
    tempstr = [] #������� � ����
    userstr = str(input('������� ��� ����������� �����\n')).lower()
    for i in userstr:
        if userstr.count(i) == 1:
            tempstr.append(i)
    print(' '.join(tempstr))

def z7():
    tempstr = ''
    filevar = open('urllist.txt', 'r')
    templist = [i.replace('\n', '') for i in filevar] #������� �� ���, �������
    for i in templist:
        if i.startswith('www.'):
            tempstr = 'https://' + i
            if not i.endswith('.com'):
                tempstr += '.com'
            print(tempstr)

def z8():
    from random import randint
    from math import log
    random_numbers = []
    randmaxnumber = int(input('������� ������ �������\n'))
    for i in range(1<<int(round(log(randmaxnumber,2)))):
        if i <= randmaxnumber:
            random_numbers.append(randint(1, 10000))
        else:
            random_numbers.append(0)
    print('��������� �����')
    print(' '.join(str(random_numbers)))
    print('���������� ��������� � ������ {}'.format(len(random_numbers)))
    print('��������� ��������� ����� - {}'.format(randint(1, 10000)))

z8()