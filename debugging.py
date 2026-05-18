''' Packages & Debugging 
  (1) Python packages & Core packages  
  (2) Package Manager  & External Package 
  (3) Debugging


'''

import turtle
print("=======Python Packages & Core Package")

''' Python Packages /Modules : Core ,File and External   '''
# Core Packages


# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)

screen = turtle.Screen()
screen.bgcolor("white")

pizza = turtle.Turtle()
pizza.speed(2)
pizza.pensize(2)

pizza.penup()
pizza.goto(0, -150)
pizza.pendown()
pizza.color("orange", "yellow")
pizza.begin_fill()
pizza.circle(150)
pizza.end_fill()

pizza.color("brown")
for _ in range(8):
    pizza.penup()
    pizza.goto(0, 0)
    pizza.setheading(_ * 45)  # 360 / 8 slices = 45*
    pizza.forward(150)
    pizza.pendown()
    pizza.backward(150)

topping = turtle.Turtle()
topping.shape("circle")
topping.color("red")
topping.penup()

pepperoni_positions = [(-60, 60), (60, 60), (-70, -40),
                       (70, -40), (0, 90), (0, -80)]
for pos in pepperoni_positions:
    topping.goto(pos)
    topping.stamp()

pizza.hideturtle()
topping.hideturtle()

turtle.mainloop()


print("-----")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)


finally:
    my_file.close()


# width
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)


print("DONE")
