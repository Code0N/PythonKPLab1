# -*- coding: cp1251 -*-

tempstr = ''
filevar = open('urllist.txt', 'r')
templist = [i.replace('\n', '') for i in filevar] #Костыли вы мои, костыли
for i in templist:
    if i.startswith('www.'):
        tempstr = 'https://' + i
        if not i.endswith('.com'):
            tempstr += '.com'
        print(tempstr)