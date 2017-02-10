# -*- coding: cp1251 -*-

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