def pre_process(a=0.97):
	def decorator(func):
		def sigprocess(sig):
			for i in range(len(sig)):
				sig[i] = sig[i] - a*sig[i-1]
			return sig
		return sigprocess
	return decorator

temp = [x for x in range (0, 50, 2)]

@pre_process(a=0.93)
def process_the_signal(sig):
		for i in sig:
			print(i)
		
xx = process_the_signal(temp)
print(xx)