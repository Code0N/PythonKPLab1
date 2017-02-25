import itertools
import random
import time
from datetime import datetime, timedelta
TeamList = ['Динамо',
    'Надинамо',
    'Барселона',
    'Ювентус',
    'Дом №13',
    'Нижние хамыри',
    'Верхние болотцы',
    'Светлый путь',
    'Воложск',
    'Stratovarius',
    'Арсенал',
    'Рабиновичус',
    'Манчестер юнайтед',
    'VS',
    'Бешенные бобры',
    'Серверные песцы']


random.shuffle(TeamList)
print ('\nСписок команд::')
print ('\n'.join(TeamList))
 
TeamList = [TeamList[d:d+4] for d in range(0, len(TeamList), 4)]

print ('\nСписок групп::')
print ('Группа A: ',TeamList[0])
print ('Группа B: ',TeamList[1])
print ('Группа C: ',TeamList[2])
print ('Группа D: ',TeamList[3])
print ('\nРасписание матчей::')


tempDate = "14.09.2017"

startTime = [14,9,2017]
endTime = [14,4,2018]

print ('Начало сезона::', str(startTime[0])+'/'+str(startTime[1])+'/'+str(startTime[2])+' '+ str('22:45') )
print ('Конец сезона', str(endTime[0])+'/'+str(endTime[1])+'/'+str(endTime[2])+' '+ str('22:45') )

now_date = datetime.now()
now_date = now_date.replace(2017,9,14)

print ('\n') #Перевод строки

a = datetime(2017, 9, 20)
b = timedelta(days=7)

while a<=datetime(2018, 4, 14):
    a=a+b
    print ('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45')