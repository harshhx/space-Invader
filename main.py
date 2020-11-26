import pygame
import random
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
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load("flying.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 0


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    # Color of the Screen
    screen.fill((0, 0, 0))
    # CLose the window
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            running = False
        # Check if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        # Check for key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    # adding game boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# Images source flaticon.com
