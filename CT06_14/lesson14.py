print("... you probably know it already.")
import turtle
scren = turtle.Screen()
scren.setup(width=600, height=400)

jim = turtle.Turtle()
jim.color("Yellow")
jim.forward(100)
jim.left(45)
jim.forward(100)
jim.color("Black")

scren.mainloop()