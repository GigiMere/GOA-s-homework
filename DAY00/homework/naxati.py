from turtle import*
width(2)
speed(30)
begin_fill()
color("black")
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)
forward(250)
color("grey")
end_fill()
left(180)
color("black")
forward(100)
right(90)
forward(200)
left(90)
forward(70)
left(90)
forward(200)
right(90)

#grass

width(5)
color("green")
right(90)
penup()
goto(0,0)
pendown()
begin_fill()
forward(800)
left(180)
forward(2000)
left(90)
forward(500)
left(90)
forward(2500)
left(90)
forward(500)
end_fill()
penup()
goto(75,0)
pendown()
color("brown")
begin_fill()
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
left(180)
forward(50)
width(2)
left(90)
color("black")
forward(15)
penup()
goto(0,0)
pendown()
width(5)
left(60)
forward(400)
right(180)
forward(400)
right(60)
forward(200)
right(60)
forward(400)
left(180)
forward(400)
left(60)
forward(200)
width(2)
right(90)
forward(50)
left(180)
forward(50)
left(180)
left(90)
#stairs
penup()
goto(0,0)
pendown()
left(60)
forward(70)
left(120)
forward(270)
right(60)
forward(50)
right(120)
forward(320)
left(60)
forward(70)
left(120)
forward(390)
right(60)
forward(70)
right(120)
forward(460)
left(60)
forward(70)
left(120)
forward(530)
#sun 
color("green")
width(5)
penup()
begin_fill()
color("yellow")
goto(-500, 300)
pendown()
circle(50)
end_fill()
left(90)
forward(40)
left(180)
penup()
goto(-300,0)
pendown()
color("black")
left(180)
right(25)
forward(30)
right(125)
forward(30)
left(180)
forward(30)
right(31)
forward(35)
right(90)
begin_fill()
circle(10)
end_fill()

#GOA
color("green")
left(90)
penup()
goto(0,0)
forward(280)
right(90)
forward(20)
pendown()
forward(25)
right(180)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(15)
left(90)
forward(10)
penup()
left(180)
forward(50)
right(90)
forward(10)
pendown()
forward(5)
left(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(40)
penup()
left(90)
forward(70)
pendown()
left(80)
forward(40)
right(150)
forward(40)
left(180)
forward(14)
left(80)
forward(10)
exitonclick()