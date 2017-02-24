def extra_enumerate(x):
	llen = len(x)
	allsum = 0
	for i in x:
		allsum += i
	sum = 0
	powr = 0
	for i in x:
		sum += i
		powr = (100 / (allsum / sum)) / 100
		yield (i, sum, powr)
		

x = [1,3,4,2]
for elem, cum, frac in extra_enumerate(x):
	print(elem, cum, frac)