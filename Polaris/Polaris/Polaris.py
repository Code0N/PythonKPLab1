# -*- coding: cp1251 -*-

#������� �1:
def z1():
    try:
        userinput = float(input('������� ��� ����������� ����� � ������������ ����: '))
        if userinput < 0:
            raise ValueError('����� �������������')
        print('{} ���. {} ���.'.format(str(userinput).split('.')[0], str(userinput).split('.')[1])) #�������-������
    except ValueError as ex:
        print('An error occured: ValueError')
    except:
        print('��� ���� ������� ���������� ��� ����� �������')

#������� �2
def z2():
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
    print('{} **** **** {}'.format(userstr[0:4], userstr[12:16]))


#z1()
#z2()
#z3()
