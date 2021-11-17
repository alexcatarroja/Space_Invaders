import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
backround = pygame.image.load("backround 1.tif")


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

# Enemy
enemy_ultra_Img = pygame.image.load("enemy_super.png")
enemy_ultra_X = (random.randint(0, 750))
enemy_ultra_Y = (random.randint(50, 150))
enemy_ultra_X_change = 3.0
enemy_ultra_Y_change = 40
collision_c = 0 # gives the enemy health


# bullet1
bullet1Img = pygame.image.load("plasma blast.png")
bullet1X = 0
bullet1Y = 0
bullet1X_change = 0
bullet1Y_change = 20
bullet1_state = "ready"

# bullet2
bullet2Img = pygame.image.load("plasma blast2.png")
bullet2X = 0
bullet2Y = 0
bullet2X_change = 0
bullet2Y_change = 20
bullet2_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 58)


def game_over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy_ultra(x, y):
    screen.blit(enemy_ultra_Img, (x, y))


def fire_bullet1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1Img, (x + 2, y + 10))


def fire_bullet2(x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (x + 2, y + 10))


def collision_super(enemy_ultra_X, enemy_ultra_Y, bullet1X, bullet1Y):
    distance = math.sqrt((math.pow(enemy_ultra_X - bullet1X, 2)) + (math.pow(enemy_ultra_Y - bullet1Y, 2)))
    if distance < 40:
        return True
    else:
        return False


def is_collision(enemyX, enemyY, bullet1X, bullet1Y):
    distance = math.sqrt((math.pow(enemyX - bullet1X, 2)) + (math.pow(enemyY - bullet1Y, 2)))
    if distance < 30:
        return True
    else:
        return False


def is_collision2(enemyX, enemyY, bullet2X, bullet2Y):
    distance = math.sqrt((math.pow(enemyX - bullet2X, 2)) + (math.pow(enemyY - bullet2Y, 2)))
    if distance < 30:
        return True
    else:
        return False




#                                  GAME LOOP
running = True
while running:
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(backround, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 5.5
            if event.key == pygame.K_LEFT:
                playerX_change = -5.5
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

# ultra enemy movement
    enemy_ultra_X += enemy_ultra_X_change
    if enemy_ultra_X <= 0:
        enemy_ultra_X_change = 1
        enemy_ultra_Y += enemy_ultra_Y_change
    elif enemy_ultra_X >= 750:
        enemy_ultra_X_change = -1
        enemy_ultra_Y += enemy_ultra_Y_change

    super_collision = collision_super(enemy_ultra_X, enemy_ultra_Y, bullet1X, bullet1Y)
    if super_collision:
        collision_c += 1
        print(collision_c)
        if collision_c >= 15:
            bullet1Y = 480
            bullet1_state = "ready"
            enemy_ultra_X = (750)
            enemy_ultra_Y = (-15)
            score_value += 1
            print(score_value)
            collision_c = 0

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


    player(playerX, playerY)
    enemy_super(enemy_superX, enemy_superY)
    show_score(textx, textY)
    pygame.display.update()

