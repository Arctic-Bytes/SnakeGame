import pygame

direction = -1  # 0 = up, 1 = down, 2 = left, 3 = right


def controls(event):
    global direction
    if event.type == pygame.KEYDOWN:
        # if event.mod == pygame.KMOD_NONE:
            # print('No modifier keys were in a pressed state when this '
                  # 'event occurred.')
        # else:
        if event.dict["unicode"] == 'w':
            direction = 0
        if event.dict["unicode"] == 's':
            direction = 1
        if event.dict["unicode"] == 'a':
            direction = 2
        if event.dict["unicode"] == 'd':
            direction = 3

    return direction

