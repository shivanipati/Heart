import turtle
k = turtle.Turtle()
m = turtle.Turtle()


k.hideturtle()
k.goto(0,-10)
k.pensize(3)
k.color('red')
k.begin_fill()
k.left(140)
k.forward(180)
k.circle(-90,200)
k.setheading(60)
k.circle(-90,200)
k.forward(178)
k.end_fill()

k.penup()
k.goto(-130,130)
k.pendown()
k.color('white')
k.write("LOVE YOU Mom,Dad",font=("verdana",19  ,"bold"))

turtle.down()
