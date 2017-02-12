# -*- coding: cp1251 -*-

def frange(start, stop, step=0.1):
    i = start
    while i < stop-step*2:
        i += step
        yield round(i, len(str(step))-2)

for i in frange(1, 5):
    print(i)