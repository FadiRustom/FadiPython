#Python 2-3
# Draw with turtle for Square & Circle
import turtle
def draw_square(mathel,light):
    for i in range(1, 5):
        mathel.forward(light)
        mathel.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create Square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad,100)
    #Create Circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #End
    window.exitonclick()

draw_art()
