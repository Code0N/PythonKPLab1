# -*- coding: cp1251 -*-

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