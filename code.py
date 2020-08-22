# CREATED BY MUHAMMAD HANAN ASGHAR
import turtle

turtle.bgcolor('black')

turtle.pensize(3)
turtle.goto(5,100)
for _ in range(6):
	for colors in ['red','yellow','green','blue','cyan','magenta','white']:
		turtle.color(colors)
		turtle.left(10)
		turtle.forward(200)
		turtle.backward(200)

input()
