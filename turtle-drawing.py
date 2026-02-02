import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

def draw(x, y):
    t.goto(x, y)

t.penup()
screen.listen()
screen.onscreenclick(draw, 1)  # levé tlačítko
t.pendown()

turtle.done()




