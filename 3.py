userstr = str(input('Введите номер вашей кредитки, если хотите повысить нам настроение: '))
if not userstr.isdigit():
    print('Номер кредитной карты может состоять только из цифр')
elif len(userstr) < 16 or len(userstr) > 16:
    print('Ошибка длины номера карты: допустимо только 16 цифр')
else:
    print('{} **** **** {}'.format(userstr[0:4], userstr[12:16]))
