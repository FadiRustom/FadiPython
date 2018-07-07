#polymorphism
#الفلمرة: أي متغير ينفذ دالة بنفس الأسم من أكثر منصنف بعمل مختلف
class obj:
    def show(self):
        print('Objict')
        
class human:
    def show(self):
        print('Human')

class animal:
    def show(self):
        print('Animal')
#التابع الذي سيستعدس بالمتغير دالة الإظهار 
def S(v):
    v.show()
#Main
o=obj()
S(o)
a=animal()
h=human()
S(h)
S(a)

