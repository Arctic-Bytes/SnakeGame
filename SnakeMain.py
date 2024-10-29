# Example file showing a basic pygame "game loop"

from Controls import *
from Objects import *

direction = -1
xcord = 0
ycord = 0
xapple = random.randrange(0, 1280)
yapple = random.randrange(0, 720)
snakeWidth = 50
setMovementSpeed = 5
bodyparts = []
snakeLength = 20
snakeLengthIncrease = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screenRect = screen.get_rect()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            direction = controls(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Sky Blue")

    # RENDER YOUR GAME HERE

    snake = drawSnake(screen, xcord, ycord)
    apples = apple(screen, xapple, yapple)

    xcord, ycord = movementSpeed(xcord, ycord, setMovementSpeed)

    if xcord < screenRect.left:
        xcord = screenRect.left
    if xcord > screenRect.right - snakeWidth:
        xcord = screenRect.right - snakeWidth
    if ycord < screenRect.top:
        ycord = screenRect.top
    if ycord > screenRect.bottom - snakeWidth:
        ycord = screenRect.bottom - snakeWidth

    appleCollected = appleCollection(snakeLength, snakeLengthIncrease, snake, apples)
    if appleCollected:
        xapple, yapple, snakeLength = appleCollected

    for part in bodyparts[:-21]:
        head = pygame.Rect(xcord, ycord, snakeWidth, snakeWidth)
        body = pygame.Rect(part[0], part[1], snakeWidth, snakeWidth)
        if head.colliderect(body):
            pygame.quit()

    if len(bodyparts) > snakeLength:
        bodyparts.pop(0)

    checkMatch = False
    for part in bodyparts:
        if part[0] == xcord and part[1] == ycord:
            checkMatch = True
    if not checkMatch:
        bodyparts.append([xcord, ycord])

    for x, y in bodyparts:
        drawSnake(screen, x, y)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
