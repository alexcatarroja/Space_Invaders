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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy_final.png"))
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3.0)
    enemyY_change.append(40)

# Super Enemy

# Enemy
enemy_super_Img = pygame.image.load("enemy_super.png")
enemy_superX = (random.randint(0, 750))
enemy_superY = (random.randint(50, 150))
enemy_superX_change = 3.0
enemy_superY_change = 40
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

# bullet3
bullet3Img = pygame.image.load("plasma blast.png")
bullet3X = 0
bullet3Y = 0
bullet3X_change = 0
bullet3Y_change = 20
bullet3_state = "ready"

# bullet4
bullet4Img = pygame.image.load("plasma blast2.png")
bullet4X = 0
bullet4Y = 0
bullet4X_change = 0
bullet4Y_change = 20
bullet4_state = "ready"

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


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def enemy_super(x, y):
    screen.blit(enemy_super_Img, (x, y))


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


def is_collision3(enemyX, enemyY, bullet3X, bullet3Y):
    distance = math.sqrt((math.pow(enemyX - bullet3X, 2)) + (math.pow(enemyY - bullet3Y, 2)))
    if distance < 30:
        return True
    else:
        return False


def is_collision4(enemyX, enemyY, bullet4X, bullet4Y):
    distance = math.sqrt((math.pow(enemyX - bullet4X, 2)) + (math.pow(enemyY - bullet4Y, 2)))
    if distance < 30:
        return True
    else:
        return False


def collision_super(enemy_superX, enemy_superY, bullet1X, bullet1Y):
    distance = math.sqrt((math.pow(enemy_superX - bullet1X, 2)) + (math.pow(enemy_superY - bullet1Y, 2)))
    if distance < 40:
        return True
    else:
        return False


def player_collision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 20:
        return True
    else:
        return False



#                                  GAME LOOP
running = True
Input = True
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

    # enemy movement
    for i in range(num_of_enemies):

        # GAME OVER
        if enemyY[i] > 480:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200, 250)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 6.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 750:
            enemyX_change[i] = -4.5
            enemyY[i] += enemyY_change[i]

        # super enemy movement
        enemy_superX += enemy_superX_change
        if enemy_superX <= 0:
            enemy_superX_change = 1
            enemy_superY += enemy_superY_change
        elif enemy_superX >= 750:
            enemy_superX_change = -1
            enemy_superY += enemy_superY_change

        SS_collision = player_collision(enemyX[i], enemyY[i], playerX, playerY)
        if SS_collision:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200, 250)
            playerImg = pygame.image.load("plasma blast.png")
            break

        collision = is_collision(enemyX[i], enemyY[i], bullet1X, bullet1Y)
        if collision:
            bullet1Y = 480
            bullet1_state = "ready"
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(10, 40)
            score_value += 1


        collision2 = is_collision2(enemyX[i], enemyY[i], bullet2X, bullet2Y)
        if collision:
            bullet2Y = 480
            bullet2_state = "ready"
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(10, 40)


        collision3 = is_collision3(enemyX[i], enemyY[i], bullet3X, bullet3Y)
        if collision:
            bullet3Y = 480
            bullet3_state = "ready"
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(10, 40)


        collision4 = is_collision4(enemyX[i], enemyY[i], bullet4X, bullet4Y)
        if collision:
            bullet4Y = 480
            bullet4_state = "ready"
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(10, 40)

        enemy(enemyX[i], enemyY[i], i)

    super_collision = collision_super(enemy_superX, enemy_superY, bullet1X, bullet1Y)
    if super_collision:
        collision_c += 1
        print(collision_c)
        if collision_c >= 15:
            bullet1Y = 480
            bullet1_state = "ready"
            enemy_superX = (750)
            enemy_superY = (-15)
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
    enemy_super(enemy_superX, enemy_superY)
    show_score(textx, textY)
    pygame.display.update()
