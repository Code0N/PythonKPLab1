# -*- coding: cp1251 -*-

#Задание 9 перевалка
def  error(not_enought, bills):
    print('Ошибка. Для необходимой вам суммы в банкомате не хватает {} купюр номиналом {} рублей'.format(not_enought, bills))

bills = {1000: 10, 100: 100, 10: 50, 1: 70}
usernum = int(input('Введите сумму денег '))
tempstr = ''
i = 1000
while i >= 1:
    temp = round(usernum / i)
    if temp > bills[i]:
        error(temp, bills[i])
        break
    else:
        tempstr += str(temp)+'*'+str(bills[i])+' '
    i /= 10
print(tempstr)