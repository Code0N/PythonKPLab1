from math import log, floor

def calculatePass(passwd):
    totalCharsCount = 95
    alpha = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_punct = r'~`!@#$%^&*()-_+='
    digits = "1234567890"

    totalChars = 95
    otherCharsLen = (len(alpha) + len(upper) + len(upper_punct) + len(digits))

    if len(passwd) == 0:
        raise ValueError()
        return 0

    fAlpha = False
    fUpper = False
    fUpperPunct = False
    fDigit = False
    fOther = False
    charset = 0

    for i in passwd:
        if i in alpha:
            fAlpha = True
        elif i in upper:
            fUpper = True
        elif i in digits:
            fDigit = True
        else:
            fOther = True

        if fAlpha:
            charset += len(alpha)
        if fUpper:
            charset += len(upper)
        if fDigit:
            charset += len(digits)
        if fUpperPunct:
            charset += len(upper_punct)
        if fOther:
            charset += otherCharsLen

        bits = floor(log(charset) * (len(passwd) / log(2)))
        return bits

try:
    PWDStr = calculatePass(str(input('Введите ваш пароль, чтобы мы смогли сохранить его на серверах АНБ\n')))
    if 0 <= PWDStr <= 10:
        print('Ваш пароль неимоверно простой, смените его скорее')
    elif 11 <= PWDStr <= 20:
        print('Ваш пароль слишком слабый')
    elif 21 <= PWDStr <= 40:
        print('Стойкость вашего пароля - ниже среднего')
    elif 41 <= PWDStr <= 60:
        print('Ваш пароль средней стойкости')
    elif 61 <= PWDStr <= 79:
        print('Ваш пароль имеет неплохую стойкость')
    elif 80 <= PWDStr <= 100:
        print('Ваш пароль очень стоек')
    elif PWDStr >= 101:
        print('Отличный пароль')

except:
    print('За что?')