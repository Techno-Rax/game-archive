'''
MADE BY ANOOJ SHETE (16yr old)
MADE with pygame
MADE in 24 hrs
:)
'''

# REQUIRED MODULES #
import pygame
import time
import warnings
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.init()
warnings.filterwarnings("ignore", category=DeprecationWarning)
clock = pygame.time.Clock()

# GLOBAL VARIABLES #
WIDTH = 500
HEIGHT = 500

FPS = 120

ball_speed_x = 2
ball_speed_y = 2

score1, score2 = 0, 0

easy = 320
hard = 100

level = easy

ln = 0

# GLOBAL BOOLEANS #
is_homescreen = True
is_gamescreen = False
is_play = False
is_settings = False
is_credit = False
is_music = "ON"
is_difficulty = "EASY"

# COLOURS #
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 234, 255)
RED = (237, 28, 36)
GREEN = (77, 221, 120)

# FONTS #
font = pygame.font.Font('fonts/pdark.ttf', 20)
end_scrn_font = pygame.font.Font('fonts/pdark.ttf', 40)
credit_font = pygame.font.Font('fonts/pdark.ttf', 14)

# IMAGES #
home = [pygame.image.load("img/home1.png"),pygame.image.load("img/home2.png")]

# MAIN DISPLAY #
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG NEON")

# Balls
trial_ball = pygame.Rect(20,200,15,15)
ball = pygame.Rect(75,220,15,15)
trial_ball_speed_x = 2
trial_ball_speed_y = 2

# PLAYERS
player1 = pygame.Rect(25, 250, 15, 75)
player2 = pygame.Rect(450, 250, 15, 75)

# HOME SCREEN RECTANGLES
play = pygame.Rect(215, 240, 90, 35)
settings = pygame.Rect(195, 300, 130, 35)
credits = pygame.Rect(200, 360, 118, 35)
title_rect = pygame.Rect(123, 52, 289, 33)

def bounce():
	bounceSound = mixer.Sound("music_sfx/bounce.wav")
	bounceSound.play()

def music():
	mixer.music.load("music_sfx/music.mp3")
	mixer.music.play(-1)

def home_screen():
	global trial_ball_speed_y, trial_ball_speed_x

	# THE TITLE
	titletxt = end_scrn_font.render("PONG NEON", True, BLUE)
	screen.blit(titletxt, (120, 50))
	#pygame.draw.rect(screen, WHITE, title_rect, 1)

	# PLAY BUTTON #
	if mx>=215 and mx<=304 and my<=276 and my>=241:
		pygame.draw.rect(screen, WHITE, play, 3)
	else:
		pygame.draw.rect(screen, WHITE, play, 1)
	PLAYtxt = font.render("PLAY", True, BLUE)
	screen.blit(PLAYtxt, (228, 248))

	# SETTINGS #
	if mx>=195 and mx<=324 and my<=335 and my>=301:
		pygame.draw.rect(screen, WHITE, settings, 3)
	else:
		pygame.draw.rect(screen, WHITE, settings, 1)
	SETTINGStxt = font.render("SETTINGS", True, BLUE)
	screen.blit(SETTINGStxt, (202, 308))

	# CREDITS #
	if mx>=200 and mx<=314 and my<=396 and my>=361:
		pygame.draw.rect(screen, WHITE, credits, 3)
	else:
		pygame.draw.rect(screen, WHITE, credits, 1)
	CREDITStxt = font.render("CREDITS", True, BLUE)
	screen.blit(CREDITStxt, (208, 368))

	# BALL MOVEMENT & COLLISION #
	pygame.draw.rect(screen, WHITE, trial_ball, 0)

	trial_ball.x += trial_ball_speed_x
	trial_ball.y += trial_ball_speed_y

	if trial_ball.y >= 485:
		trial_ball_speed_y *= -1
	if trial_ball.y <= 0:
		trial_ball_speed_y *= -1
	if trial_ball.x >= 485:
		trial_ball_speed_x *= -1
	if trial_ball.x <= 0:
		trial_ball_speed_x *= -1

	if title_rect.colliderect(trial_ball):
		if abs(title_rect.right - trial_ball.left) <= 10:
			trial_ball_speed_x *= -1
		if abs(title_rect.left - trial_ball.right) <= 10:
			trial_ball_speed_x *= -1
		if abs(title_rect.top - trial_ball.bottom) <= 10:
			trial_ball_speed_y *= -1
		if abs(title_rect.bottom - trial_ball.top) <= 10:
			trial_ball_speed_y *= -1

	if play.colliderect(trial_ball):
		if abs(play.right - trial_ball.left) <= 10:
			trial_ball_speed_x *= -1
		if abs(play.left - trial_ball.right) <= 10:
			trial_ball_speed_x *= -1
		if abs(play.top - trial_ball.bottom) <= 10:
			trial_ball_speed_y *= -1
		if abs(play.bottom - trial_ball.top) <= 10:
			trial_ball_speed_y *= -1

	if settings.colliderect(trial_ball):
		if abs(settings.left - trial_ball.right) <= 10:
			trial_ball_speed_x *= -1
		if abs(settings.right - trial_ball.left) <= 10:
			trial_ball_speed_x *= -1
		if abs(settings.top - trial_ball.bottom) <= 10:
			trial_ball_speed_y *= -1
		if abs(settings.bottom - trial_ball.top) <= 10:
			trial_ball_speed_y *= -1

	if credits.colliderect(trial_ball):
		if abs(credits.right - trial_ball.left) <= 10:
			trial_ball_speed_x *= -1
		if abs(credits.left - trial_ball.right) <= 10:
			trial_ball_speed_x *= -1
		if abs(credits.top - trial_ball.bottom) <= 10:
			trial_ball_speed_y *= -1
		if abs(credits.bottom - trial_ball.top) <= 10:
			trial_ball_speed_y *= -1

	home_button()

