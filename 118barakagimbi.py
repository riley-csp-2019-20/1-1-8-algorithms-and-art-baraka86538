import turtle as trtl

b = trtl.Turtle()
b.fillcolor("light blue")
b.setheading(45+90)
b.begin_fill()
b.circle(100, 360, 4)
b.end_fill()

b.fillcolor("black")
b.begin_fill()
b.penup()
b.goto(0,0)
b.right(270)
b.forward(60)
b.pendown()
b.circle(15, 360, 4)
b.end_fill()
b.penup()
b.goto(-115,-42)
b.pendown()
b.begin_fill()
b.circle(15, 360, 4)
b.end_fill()

b.penup()
b.goto(-75,-100)
b.pendown()
b.begin_fill()
b.circle(15, 360, 4)
b.end_fill()

b.penup()
b.goto(-75,-120)
b.pendown()
b.begin_fill()
b.circle(15, 360, 4)
b.end_fill()

b.penup()
b.setheading(180)
b.goto(-80,150)
b.pendown()
b.fillcolor("brown")
b.begin_fill()
b.circle(100, 360, 3)
b.end_fill()

b.penup()
b.goto(0, 400)
b.pendown()
b.fillcolor("yellow")
b.begin_fill()
b.circle(100)
b.end_fill()





wn = trtl.Screen()
wn.mainloop()