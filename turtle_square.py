import turtle

# Maak een turtle genaamd Frits
frits = turtle.Turtle()

# Maak het scherm aan, zodat we kunnen zien wat Frits uitspookt.
s = turtle.getscreen()

# Teken de eerste zijde
frits.forward(100)
# Draai de turtle 90 graden
frits.left(90)
# Teken de tweede zijde
frits.forward(100)
# Draai de turtle 90 graden
frits.left(90)
# Teken de derde zijde
frits.forward(100)
# Draai de turtle 90 graden
frits.left(90)
# Teken de vierde zijde
frits.forward(100)

# Zorg dat het schermpje niet sluit als we klaar zijn.
turtle.exitonclick()