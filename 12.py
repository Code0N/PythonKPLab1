from math import ceil

def get_frames(signal, size=1024, overlap=0.5):
	_i = -ceil(overlap) #begin
	j = (size-1)-overlap #end
	for i in range(len(signal)):
		_i += ceil(overlap)
		j += ceil(overlap)
		temp = signal[_i:j]
		if temp != []:
			yield temp
		

signal = [i for i in range(1000)]
for i in get_frames(signal, 16, 5):
	print(i)