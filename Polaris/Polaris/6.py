# -*- coding: cp1251 -*-

tempstr = [] #������� � ����
userstr = str(input('������� ��� ����������� �����\n')).lower()
for i in userstr:
    if userstr.count(i) == 1:
        tempstr.append(i)
print(' '.join(tempstr))