import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))



#                               TITLE AND ICON
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship!.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship!.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# bullet1
bullet1Img = pygame.image.load("plasma blast.png")
bullet1X = 0
bullet1Y = 0
bullet1X_change = 0
bullet1Y_change = .03
bullet1_state = "ready"

# bullet2
bullet2Img = pygame.image.load("plasma blast2.png")
bullet2X = 0
bullet2Y = 0
bullet2X_change = 0
bullet2Y_change = .03
bullet2_state = "ready"

# bullet3
bullet3Img = pygame.image.load("plasma blast.png")
bullet3X = 0
bullet3Y = 0
bullet3X_change = 0
bullet3Y_change = .03
bullet3_state = "ready"

# bullet4
bullet4Img = pygame.image.load("plasma blast2.png")
bullet4X = 0
bullet4Y = 0
bullet4X_change = 0
bullet4Y_change = .03
bullet4_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1Img, (x + 2, y + 10))


def fire_bullet2(x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (x + 2, y + 10))


def fire_bullet3(x, y):
    global bullet3_state
    bullet3_state = "fire"
    screen.blit(bullet3Img, (x + 40, y + 10))


def fire_bullet4(x, y):
    global bullet4_state
    bullet4_state = "fire"
    screen.blit(bullet4Img, (x + 40, y + 10))


running = True
while running:
    screen.fill((0, 0, 0))
    # Background image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_SPACE:
                if bullet1_state == "ready":
                    bullet1X = playerX
                    bullet1Y = playerY
                    fire_bullet1(bullet1X, bullet1Y)
            if event.key == pygame.K_SPACE:
                if bullet2_state == "ready":
                    if bullet1Y <= 280:
                        bullet2X = playerX
                        bullet2Y = playerY
                        fire_bullet2(bullet2X, bullet2Y)
            if event.key == pygame.K_SPACE:
                if bullet3_state == "ready":
                    bullet3X = playerX
                    bullet3Y = playerY
                    fire_bullet3(bullet3X, bullet3Y)
            if event.key == pygame.K_SPACE:
                if bullet4_state == "ready":
                    if bullet3Y <= 280:
                        bullet4X = playerX
                        bullet4Y = playerY
                        fire_bullet4(bullet4X, bullet4Y)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
                print("Keystroke is released")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -2.0
            if event.key == pygame.K_DOWN:
                playerY_change = 2.0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                print("Keystroke is released")

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 520:
        playerY = 520

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750

    # Bullet movement
    if bullet1Y <= 0:
        bullet1Y = 480
        bullet1_state = "ready"

    if bullet1_state == "fire":
        fire_bullet1(bullet1X, bullet1Y)
        bullet1Y -= bullet1Y_change

    if bullet2Y <= 0:
        bullet2Y = 480
        bullet2_state = "ready"

    if bullet2_state == "fire":
        fire_bullet2(bullet2X, bullet2Y)
        bullet2Y -= bullet2Y_change

    if bullet3Y <= 0:
        bullet3Y = 480
        bullet3_state = "ready"

    if bullet3_state == "fire":
        fire_bullet3(bullet3X, bullet3Y)
        bullet3Y -= bullet3Y_change

    if bullet4Y <= 0:
        bullet4Y = 480
        bullet4_state = "ready"

    if bullet4_state == "fire":
        fire_bullet4(bullet4X, bullet4Y)
        bullet4Y -= bullet4Y_change

    player(playerX, playerY)
    pygame.display.update()
