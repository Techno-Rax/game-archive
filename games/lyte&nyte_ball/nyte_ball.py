import pygame # For 2d games
import math  # For measuring distance
import time 
import random
from pygame import mixer

# To initialise pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((500, 500))

# Global Variables
score_value = 0
no_of_obstacles = 2

# Title And Logo
pygame.display.set_caption("Nite Ball")
icon = pygame.image.load("data/icon2.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('data/nite.png')

# Music
mixer.music.load("music/bensound-creativeminds.mp3")
mixer.music.play(-1)

# ball
ballimg = pygame.image.load('data/light_ball.png')
bally = 468
ballx = 235
ball_change = -1.5

# Obstacle
obsimg = pygame.image.load('data/obstacle.png')
obsx = 0
obsy = 15
obs_change = 2.5

obs2img = pygame.image.load('data/obstacle2.png')
obs2x = 398
obs2y = 65
obs2_change = -2.5

obs3img = pygame.image.load('data/obstacle.png')
obs3x = 0
obs3y = 115
obs3_change = 2.5

obs4img = pygame.image.load('data/obstacle2.png')
obs4x = 398
obs4y = 165
obs4_change = -2.5

# Functions


def ball(x, y):
	screen.blit(ballimg, (x, y))


def obstacle(x, y):
	screen.blit(obsimg, (x, y))


def obstacle2(x, y):
	screen.blit(obs2img, (x, y))

def obstacle3(x, y):
	screen.blit(obs3img, (x, y))

def obstacle4(x, y):
	screen.blit(obs4img, (x, y))

def isCollision(ballx, bally, obsx, obsy):
	distance1 = math.sqrt(math.pow(obsx - ballx, 2) + (math.pow(obsy - bally, 2)))
	if distance1 < 25:
		return True
	else:
 		return False

def isCollision2(ballx, bally, obs2x, obs2y):
	distance2 = math.sqrt(math.pow(obs2x - ballx, 2) + (math.pow(obs2y - bally, 2)))
	if distance2 < 25:
		return True
	else:
		return False

def isCollision3(ballx, bally, obs3x, obs3y):
	distance3 = math.sqrt(math.pow(obs3x - ballx, 2) + (math.pow(obs3y - bally, 2)))
	if distance3 < 25:
		return True
	else:
		return False

def isCollision4(ballx, bally, obs4x, obs4y):
	distance4 = math.sqrt(math.pow(obs4x - ballx, 2) + (math.pow(obs4y - bally, 2)))
	if distance4 < 25:
		return True
	else:
		return False

# To show score
font = pygame.font.Font('fonts/freesansbold.ttf', 28)
def show_score(x, y):
	score = font.render(str(score_value), True, (225, 255, 255))
	screen.blit(score, (x, y))

# The main loop
run = True
while run:

	# RGB = Red, Green, Blue
	screen.fill((0, 0, 0))

	# Background
	screen.blit(background, (0, 0))

	# Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE or pygame.K_DOWN:
				ball_change = -0.2
			print("""
				<Key Pressed>
				""")

		if event.type == pygame.KEYUP:
			ball_change = -1.5
			print("""
				<Key Released>
				""")
			
	# Movement of the ball
	bally  += ball_change

	# Movement of the obstacle
	obsx += obs_change
	if obsx > 400:
		obs_change *= -1

	if obsx < 0:
		obs_change *= -1

	obs2x += obs2_change
	if obs2x > 400:
		obs2_change *= -1

	if obs2x < 0:
		obs2_change *= -1

	obs3x += obs3_change
	if obs3x > 400:
		obs3_change *= -1

	if obs3x < 0:
		obs3_change *= -1

	obs4x += obs4_change
	if obs4x > 400:
		obs4_change *= -1

	if obs4x < 0:
		obs4_change *= -1

	# Movement of the ball(win)
	if bally < 0:
		for i in range(1, 10):
			x1 = random.randint(0, 250)
			x2 = random.randint(0, 250)
			x3 = random.randint(0, 250)
			x4 = random.randint(0, 250)

			y1 = random.randint(100, 400)
			y2 = random.randint(100, 400)
			y3 = random.randint(100, 400)
			y4 = random.randint(100, 400)

			d1 = random.randint(1, 5)
			d2 = random.randint(1, 5)
			d3 = random.randint(1, 5)

			bally = 468
			obsx = x1
			obs2x = x2
			obs3x = x3
			obs4x = x4

			obsy = y1
			obs2y = y2
			obs3y = y3
			obs4y = y4

			obs_change = d1
			obs2_change = -d2
			obs3_change = d3
			obs4_change = -d1

		time.sleep(0.1)
		score_value += 1

	# Collision
	collision = isCollision(ballx, bally, obsx, obsy)
	collision2 = isCollision2(ballx, bally, obs2x, obs2y)
	collision3 = isCollision3(ballx, bally, obs3x, obs3y)
	collision4 = isCollision4(ballx, bally, obs4x, obs4y)
	if collision or collision2 or collision3 or collision4:
		time.sleep(0.1)
		bally = 210
		time.sleep(0.1)
		bally = 468

	ball(ballx, bally)
	show_score(250, 100)
	obstacle(obsx, obsy)
	obstacle2(obs2x, obs2y)
	obstacle3(obs3x, obs3y)
	obstacle4(obs4x, obs4y)
	pygame.display.update()
