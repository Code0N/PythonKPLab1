from math import trunc

def outError(count, enought):
    print('ƒл¤ выдачи суммы не хватает {} купюр номиналом {} рублей'.format(count, enought))

bills = {1000: 10, 100: 100, 10: 50, 1: 70}
usernum = int(input('¬ведите сумму денег '))
i = 1000
tempstr = ''
while(i >= 1):
    temp = trunc(usernum / i)
    if i < 10:
        i = 1    
    if temp > bills[i]:
        outError(temp, i)
        break
    tempstr += str(temp)+'*'+str(round(i))+' '
    usernum -= temp*i
    i /= 10

print(tempstr)
