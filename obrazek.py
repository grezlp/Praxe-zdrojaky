from turtle import forward, left, right, getcanvas, exitonclick

forward(50)
left(60)
forward(50)
right(60)
forward(50)
exitonclick()

getcanvas().postscript(file='obrazek.ps')