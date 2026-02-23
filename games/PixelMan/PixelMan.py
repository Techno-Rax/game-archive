import pygame
import time
import math
import random
from pygame import mixer
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

clock = pygame.time.Clock()
start_time = time.time()

# MUSIC AND SFX #

# VARIABLES #
FPS = 100
walk_count = 0
jumpCount = 10
score_bar = 40
score_pos = 380

# COLOURS
BLACK = (0, 0, 0)
BLUE = (4, 94, 97)
RED = (110, 8, 11)
YELLOW = (129, 135, 16)
GREEN = (76, 161, 81)
gem_colour = 0

isJump = False
isCollision = False
coin_collision1 = False
coin_collision2 = False
coin_collision3 = False

# SCORES 
score = 0
coin_score = 0
total_score = 0
high_score = 0

# Fonts #
pygame.font.init()
font = pygame.font.Font('fonts/freesansbold.ttf', 20)
game_over_font = pygame.font.Font('fonts/freesansbold.ttf', 50)
total_score_font = pygame.font.Font('fonts/freesansbold.ttf', 20)

# SCREEN #
SCREENSIZE = (800, 500)
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pixel Man Run")

# BACKGROUND #
background_img = pygame.image.load('Background/background.png').convert()
bg_x = 0

# PLAYER #
player_img = [pygame.image.load('Characters/R1.png'), pygame.image.load('Characters/R1.png'), pygame.image.load('Characters/R2.png'), pygame.image.load('Characters/R2.png'), pygame.image.load('Characters/R3.png'), pygame.image.load('Characters/R3.png'), pygame.image.load('Characters/R4.png'),pygame.image.load('Characters/R4.png')]
x,y = 125,365

# RECTS #
player_rect = pygame.Rect(x+48, y+25, 30, 65)
player_speed = 2

tileRect1 = pygame.Rect(800, 390, 20, 80)
tileRect2 = pygame.Rect(1300, 390, 50, 95)
tileRect3 = pygame.Rect(1900, 390, 70, 120)
tileSpeed = 4

# GEM #
gem_img = [pygame.image.load("images/gem.png"),pygame.image.load("images/gem2.png"),pygame.image.load("images/gem3.png"),pygame.image.load("images/gem4.png")]
gem_rect1 = pygame.Rect(0, 0, 25, 35)
gem_rect2 = pygame.Rect(0, 0, 25, 35)
gem_rect3 = pygame.Rect(0, 0, 25, 35)


def tilesMovement():
	global x, player_speed, y
	global isCollision
	global stroke, coin_collision, coin_score
	global tileRect1, tileRect2, tileRect3

	player_rect.x = x+48
	player_rect.y = y+25

	tileRect1.x -= tileSpeed
	if tileRect1.left <= -tileRect1.width:
		tileRect1.width = random.randint(15, 30)
		tileRect1.height = random.randint(60, 130)
		tileRect1.x = random.randint(800, 1500)
		tileRect1.y = 450-tileRect1.height


	tileRect2.x -= tileSpeed
	if tileRect2.left <= -tileRect2.width:
		tileRect2.width = random.randint(15, 30)
		tileRect2.height = random.randint(20, 160)
		tileRect2.x = random.randint(2200, 2900)
		tileRect2.y = 450 - tileRect2.height


	tileRect3.x -= tileSpeed
	if tileRect3.left <= -tileRect3.width:
		tileRect3.width = random.randint(15, 20)
		tileRect3.height = random.randint(40, 110)
		tileRect3.x = random.randint(3600, 4200)
		tileRect3.y = 450 - tileRect3.height

	# COLLISION #
	if player_rect.colliderect(tileRect1):
		if abs(tileRect1.left - player_rect.right) < 5:
			x -= player_speed
			isCollision = True
		elif tileRect1.top - player_rect.bottom < 10:
			player_rect.bottom = tileRect1.top
			y = player_rect.top-20
			isCollision = True
		else:
			isCollision = False

	# Collision with tiles # 
	if player_rect.colliderect(tileRect2):
		if abs(tileRect2.left - player_rect.right) < 5:
			x -= player_speed
			isCollision = True
		elif tileRect2.top - player_rect.bottom < 10:
			player_rect.bottom = tileRect2.top
			y = player_rect.top-20
			isCollision = True
		else:
			isCollision = False

	if player_rect.colliderect(tileRect3):
		if abs(tileRect3.left - player_rect.right) < 5:
			x -= player_speed
			isCollision = True
		elif tileRect3.top - player_rect.bottom < 10:
			player_rect.bottom = tileRect3.top
			y = player_rect.top-20
			isCollision = True
		else:
			isCollision = False

	if player_rect.colliderect(gem_rect1) and not(isCollision):
		coin_collision1 = True
		coin_score += 0.4
	
	elif player_rect.colliderect(gem_rect2) and not(isCollision):
		coin_collision2 = True
		coin_score += 0.4

	elif player_rect.colliderect(gem_rect3) and not(isCollision):
		coin_collision3 = True
		coin_score += 0.4

	else:
		coin_collision1 = False
		coin_collision2 = False
		coin_collision3 = False


