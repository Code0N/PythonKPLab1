# -*- coding: cp1251 -*-

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