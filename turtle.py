import turtle

turtle.Screen().bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
distance = 0
turtle.pencolor("yellow")
for i in range(100):
    turtle.forward(distance)
    turtle.left(90)
    distance+=5
