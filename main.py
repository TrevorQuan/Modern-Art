import turtle
import random

turtle.shape("turtle")
turtle.speed(0)

for i in range(1000):
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  turtle.color(red, green, blue)

  x = random.randint(-300, 300)
  y = random.randint(-300,300)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

  # Draw a rectangle
  # Length and height to be random, between 10,100

  l = random.randint(10, 100)
  h = random.randint(10, 100)
  turtle.begin_fill()
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(h)
  turtle.right(90)
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(h)
  turtle.right(90)
  turtle.end_fill()

  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  turtle.color(red, green, blue)

  x = random.randint(-300, 300)
  y = random.randint(-300,300)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  r = random.randint(10,50)
  turtle.begin_fill()
  turtle.circle(r)
  turtle.end_fill()