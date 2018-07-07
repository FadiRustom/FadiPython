class Test():
    ''' Document the class test'''
    def __init__(self, Name, Eye):
        print("Test Class", 'Father')
        self.name = Name
        self.eye = Eye
        
    def test(self,i):
        self.i =i
        for self.i in range(self.i, self.i+5):
            print (self.i)
        return "i= ", self.i
    
class Child(Test):
    def __init__(self, Name, Eye, Toys):
        print("Child test")
        Test.__init__(self, Name, Eye)
        self.toys = Toys
    def child():
        #self.i=i
        return '("Self")'

m = Child('Rustom', 'Blue', 20)
print(m.name, m.toys)
m.test(4)
print(m.test(3))
n=Child.child()

print(n)
