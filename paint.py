"""Paint, for drawing shapes."""

from turtle import *
from freegames import vector
import math

#Esta función dibuja una línea
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    # Esta función mueve la tortuga a donde hace click el usuario
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def rectangle(start, end):
    up()
    # Esta función mueve la tortuga a donde hace click el usuario
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()


def circle(start, end):
    """Dibuja un circulo."""
    radius = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    up()
    goto(start.x + radius, start.y)
    down()
    begin_fill()
    circle = Turtle()  
    circle.circle(radius)  
    end_fill()


def triangle(start, end):
    """Dibuja un triangulo."""
    up()
    # Esta función mueve la tortuga a donde hace click el usuario
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """almacena el punto inicial para dibujar la figura"""     
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Almacena el valor en el estado bajo la clave."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
#Escuchan lo que teclea el usuario y en base a eso ejecuta algo en específico
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
