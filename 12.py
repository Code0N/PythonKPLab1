def get_frames(signal,size,overlap):   
    step = size * overlap
    print (step)
    i = 0
    while i<len(signal):
        yield (signal[i:i+size])
        i = i + int(step)


x = [i for i in range(1024)]

for i in get_frames(x, 4, 0.5):
	print(i)