"""Memory, puzzle game of number pairs."""
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# Se cambia la lista de objetos a usar en el memorama
tiles = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "¡!", "@", "#", "$", "%", "&", "//", "()", "=", "?", "<", "::", "[]", "||"] * 2
state = {'mark': None}
hide = [True] * 64

tap_count= 0

def square(x, y):
    """Dibuja el tablero de juego."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordendas a indices."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte los titulos a coordenadas."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def all_revealed():
    """Verifica si todas las fichas están reveladas."""
    return all(not hide[i] for i in range(len(hide)))

def tap(x, y):
    """actualizas las casillas escondidas en base a los taps y cuenta el numero de taps."""
    spot = index(x, y)
    mark = state['mark']
    global tap_count  
    tap_count += 1  
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    print("Número de toques:", tap_count) 

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
def draw():
    """Dibuja la imagen."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Se ajusta la posición de los elementos en el cuadro dependiendo si es alfabético o signos
        if tiles[mark].isalpha():
            goto(x + 13, y )
        else:
            goto(x + 15, y+3 )
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
