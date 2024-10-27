import pygame


def drawSnake(screen, x, y):
    snake = pygame.draw.rect(screen, "black", pygame.Rect(x, y, 50, 50))
    return snake


def apple(screen, x, y):
    apple = pygame.draw.rect(screen, "red", pygame.Rect(x, y, 25, 25))
    return apple
