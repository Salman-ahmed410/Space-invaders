import math
import random
import pygame

screenWidth = 1280
screenHeight = 720
playerSpawnX = 600
playerSpawnY = 600
enemySpawnXmin = 50
enemySpawnXmax = 1200
enemySpawnYmin = 50
enemySpawnYmax = 200
enemySpeedX = 5
enemySpeedY = 10
bulletSpeeed = 10
collisionDistance = 27
pygame.init()

screen = pygame.display.set_mode((screenWidth,screenHeight))

background = pygame.image.load('space invaders.jpeg')

pygame.display.set_caption('Space Invaders')

playerIMG = pygame.image.load('player.png')
playerX = playerSpawnX
playerY = playerSpawnY
playerX_change = 0

enemyIMG = []
enemyX = []
enemyY =[]
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('enemy-removebg-preview.png'))
    enemyX.append(random.randint(enemySpawnXmin,enemySpawnXmax))
    enemyY.append(random.randint(enemySpawnYmin,enemySpawnYmax))
    enemyX_change.append(enemySpeedX)
    enemyY_change.append(enemySpeedY)

bulletIMG = pygame.image.load('bullet-removebg-preview.png')
bulletX = 0
bullety = playerSpawnY
bulletX_change = 0
bulletY_change = bulletSpeeed
bulletState = 'ready'

score = 0

font = pygame.font.Font('Audiowide-regular.ttf', 32)
textx = 10
texty = 10

gameOverFont = pygame.font.Font('Audiowide-regular.ttf', 64)


def show_score(x,y):
   score = font.render('Score: ' + str(score), True, (255,255,255))
   screen.blit(score, (x,y))

def game_over_text():
    over_text = gameOverFont.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (400,300))