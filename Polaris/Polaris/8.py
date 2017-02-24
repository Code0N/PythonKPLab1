# -*- coding: cp1251 -*-

from random import randint
from math import log
random_numbers = []
randmaxnumber = int(input('Введите размер массива\n'))
for i in range(1<<int(round(log(randmaxnumber,2)))):
    if i <= randmaxnumber:
        random_numbers.append(randint(1, 10000))
    else:
        random_numbers.append(0)
print('Случайные числа')
print(' '.join(str(random_numbers)))
print('Количество элементов в списке {}'.format(len(random_numbers)))
print('Отдельное случайное число - {}'.format(randint(1, 10000)))