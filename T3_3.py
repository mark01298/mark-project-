import turtle
one = input("какого цвета будет первая линия которую нарисует черепашка?")
two = input("какого цвета будет вторая линия которую нарисует черепашка?")
three = input("какого цвета будет третья линия которую нарисует черепашка?")
four = input("какого цвета будет четвертая линия которую нарисует черепашка?")
shirina = input("какая будет ширина у линий?")
turtle.penup()
turtle.goto(-300,250)
turtle.pendown()
turtle.color(one)
turtle.pensize(shirina)
turtle.forward(600)
turtle.penup()
turtle.goto(-300,150)
turtle.pendown()
turtle.color(two)
turtle.forward(600)
turtle.penup()
turtle.goto(-300,50)
turtle.pendown()
turtle.color(three)
turtle.forward(600)
turtle.penup()
turtle.goto(-300,-50)
turtle.pendown()
turtle.color(four)
turtle.forward(600)







