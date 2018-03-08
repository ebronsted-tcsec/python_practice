import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

emily = turtle.Turtle()
emily.shape("turtle")
emily.speed(1)

draw_circle(emily, "green", 50, 25, 0)
draw_circle(emily, "blue", 50, 0, 0)
draw_circle(emily, "yellow", 50, -25, 0)

emily.penup()
emily.goto(0, -50)
emily.color('black')
emily.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
emily.goto(0, -80)