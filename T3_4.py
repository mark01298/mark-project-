import turtle
t = turtle.textinput('TURTLE', 'какая длина стороны будет у треугольника?')
tt = turtle.textinput('TURTLE', 'а какой цвет будет у треугольника?')
ttt = turtle.textinput('TURTLE', 'а какая ширина будет у треугольника?')
turtle.pencolor(tt)
turtle.pensize(ttt)
turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()
turtle.forward(int(t))
turtle.left(120)
turtle.forward(int(t))
turtle.left(120)
turtle.forward(int(t))
























