# -*- coding: cp1251 -*-

#������� �1:
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
userinput = int(input('������� ����� �����: '))
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

