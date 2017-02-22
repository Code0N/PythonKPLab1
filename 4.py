userstr = (str(input("Введите любую, желательно - осмысленную, строку\n"))).split(' ')
print('Слова длинее семи символов:\n')
for i in userstr:
	if len(i) > 7:
		print(i)
		del i
print("Слова длиною от 4 до 7 символов\n")
for i in userstr:
	if (len(i) >= 4) and (len(i) <= 7):
		print(i)
		del i
print('Остальные слова\n')
for i in userstr:
	if len(i) < 4:
		print(i)