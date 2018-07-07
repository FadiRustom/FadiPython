#Python 2-3
# Draw with turtle for Square of Circle
import turtle
def draw_square(lenght):
    turtle.color("yellow")    
    turtle.shape("square")
    turtle.speed(10)
    for i in range(1, 5):
        turtle.forward(lenght)
        turtle.right(90)

def circle_of_square(lenght, angle):
    window = turtle.Screen()
    window.bgcolor("blue")
    for i in range (0, 360, angle):
        draw_square(lenght)
        turtle.left(angle)
    #End
    window.exitonclick()


circle_of_square(100, 10)
