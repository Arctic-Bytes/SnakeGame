import pygame
import random


def drawSnake(screen, x, y):
    snake = pygame.draw.rect(screen, "black", pygame.Rect(x, y, 50, 50))
    return snake


def apple(screen, x, y):
    apple = pygame.draw.rect(screen, "red", pygame.Rect(x, y, 25, 25))
    return apple


def appleCollection(snakeLength, snakeLengthIncrease, snake, apples):
    collect = pygame.Rect.colliderect(snake, apples)
    if collect:
        xapple = random.randrange(0, 1000)
        yapple = random.randrange(0, 650)
        snakeLength += snakeLengthIncrease
        return xapple, yapple, snakeLength
