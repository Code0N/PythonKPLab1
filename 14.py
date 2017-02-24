def non_empty(funcpar):
	def _wrapper():
		temp = [i for i in funcpar() if ((i != '') and not (i is None))] #Костыль, но хоть работает
		return temp
	return _wrapper

	
@non_empty
def get_pages():
	return ['chapter1', '', 'contents', '', 'line1']
	
x = get_pages()

print(x)