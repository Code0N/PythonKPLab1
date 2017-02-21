rangelist = []
while True:
	temp = str(input('Введите число. или символ для прекращения: '))
	if temp.isdigit():
		rangelist.append(int(temp))
	else:
		break

temp = None
for i in range(len(rangelist)-1):
	if (rangelist[i] >= rangelist[i+1]):
		temp = rangelist[i+1]
		break

if temp is None:
	print('True')
else:
	print('False')