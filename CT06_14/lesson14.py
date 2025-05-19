print("... you probably know it already.")
import turtle
scren = turtle.Screen()
scren.setup(width=600, height=400)

jim = turtle.Turtle()
jim.shape("square")
jim.speed(10)
jim.color("Yellow")
jim.forward(100)
jim.left(45)
jim.forward(100)
jim.color("Black")
jim.forward(50)
jim.left(90)
jim.forward(50)
jim.left(90)
jim.forward(50)
jim.left(90)
jim.forward(50)

pippey=turtle.Turtle()
pippey.shape("square")
pippey.speed(10)
pippey.color("Yellow")
pippey.left(135)
pippey.forward(100)
pippey.right(90)
pippey.forward(50)
pippey.right(90)
pippey.forward(50)
pippey.left(45)
pippey.forward(100)
pippey.left(45)
pippey.forward(50)

jim.penup()
jim.right(45)
jim.forward(100)
jim.right(90)
jim.forward(50)
jim.write("bnana")

import random
abert=turtle.Turtle()
abert.speed(10)

for count in range(15):
    randx=random.randint(-300,300)
    randy=random.randint(-200,200)

    abert.goto(randx,randy)
    j

scren.mainloop()