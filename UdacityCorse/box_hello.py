
def bar(n,ch='-'):
	return n*ch

def box(txt):
	print( '+'+bar(len(txt))+'+')
	print ('|' + txt + '|')
	print ('+'+bar(len(txt))+"+")



box('Hello')