def game_screen():
	global ln

	# LINE
	pygame.draw.line(screen, BLUE, (250, ln), (250, 0), 2)
	ln += 10
	if ln >= 500:
		ln = 500

	# BALL
	pygame.draw.rect(screen, WHITE, ball, 0)

	# PLAYER
	pygame.draw.rect(screen, WHITE, player1, 0)
	pygame.draw.rect(screen, WHITE, player2, 0)

	# SCORE
	SCORE1txt = font.render(f"{score1}", True, BLUE)
	SCORE2txt = font.render(f"{score2}", True, BLUE)

	screen.blit(SCORE1txt, (215, 35))
	screen.blit(SCORE2txt, (270, 35))
	home_button()

def setting():
	global is_music, is_difficulty
	SETTINGS_TITLE = end_scrn_font.render(f"SETTINGS", True, BLUE)
	screen.blit(SETTINGS_TITLE, (150, 40))
	music_on_off = font.render(f"MUSIC", True, WHITE)
	difficulty = font.render(f"difficulty", True, WHITE)
	music_on_off2 = font.render(f"{is_music} 'N, Y'", True, BLUE)
	difficulty2 = font.render(f"{is_difficulty} 'E, H'", True, BLUE)
	screen.blit(music_on_off, (100, 150))
	screen.blit(difficulty, (100, 200))
	screen.blit(music_on_off2, (200, 150))
	screen.blit(difficulty2, (250, 200))

def credit():
	CREDIT_TITLE = end_scrn_font.render(f"CREDITS", True, BLUE)
	CREDITtxt1 = credit_font.render(f"This Game Is Made By Anooj Shete.", True, WHITE)
	CREDITtxt2 = credit_font.render(f"MUSIC SOUND CLOUD 'VALIANT'", True, WHITE)
	CREDITtxt3 = credit_font.render(f"Thanks For Playing My Game.", True, WHITE)
	CREDITtxt4 = credit_font.render(f"""Follow Me On Instagram anoojshete""", True, BLUE)
	screen.blit(CREDIT_TITLE, (150, 40))
	screen.blit(CREDITtxt1, (100, 150))
	screen.blit(CREDITtxt2, (120, 200))
	screen.blit(CREDITtxt3, (120, 250))
	screen.blit(CREDITtxt4, (80, 300))

	home_button()


def movement():
	global ball_speed_y, ball_speed_x

	# PLAYER 1 MOVEMENT #
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_UP or event.key == pygame.K_w:
			player1.y -= 3
		if event.key == pygame.K_DOWN or event.key == pygame.K_s:
			player1.y += 3
		

	# BALL MOVEMENT #
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.x >= level and ball_speed_x != -2:
		if ball.y < player2.y+75//2:
			player2.y -= 2.5
		if ball.y > player2.y+75//2:
			player2.y += 2.5

