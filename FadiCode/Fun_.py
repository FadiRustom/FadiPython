#DessineTurtle
# استدعاء المكتبة
from turtle import *
#Fun Carre
def carre(Tall, Color='black'):
    "Function qui Dessine a Carre with Taller & Color of Line 'Doc'"
    color(Color)
    c=0
    while c<4:
        forward(Tall)
        right(90)
        c=c+1
        
#Fun Angle
def angle(Tall, Color='black'):
    "Function gui Dessine a Angle with Taller & Color of Line agret=60 'Doc' "
    color(Color)
    c=0
    while c<3:
        forward(Tall)
        right(120)
        c=c+1


        
