# -*- coding: cp1251 -*-

try:
    userinput = float(input('������� ��� ����������� ����� � ������������ ����: '))
    if userinput < 0:
        raise ValueError('����� �������������')
    print('{} ���. {} ���.'.format(str(userinput).split('.')[0], str(userinput).split('.')[1])) 
except ValueError:
    print('An error occured: ValueError')
except:
    print('��� ���� ������� ������������ ��� ����� �������')