def draw():
	global blockx, blocky
	global walk_count
	global bg_x
	global score_bar, score_pos
	global gem_colour

	# backround ----------------------------------------------------------------
	relative_x = bg_x % background_img.get_rect().width
	screen.blit(background_img, (relative_x-background_img.get_rect().width ,0))
	if relative_x < 800:
		screen.blit(background_img, (relative_x,0))

	if not(isJump):
		bg_x -= 1

	# BLOCKS -------------------------------------------------------------------
	pygame.draw.rect(screen,(0,0,0), (0, 450, 800 ,50))

	# player -------------------------------------------------------------------
	if not isCollision:
		if walk_count < 32:
			screen.blit(player_img[walk_count//4], (x,y))
			walk_count += 1
		if walk_count >= 32:
			walk_count = 0

	# Collision Rects ----------------------------------------------------------
	pygame.draw.rect(screen, (0,0,0), tileRect1, 0)
	pygame.draw.rect(screen, (0,0,0), tileRect2, 0)
	pygame.draw.rect(screen, (0,0,0), tileRect3, 0)

	gem_rect1.x = tileRect1.x
	gem_rect2.x = tileRect2.x
	gem_rect3.x = tileRect3.x

	gem_rect1.y = 370-tileRect1.height
	gem_rect2.y = 370-tileRect2.height
	gem_rect3.y = 370-tileRect3.height

	# SCORE --------------------------------------------------------------------
	score_value = font.render(str(round(score,1))+" m", True, (0,0,0))
	screen.blit(score_value, (385,12))
	pygame.draw.rect(screen,(0,0,0), (score_pos, 35, score_bar ,2), 0)
	score_bar += 10
	score_pos -= 5

	# HIGH_SCORE
	high_score_value = font.render(str(round(high_score)), True, (0,0,0))
	screen.blit(high_score_value, (15,12))

	# COIN SCORE
	screen.blit(gem_img[gem_colour], (750,14))
	coin_value = font.render(f"{math.ceil(coin_score)}", True, (0,0,0))
	screen.blit(coin_value, (770,12))


	# GEM #
	if coin_collision1 == False and gem_rect1.x > player_rect.x and isCollision == False:
		screen.blit(gem_img[gem_colour], (tileRect1.x+tileRect1.width/3, 390-tileRect1.height))
	if coin_collision2 == False and gem_rect2.x > player_rect.x and isCollision == False:
		screen.blit(gem_img[gem_colour], (tileRect2.x+tileRect2.width/3, 390-tileRect2.height))
	if coin_collision3 == False and gem_rect3.x > player_rect.x and isCollision == False:
		screen.blit(gem_img[gem_colour], (tileRect3.x+tileRect3.width/3, 390-tileRect3.height))

def endscrn():
	global score_r, coin_score_r, total_score, score, coin_score

	if isCollision:
		game_over = game_over_font.render("GaMe OvEr", True, (200,5,5))
		total = total_score_font.render(f"{round(total_score)}", True, (0, 0, 0))
		retry = font.render("(click to retry)", True, (50,50,50))
		screen.blit(game_over, (250,210))
		screen.blit(retry, (320,265))
		score -= 0.1
		coin_score -= 0.1
		
		if total_score >= (score_r + coin_score_r*10):
			total_score = (score_r + coin_score_r*10)
		if coin_score <= 0:
			coin_score = 0
		if score <= 0:
			score = 0
		if coin_score==0 and score == 0:
			total_score += 1
			screen.blit(total, (370,320))


def re():
	tileRect1.x = 800
	tileRect1.y = 450-tileRect1.height
	tileRect2.x = 1300
	tileRect2.y = 450-tileRect2.height
	tileRect3.x = 1600
	tileRect3.y = 450-tileRect3.height

run = True
while run:
	elapsed_time = time.time()

	# EVENTS -------------------------------------------------------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				isJump = True
			if event.button == 1 and isCollision:
				score = 0
				coin_score = 0
				bg_x = 0
				x,y = 125,365
				player_speed = 2
				tileSpeed = 4
				score_bar = 40
				score_pos = 380
				isCollision = False
				re()

	keys = pygame.key.get_pressed()

	if not(isJump):
		if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
			isJump = True
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount**2) * 0.5 * neg
			jumpCount -= 1
			FPS = 50
			bg_x -= 2
			tileSpeed = 7.5

		else:
			isJump = False
			jumpCount = 10
			FPS = 100
			tileSpeed = 4

	real_time = int(elapsed_time-start_time)
	if not(isCollision):
		score += 0.01
		score_r = score
		coin_score_r = coin_score

	if total_score >= high_score:
		high_score = total_score


	draw()
	tilesMovement()
	endscrn()
	clock.tick(FPS)
	pygame.display.update()
