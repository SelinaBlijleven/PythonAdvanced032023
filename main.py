import turtle

# Maak een turtle
frits = turtle.Turtle()

# Schermpje
s = turtle.getscreen()

# Teken de eerste zijde
frits.forward(100)
# Draai de turtle
frits.left(90)
# Teken de tweede zijde
frits.forward(100)
# Draai de turtle
frits.left(90)
# Teken de derde zijde
frits.forward(100)
# Draai de turtle
frits.left(90)
# Teken de vierde zijde
frits.forward(100)

# Zorg dat het schermpje niet sluit
turtle.exitonclick()