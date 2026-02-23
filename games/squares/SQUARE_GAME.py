import pygame
import random
import time
import math
import warnings
from pygame import mixer
from pygame.locals import *

warnings.filterwarnings("ignore", category=DeprecationWarning)


mainClock = pygame.time.Clock()
start_time = time.time()

pygame.init()

WINDOW_SIZE = (500, 500)
win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Squares?")
icon = pygame.image.load("data/cursor_green.png")
pygame.display.set_icon(icon)

# Global Variables
radius = 2
rect_radius = 2
pause_radius = 2
rect_counter = 0
c = 0
x = 110
y = 0
speed = 2
score = 0
counter = 0
level = 1
missed_shots = 0
screen_shake = 0
difficulty = ""

# Background music
mixer.music.load("data/music.wav")
mixer.music.play(-1)

# Fonts
font = pygame.font.Font('data/freesansbold.ttf', 15)
difficulty_font = pygame.font.Font('data/freesansbold.ttf', 13)

# Blocks #
tiles = [pygame.Rect(50,50,64,64)]

# Cursor
cursor_img = [pygame.image.load("data/cursor.png"), pygame.image.load("data/cursor_pressed.png"), pygame.image.load("data/cursor_green.png")]
is_pressed = False
is_green = False

# Pause/play
pause_img = [pygame.image.load("data/pause.png"), pygame.image.load("data/play.png")]

# IMAGES #
def cursor():
	if is_pressed:
		win.blit(cursor_img[1], (mx-8, my-8))
	elif is_green:
		win.blit(cursor_img[2], (mx-8, my-8))
	else:
		win.blit(cursor_img[0], (mx-8, my-8))

def pause_func():
	if is_pause:
		win.blit(pause_img[1], (455, 455))
	else:
		win.blit(pause_img[0], (455, 455))

def ScoreTxt(x, y):
	scoretxt = font.render(f"SCORE", True, (0, 234, 255))
	score_txt = font.render(f"{score}", True, (255,255,255))
	win.blit(scoretxt, (425, 20))
	win.blit(score_txt, (447, 40))

def timer(x, y):
	timetxt = font.render("TIME", True, (0, 234, 255))
	time_txt = font.render(f"{elapsed_time}", True, (255,255,255))
	win.blit(timetxt, (20, 20))
	win.blit(time_txt, (30, 40))

def LevelTxt(x, y):
	leveltxt = font.render("LEVEL", True, (0, 234, 255))
	level_txt = font.render(f"{level}", True, (255,255,255))
	win.blit(leveltxt, (225, 20))
	win.blit(level_txt, (240, 40))

def MissedShotTxt(x, y):
	missedtxt = font.render("MISSED", True, (0, 234, 255))
	missed_txt = font.render(f"{missed_shots}", True, (255,255,255))
	win.blit(missedtxt, (425, 70))
	win.blit(missed_txt, (447, 90))

def SPEEDtxt(x, y):
	speedtxt = font.render("SPEED", True, (0, 234, 255))
	speed_txt = font.render(f"{speed//1}", True, (255,255,255))
	win.blit(speedtxt, (15, 70))
	win.blit(speed_txt, (30, 90))

def difficultytxt():
	difficulty_txt = difficulty_font.render(difficulty, True, (255,255,255))
	win.blit(difficulty_txt, (10, 480))


is_pause = False
run = True
while run:
	win.fill((0,0,0))
	mx, my = pygame.mouse.get_pos()

	elapsed_time = int(time.time() - start_time)

	#  Events  #
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				is_play = not is_play

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				is_pause = not is_pause

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				is_pressed = True
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				is_pressed = False

	#  DRAW HERE  #
	pygame.draw.line(win, (0, 234, 255), (405, 0),(405, 500), 2)
	pygame.draw.line(win, (0, 234, 255), (85, 0),(85, 500), 2)
	pygame.draw.circle(win, (153, 32, 161), (mx, my), rect_radius, 2)
	block = pygame.draw.rect(win, (212, 109, 252), [x,y,25,25])

	if not is_pause:
		y += speed
		speed += 0.001

	if is_pause:
		pygame.draw.circle(win, (0, 220, 255), (455+8, 455+8), pause_radius, 2)
		pause_radius += 20


	if not is_pause:
		pause_radius = 2

	if speed > 15:
		speed = 15

	if y > 500:
		y = -30
		missed_shots += 1
		x = random.randint(100, 380)
		screen_shake=30

	if elapsed_time % 60 < 5 and level < 5:
		pygame.draw.circle(win, (90, 202, 214), (244, 44), radius, 2)
		radius += 8
	else:
		radius = 2

	# Collisions #
	if math.sqrt(math.pow(x-mx, 2) + math.pow(y-my, 2)) <= 35 and my > y and mx > x:
		is_green = True
	else:
		is_green = False

	if is_green and is_pressed:
		y = -30
		x = random.randint(100, 380)
		score += 1
		coinSound = mixer.Sound("data/coin.wav")
		coinSound.play()
		rect_counter = 60

	if rect_counter > 0:
		rect_counter -= 2
		rect_radius += 16
	if rect_counter <= 0:
		rect_counter = 0
	if rect_counter <= 0:
		rect_radius = 2

	# LEVELS #
	if elapsed_time>=60 and elapsed_time<120:
		level = 2
		difficulty = '"NORMAL"'
	elif elapsed_time>=120 and elapsed_time<180:
		level = 3
		difficulty = '"HARD"'
	elif elapsed_time>=180 and elapsed_time<240:
		level = 4
		difficulty = '"INSANE"'
	elif elapsed_time>=210:
		level = "??"
		difficulty = '"SH!T"'
	else:
		difficulty = '"EASIE"'

	cursor()
	pause_func()
	LevelTxt(x, y)
	ScoreTxt(x,y)
	difficultytxt()
	MissedShotTxt(x, y)
	timer(x,y)
	SPEEDtxt(x, y)

	# Screen Shake #

	if radius>=415 and radius<500:
		screen_shake = 30

	if screen_shake > 0:
		screen_shake -= 1

	render_offset = [0,0]
	if screen_shake:
		render_offset[0] = random.randint(0, 8) - 4
		render_offset[1] = random.randint(0, 8) - 4

	pygame.mouse.set_visible(False)
	win.blit(pygame.transform.scale(win, (500, 500)), render_offset)
	pygame.display.update()
	mainClock.tick(60)

# Thank You! #