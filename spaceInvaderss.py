import math
import random
import pygame

pygame.init()

screenWidth = 800
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Space Invaders')

background_img = pygame.image.load('space invaders.jpeg')
background = pygame.transform.scale(background_img, (screenWidth, screenHeight))
playerIMG = pygame.image.load('player.png')
enemyIMG_FILE = 'enemy-removebg-preview.png'
bulletIMG = pygame.image.load('bullet-removebg-preview.png')

playerSpawnX = 368
playerSpawnY = 420
playerX = playerSpawnX
playerY = playerSpawnY
playerX_change = 0

enemySpawnXmin = 50
enemySpawnXmax = 736
enemySpawnYmin = 10
enemySpawnYmax = 100
enemySpeedX = 5
enemySpeedY = 40
num_of_enemies = 7

enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("green_enemy-removebg-preview.png"))
    enemyX.append(random.randint(enemySpawnXmin, enemySpawnXmax))
    enemyY.append(random.randint(enemySpawnYmin, enemySpawnYmax))
    enemyX_change.append(enemySpeedX)
    enemyY_change.append(enemySpeedY)

bulletX = 0
bulletY = playerSpawnY
bulletY_change = 10
bullet_state = 'ready'

collisionDistance = 15
score = 0
game_over = False

font = pygame.font.Font('Audiowide-regular.ttf', 32)
textX = 10
textY = 10

gameOverFont = pygame.font.Font('Audiowide-regular.ttf', 64)
clock = pygame.time.Clock()


def show_score(x, y):
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def game_over_text():
    over_text = gameOverFont.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (400, 300))


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletIMG, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < collisionDistance


running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                playerX_change = 6
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, screenWidth - 64))

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over = True
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= screenWidth - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        if bullet_state == 'fire':
            collision = isCollision(enemyX[i], enemyY[i], bulletX + 16, bulletY + 10)
            if collision:
                bulletY = playerSpawnY
                bullet_state = 'ready'
                score += 1
                enemyX[i] = random.randint(enemySpawnXmin, enemySpawnXmax)
                enemyY[i] = random.randint(enemySpawnYmin, enemySpawnYmax)

        enemy(enemyX[i], enemyY[i], i)

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = playerSpawnY
        bullet_state = 'ready'

    player(playerX, playerY)
    show_score(textX, textY)
    if game_over:
        game_over_text()
    pygame.display.update()
    clock.tick(60)
pygame.quit()