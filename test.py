from utils import delay, moveTo


def moveY():
    delay(2)
    y = 0
    while(y < 901):
        moveTo([750, y])
        y += 100
        delay(.8)

def moveX():
    delay(2)
    x = 600
    while(x < 1601):
        moveTo([x, 700])
        x += 100
        delay(.8)

moveX()

# battle 400, 600