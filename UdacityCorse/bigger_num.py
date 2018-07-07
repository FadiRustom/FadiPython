def bigger(a, b):
	if a >b:
		return a
	else:
		return b

	
def biggerst(a, b, c):
	return bigger(bigger(a,b),c)

print(biggerst(5,3,6))
#6
print(biggerst(15,3,6))
#15
print(biggerst(5,13,6))
#13
print(biggerst(13,13,6))
 
