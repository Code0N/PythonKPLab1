# -*- coding: cp1251 -*-

userstr = (str(input('Введите свою бесполезную строку:\n'))).split(' ')
for i in range(len(userstr)):
    if ((userstr[i])[0]).isupper():
        userstr[i] = userstr[i].upper()
print(' '.join(userstr))
