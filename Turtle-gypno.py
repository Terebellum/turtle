import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed(15)

col = ('white','pink','cyan', "red", "blue", "gray")
for i in range (360):
    t.pencolor(col[i%6])
    t.forward(i*2)
    t.right(80)
