#تعدد الواجهة
class Add:
    def __init__(self, N1, N2):
        self.n1=N1
        self.n2=N2
    def show(self):
        print('Add')
        print (self.n1+self.n2)
        
class Sub:
    def __init__(self, N1, N2):
        self.n1=N1
        self.n2=N2
    def show(self):
        print('Sub')
        print (self.n1-self.n2)

class Mult:
    def __init__(self, N1, N2):
        self.n1=N1
        self.n2=N2
    def show(self):
        print('Mul')
        print (self.n1*self.n2)

class animal:
    def show(self):
        print('Animal')
#التابع الذي سيستعدس بالمتغير دالة الإظهار 
def S(v):
    v.show()
#Main
z=True
#z=input('Input False to exit')
while z:  
    n1=int(input("Enter Firest Number or q to exit"))
    if n1=='q' or n1=='Q':
        pass
    n2=int(input("Enter Second Number"))
    o=input('Enter Operater')
    if o=='+':
        a= Add(n1,n2)
    elif 0=='-':
        a= Sub(n1,n2)
    elif 0=='*':
        a= Mult(n1,n2)
    
    

    S(a)
