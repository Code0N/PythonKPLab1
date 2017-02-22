tempstr = [] #ѕустота и тлен
userstr = str(input('Введите ваш бесполезный текст\n')).lower()
for i in userstr:
    if userstr.count(i) == 1:
        tempstr.append(i)
print(' '.join(tempstr))