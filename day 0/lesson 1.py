from turtle import *  

shape("turtle")
#we want to paint a house

#step 1: draw a square
speed(20)
begin_fill()
color("purple")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

#end of square
#drawing a window

left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(60)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200,200)
width(2)
color("blue")

right(60)
forward(190)
left(90)
forward(20)
pendown()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
back(25)
left(90)
forward(50)
back(25)
left(90)
forward(25)
back(50)
penup()
forward(130)
pendown()
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
back(50)
left(90)
forward(25)
right(90)
forward(25)
penup()
goto(-30,-30)
pendown()
color("black")


exitonclick()
