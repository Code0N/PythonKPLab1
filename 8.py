# -*- coding: cp1251 -*-

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