import turtle 

s = turtle.Screen()
s.bgcolor("white")

t = turtle.Turtle()

t.penup()
t.goto(-200, -100)
t.pendown()
t.begin_fill()
t.color("brown")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.penup()
t.goto(-200, 0)
t.pendown()
t.begin_fill()
t.color("red")
t.goto(-150, 50)
t.goto(-100, 0)
t.end_fill()

t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("brown")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.color("red")
t.goto(50, 50)
t.goto(100, 0)
t.end_fill()

t.penup()
t.goto(200, -100)
t.pendown()
t.begin_fill()
t.color("brown")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.penup()
t.goto(200, 0)
t.pendown()
t.begin_fill()
t.color("red")
t.goto(250, 50)
t.goto(300, 0)
t.end_fill()

t.penup()
t.goto(-300, 200)
t.pendown()
t.begin_fill()
t.color("yellow")
t.circle(50)
t.end_fill()

t.penup()
t.goto(350, -100)
t.pendown()
t.begin_fill()
t.color("green")
t.goto(320, 50)
t.goto(380, 50)
t.goto(350, -100)
t.end_fill()

