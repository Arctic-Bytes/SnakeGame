import pygame

direction = -1  # 0 = up, 1 = down, 2 = left, 3 = right


def controls(event):
    global direction
    if event.type == pygame.KEYDOWN:
        if event.dict["unicode"] == 'w':
            direction = 0
        if event.dict["unicode"] == 's':
            direction = 1
        if event.dict["unicode"] == 'a':
            direction = 2
        if event.dict["unicode"] == 'd':
            direction = 3

    return direction


def movementSpeed(xcord, ycord, movementSpeed):
    if direction == 0:
        ycord += -movementSpeed
    if direction == 1:
        ycord += movementSpeed
    if direction == 2:
        xcord += -movementSpeed
    if direction == 3:
        xcord += movementSpeed
    return xcord, ycord
