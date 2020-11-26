import pygame

# initialise
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Logo
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("rocket.png")
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:
    # Color of the Screen
    screen.fill((0, 0, 0))
    # CLose the window
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            running = False
    player()
    pygame.display.update()

# Images source flaticon.com
