# -*- coding: cp1251 -*-

from random import choice

rangelist = []
while True:
	temp = str(input('‚ведите число. или символ длЯ прекращениЯ: '))
	if temp.isdigit():
		rangelist.append(int(temp))
	else:
		break
isup = True
temp = -1
for i in rangelist:
    if i <= temp:
        rangelist = False
        temp = i
        break
    else:
        temp = i
print(isup)