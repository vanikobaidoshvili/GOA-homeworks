from turtle import *

width(7)
begin_fill()
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
 # end of square

# door makeing

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof makeing 

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows makeing

penup()
goto(10, 130)
pendown()
color("blue")
begin_fill()
left(120)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
end_fill()

penup()
goto(140, 130)
pendown()
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick()