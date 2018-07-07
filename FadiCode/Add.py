# عمل تغليف بطريقة اللائحة حتى لا تعرف المتغيرات الخاصة بصنف

class Add:
    def __init__(self, **Num):
        self.n=Num
    def set_n1(self, n1) :
        self.n[0]=n1
    def get_n1(self):
        return self.n[0]
    def set_n2(self, n2) :
        self.n[1]=n2
    def get_n2(self):
        return self.n[1]
    def set_n3(self, n3) :
        self.n[2]=n3
    def get_n3(self):
        return self.n[2]

a=Add()
a.set_n1(22)
a.set_n2(33)
print(a.get_n1()+ a.get_n2())

    
    
