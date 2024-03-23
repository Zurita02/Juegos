"""Snake, classic arcade game."""

from random import randrange
from turtle import *
from random import choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ['blue', 'green', 'yellow', 'orange', 'purple']

# Elegir colores aleatorios para la serpiente y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != 'red'])

def change(x, y):
    """Esta fucnion cambia la direccion de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Verifica que la serpeinte este dentro del rango del tablero, si es asi regresa un valor verdadero."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente hacia enfrente una casilla."""
    head = snake[-1].copy()
    head.move(aim)
    global snake_color, food_color

    color(snake_color)
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    color(food_color)

    #Se elige coordenada al zar para mover la comida cada vez que avanza la serpiente
    food.x, food.y = choice([(food.x +10, food.y), (food.x -10, food.y), (food.x, food.y +10), (food.x, food.y -10), (food.x, food.y)])
    square(food.x, food.y, 9, food_color)

    update()  # Actualizar la ventana con los nuevos colores

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Usa el color aleatorio de la serpiente
    square(food.x, food.y, 9, food_color)  # Usa el color aleatorio de la comida
    update()
    ontimer(move, 100)

   

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
