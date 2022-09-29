#Importaciones
from turtle import Turtle, Screen

#Bienvenida

print('Bienvenido/a al programa de dibujo de un cuadrado')

#Entrega de datos

lado= int(input('Dime cuannto mide el lado del cuadrado: '))

#Dibujo de cuadrado

pantalla= Screen()
pantalla.setup(400, 300)
pantalla.screensize(400, 300)

tortuga= Turtle()
tortuga.penup()
tortuga.goto(0, 0)
tortuga.pendown()
tortuga.write('(0, 0)')
tortuga.setx(lado)
tortuga.write('(' + str(lado) + ",0)") #También se podría usar .format
#ejemplo: tortuga.write('({0},{0})'.format(lado))
tortuga.sety(lado)
tortuga.write('(' + str(lado) + ',' + str(lado) + ')')
tortuga.setx(0)
tortuga.write('(0,' + str(lado) + ')')
tortuga.home()

pantalla.exitonclick()

