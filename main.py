import pygame
import random

# initialise
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("images/abstract-space-background-with-nebula-stars.jpg")

# Title and Logo
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images/rocket.png")
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load("images/flying.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 20


# Ready -> You can't fire the bullet
# Fire -> the bullet is currently moving


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
bulletImg = pygame.image.load("images/bullet.png")
bulletX = random.randint(0, 736)
bulletY = 480
bulletX_change = 0
bulletY_change = 1.2
# Ready -> You can't fire the bullet
# Fire -> the bullet is currently moving
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # Color of the Screen
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # CLose the window
    for event in pygame.event.get():
        if pygame.QUIT == event.type:
            running = False
        # Check if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        # Check for key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    # adding player boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    # adding enemy boundaries
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    if enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# Images source flaticon.com
