try:
    userinput = float(input('Введите своЄ бесполезное число в вещественном виде: '))
    if userinput < 0:
        raise ValueError('Число отрицательное')
    print('{} руб. {} коп.'.format(str(userinput).split('.')[0], str(userinput).split('.')[1])) 
except ValueError:
    print('An error occured: ValueError')
except:
    print('Ваш ввод слишком неподходящий для этого скрипта')