def Collision():
	global ball_speed_y, ball_speed_x, score1, score2

	if player1.y <= 0:
		player1.y = 0
	elif player1.y >= 425:
		player1.y = 425
	if player2.y <= 0:
		player2.y = 0
	elif player2.y >= 425:
		player2.y = 425

	if ball.y >= 485:
		ball_speed_y *= -1
		bounce()

	if ball.y <= 0:
		ball_speed_y *= -1
		bounce()

	if ball.x >= 485:
		score1 += 1
		ball.x, ball.y = 425, 250
		ball_speed_x *= -1

	if ball.x <= 0:
		score2 += 1
		ball.x, ball.y = 75, 250
		ball_speed_x *= -1

	# Collision with paddeles
	if player1.colliderect(ball):
		if abs(player1.right - ball.left) <= 10:
			ball_speed_x *= -1
		if abs(player1.top - ball.bottom) <= 10:
			ball_speed_y *= -1
		if abs(player1.bottom - ball.top) <= 10:
			ball_speed_y *= -1
		bounce()

	if player2.colliderect(ball):
		if abs(player2.left - ball.right) <= 10:
			ball_speed_x *= -1
		if abs(player2.top - ball.bottom) <= 10:
			ball_speed_y *= -1
		if abs(player2.bottom - ball.top) <= 10:
			ball_speed_y *= -1
		bounce()

def boolean_handling():
	global is_play, is_homescreen, is_gamescreen

	if is_play == True:
		is_gamescreen = True
		is_homescreen = False

	if is_homescreen == True:
		score1, score2 = 0, 0
		ball.x, ball.y = 75, 250

	if is_difficulty  == "EASY":
		level = easy
	if is_difficulty  == "HARD":
		level = hard

def end_screen():
	global score1, score2
	global ln

	if score1 >= 10 and not score2 >= 10:
		score1 = 10
		WINtxt = end_scrn_font.render("YOU WIN", True, GREEN)
		screen.blit(WINtxt, (140, 180))
		ln -= 20

	if score2 >= 10 and not score1 >= 10:
		score2 = 10
		WINtxt = end_scrn_font.render("YOU LOSE", True, RED)
		screen.blit(WINtxt, (140, 180))
		ln -= 20

	home_button()

def home_button():
	if mx>=478 and my<=34:
		screen.blit(home[1], (480, 10))
	else:
		screen.blit(home[0], (480, 10))

if is_music=="ON":
	music()

run = True
while run:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if is_settings:
				if event.key == pygame.K_y:
					is_music = "ON"
				if event.key == pygame.K_n:
					is_music = "OFF"

				if event.key == pygame.K_e:
					is_difficulty = "EASY"
				if event.key == pygame.K_h:
					is_difficulty = "HARD"

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1 and mx>=215 and mx<=304 and my<=276 and my>=241:
				time.sleep(0.1)
				is_play = True
				is_gamescreen = True
				is_homescreen = False
				is_credit = False
				is_settings = False
				score1, score2 = 0, 0
				ball.x, ball.y = 75, 250
				ln = 0
			if event.button == 1 and mx>=200 and mx<=314 and my<=396 and my>=361:
				time.sleep(0.1)
				is_play = False
				is_credit = True
				is_homescreen = False
				is_gamescreen = False
				is_settings = False
			if event.button == 1 and mx>=195 and mx<=324 and my<=335 and my>=301:
				time.sleep(0.1)
				is_play = False
				is_credit = False
				is_homescreen = False
				is_gamescreen = False
				is_settings = True
			if event.button == 1 and mx>=478 and my<=34:
				score1, score2 = 0, 0
				is_play = False
				is_homescreen = True
				is_gamescreen = False
				is_credit = False
				is_settings = False

	# MOUSE POS #
	mx, my = pygame.mouse.get_pos()
	#print(mx, my)

	if is_homescreen:
		home_screen()
	if is_gamescreen:
		game_screen()
		movement()
		Collision()
	if is_credit:
		credit()
	if is_settings:
		setting()

	boolean_handling()
	end_screen()

	clock.tick(FPS)
	pygame.display.update()

#-------------------------------------------------------------------x---------------------------------------------------------------------#