'''
>>THIS GAME IS MADE BY ANOOJ SHETE

>>IF ANYONE WANTS TO MODIFY THE GAME MAY GIVE CREDITS
'''
import pygame
import math
import time
import warnings
pygame.init()  # To initialse pygame

warnings.filterwarnings("ignore", category=DeprecationWarning)
start_time = time.time()

clock = pygame.time.Clock()  # For time functions
SCREEN_SIZE = (800, 500)
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("MR. BONES")
icon = pygame.image.load('data/R1.png')
pygame.display.set_icon(icon)

# Background Image and Musis(if any)
background = pygame.image.load('data/background.jpg').convert_alpha()
game_over_bull = False

# Musics and sound effects

# Variables
isJump = False
jumpCount = 13
walkCount = 0
enemyWalkCount = 0
fireCount = 0
crusher_distance = 100

d = 30

width = 80
height = 80
life = 3
health = 10.0
health_value = 100

level = 1

# PLayer
RIGHT = [pygame.image.load('data/RIGHT1.png'),pygame.image.load('data/RIGHT2.png'), pygame.image.load('data/RIGHT1.png')]
LEFT = [pygame.image.load('data/LEFT1.png'),pygame.image.load('data/LEFT2.png'), pygame.image.load('data/LEFT1.png')]
playerRight = [pygame.image.load('data/R1.png'),pygame.image.load('data/R2.png'),pygame.image.load('data/R3.png'),pygame.image.load('data/R4.png'),pygame.image.load('data/R1.png'),pygame.image.load('data/R2.png'),pygame.image.load('data/R3.png'),pygame.image.load('data/R4.png'),pygame.image.load('data/R1.png')]
playerLeft = [pygame.image.load('data/L1.png'),pygame.image.load('data/L2.png'),pygame.image.load('data/L3.png'),pygame.image.load('data/L4.png'),pygame.image.load('data/L2.png'),pygame.image.load('data/L2.png'),pygame.image.load('data/L3.png'),pygame.image.load('data/L4.png'),pygame.image.load('data/L1.png')]
SNATCHR = pygame.image.load('data/SNATCHR.png')
SNATCHL = pygame.image.load('data/SNATCHL.png')
playerSnatchR = False
playerSnatchL = False

# Coordinates
x = 50
y = 420
hitboxPlayer = (x + 5, y + 3, 50, 75)

# Enemies
ENEMYR = [pygame.image.load('data/BR1.png'), pygame.image.load('data/BR2.png'), pygame.image.load('data/BR1.png'), pygame.image.load('data/BR2.png'), pygame.image.load('data/BR1.png'), pygame.image.load('data/BR2.png'), pygame.image.load('data/BR1.png'), pygame.image.load('data/BR2.png'), pygame.image.load('data/BR1.png')]
ENEMYL = [pygame.image.load('data/BL1.png'), pygame.image.load('data/BL2.png'), pygame.image.load('data/BL1.png'), pygame.image.load('data/BL2.png'), pygame.image.load('data/BL1.png'), pygame.image.load('data/BL2.png'), pygame.image.load('data/BL1.png'), pygame.image.load('data/BL2.png'), pygame.image.load('data/BL1.png')]
STICKR = [pygame.image.load('data/STICKR1.png'), pygame.image.load('data/STICKR2.png'), pygame.image.load('data/STICKR3.png'), pygame.image.load('data/STICKR1.png'), pygame.image.load('data/STICKR2.png'), pygame.image.load('data/STICKR3.png'), pygame.image.load('data/STICKR1.png'), pygame.image.load('data/STICKR2.png'), pygame.image.load('data/STICKR3.png')]
STICKL = [pygame.image.load('data/STICKL1.png'), pygame.image.load('data/STICKL2.png'), pygame.image.load('data/STICKL3.png'), pygame.image.load('data/STICKL1.png'), pygame.image.load('data/STICKL2.png'), pygame.image.load('data/STICKL3.png'), pygame.image.load('data/STICKL1.png'), pygame.image.load('data/STICKL2.png'), pygame.image.load('data/STICKL3.png')]
a = 500
b = 410
Eright = False
Eleft = False
stickl = False
stickr = False
enemy_health = 10

BOSSR = [pygame.image.load('data/BOSSR1.png'), pygame.image.load('data/BOSSR2.png'), pygame.image.load('data/GAYABR.png'), pygame.image.load('data/BOSSFIRER.png')]
BOSSL = [pygame.image.load('data/BOSSL1.png'), pygame.image.load('data/BOSSL2.png'), pygame.image.load('data/GAYABL.png'), pygame.image.load('data/BOSSFIREL.png')]
bx = 500
by = 390
Bmove = 5
boss_health = 10
boss_fx = 500
boss_fy = 420
boss_fire = False

# FIRE
FIRER = [pygame.image.load('data/FIRER1.png'), pygame.image.load('data/FIRER2.png'), pygame.image.load('data/FIRER1.png')]
FIREL = [pygame.image.load('data/FIREL1.png'), pygame.image.load('data/FIREL2.png'), pygame.image.load('data/FIREL1.png')]
isFireR = False
isFireL = False
fireMove = False
fx1 = 10
fx2 = 720
fy = 360

# Crusher
CRUSHER = pygame.image.load('data/CRUSHER.png')
cy = -125
cx = 250
isCrush = False
CRUSHEDR = pygame.image.load('data/CRUSHEDR.png')
CRUSHEDL = pygame.image.load('data/CRUSHEDL.png')

# Skulls
skullR = [pygame.image.load('data/SKULLR.png'),pygame.image.load('data/SKULLR1.png')]
skullL = [pygame.image.load('data/SKULLL.png'),pygame.image.load('data/SKULLL1.png')]

# Lifes
LIFE = pygame.image.load('data/life.png')

left = False
right = False
r = False
l = False

# bones (bullet)
bullet = pygame.image.load('data/bone.png')
bulletX = 1000
bulletY = 437
isBulletFireR = False
isBulletFireL = False
bullet_state = "ready"
bulletRight = False
bulletLeft = False

# Score
score_value = 0
timer_font = pygame.font.Font('data/freesansbold.ttf', 18)
score_font = pygame.font.Font('data/freesansbold.ttf', 20)

def isCollision(x, y, cx, cy):
	global crusher_distance
	crusher_distance = math.sqrt(math.pow(cx - x, 2) + math.pow(cy - y, 2))
	if crusher_distance < 80:
		return True
	else:
		return False


def isBossCollision(x, y, bx, by):
	global boss_distance
	boss_distance = math.sqrt(math.pow(bx - x, 2) + math.pow(by - y, 2))
	if boss_distance < 63:
		return True
	else:
		return False

def isBossFireCollision(x, y, boss_fx, boss_fy):
	global boss_fire_distance
	boss_fire_distance = math.sqrt(math.pow(boss_fx - x, 2) + math.pow(boss_fy - y, 2))
	if boss_fire_distance < 40:
		return True
	else:
		return False

def isBulletBossCollision(bx, by, bulletX, bulletY):
	global distance
	bullet_distance = math.sqrt(math.pow(bulletX - bx, 2) + math.pow(bulletY - by, 2))
	if bullet_distance <= 25 and bullet_distance >= 5:
		return True
	else:
		return False

def isFire1Collision(x, y, fx1, fy):
	global fire_distance1
	fire_distance1 = math.sqrt(math.pow(fx1 - x, 2) + math.pow(fy - y, 2))
	if fire_distance1 < 30:
		return True
	else:
		return False

def isFire2Collision(x, y, fx2, fy):
	global fire_distance2
	fire_distance2 = math.sqrt(math.pow(x- fx2, 2) + math.pow(y - fy, 2))
	if fire_distance2 < 45:
		return True
	else:
		return False

def lifes():
	global life
	if life == 3:
		win.blit(LIFE, (125, 0))
		win.blit(LIFE, (150, 0))
		win.blit(LIFE, (175, 0))
	if life == 2:	
		win.blit(LIFE, (125, 0))
		win.blit(LIFE, (150, 0))
	if life == 1:
		win.blit(LIFE, (125, 0))

def isEnemyCollision(x, y, a, b):
	global distance
	distance = math.sqrt(math.pow(x - a, 2) + math.pow(y - b, 2))
	if distance < 63:
		return True
	if distance < 25 and distance > 63:
		return False

def isBulletCollision(a, b, bulletX, bulletY):
	global distance
	bullet_distance = math.sqrt(math.pow(bulletX - a, 2) + math.pow(bulletY - b, 2))
	if bullet_distance <= 25 and bullet_distance >= 5:
		return True
	else:
		return False

def timer():
	timing = timer_font.render("TIME: "+str(time_left), True, (255,255,255))
	win.blit(timing, (720, 8))

def show_score():
	score =  score_font.render(str(score_value), True, (255,255,255))
	win.blit(score, (390, 25))
# Functions for Player, Enemy, Fire, Crusher. etc

def redraw():
	global walkCount, fireCount, enemyWalkCount
	global fx1, fx2
	global life, health,  enemy_health, boss_health
	global fire_collision1, fire_collision2, crusher_collision, cy, distance
	global bulletX, bullet_state, bulletY, bulletRight, bulletLeft
	global score_value, level
	global a, x, bx, by, Bmove, boss_fx, boss_fire, boss_fire_distance, boss_fire_collision

	# Background - RGB
	win.blit(background, (0, 0))

	# To not get the index error!
	if walkCount + 1 >= 27:
		walkCount = 0

	if enemyWalkCount + 1 >= 27:
		enemyWalkCount = 0

	if fireCount + 1 >= 27:
		fireCount = 0

	if score_value >= 50:
		level == 2
	if score_value >= 100:
		level == 3  # The last level

	# ALL ABOUT PLAYER---------------------------------------------------------------------------------------------------------------------

	# Collsion detections-------------------------------------------------------------------------
	crusher_collision = isCollision(x, y, cx, cy)
	if crusher_collision and r:
		health -= 2
		win.blit(CRUSHEDR, (250, 420))
	if crusher_collision and l:
		health -= 2
		win.blit(CRUSHEDL, (270, 420))
	if crusher_collision and not(l) and not(r):
		health -= 2
		win.blit(CRUSHEDR, (250, 420))

	bullet_collision = isBulletCollision(bulletX, bulletY, a, b)
	if bullet_collision:
		score_value += 1
		enemy_health -= 0.2
		bullet_state = "ready"
		if bulletRight:
			a += 15
		elif bulletLeft:
			a -= 15

	if enemy_health <= 0:
		enemy_health = 15

	fire_collision1 = isFire1Collision(x, y, fx1, fy)
	fire_collision2 = isFire2Collision(x, y, fx2, fy)
	if fire_collision1 or fire_collision2:
		health -= 1

	if isJump and right and not(crusher_collision):
		win.blit(RIGHT[0], (x,y))
	if isJump and left and not(crusher_collision):
		win.blit(LEFT[0], (x,y))
	if isJump and crusher_collision:
		if right:
			win.blit(CRUSHEDR, (250, 420))
		if left:
			win.blit(CRUSHEDL, (270, 420))

	if bullet_state == "ready":
		bulletX = x
		bulletY = y
	if bullet_state == "fire" and playerSnatchR:
		bulletX += 15
		bulletRight = True
		bulletLeft = False
	if bullet_state == "fire" and playerSnatchL:
		bulletX -= 15
		bulletLeft = True
		bulletRight = False

	# SNATCH and MAGIC(fire-ball)
	if bullet_state == "fire":
		if playerSnatchR:
			win.blit(SNATCHR, (x,y))
			win.blit(bullet, (bulletX, bulletY))
		if playerSnatchL:
			win.blit(SNATCHL, (x,y))
			win.blit(bullet, (bulletX, bulletY))
	else:
		if playerSnatchR:
			win.blit(RIGHT[0], (x, y))
		if playerSnatchL:
			win.blit(LEFT[0], (x, y))

	if right and not(playerSnatchR) and not(playerSnatchL) and not(isJump) and not(crusher_collision):
		win.blit(playerRight[walkCount // 4], (x, y))
		walkCount += 1

	elif left and not(playerSnatchR) and not(playerSnatchL) and not(isJump) and not(crusher_collision):
		win.blit(playerLeft[walkCount // 4], (x, y))
		walkCount += 1

	if not(right) and not(left) and not(playerSnatchR) and not(playerSnatchL) and not(crusher_collision):
		if r and not(playerSnatchR) and not(playerSnatchL):
			win.blit(RIGHT[walkCount // 9], (x, y))
			walkCount += 1
		elif l and not(playerSnatchR) and not(playerSnatchL):
			win.blit(LEFT[walkCount // 9], (x, y))
			walkCount += 1
		else:
			win.blit(RIGHT[walkCount // 9], (x, y))
			walkCount += 1

	# Crusher
	win.blit(CRUSHER, (cx, cy))

	if isFireR:
		win.blit(FIRER[fireCount // 9], (fx1, 360))
		fx1 += 10
		fireCount += 1
	if isFireL:
		win.blit(FIREL[fireCount // 9], (fx2, 360))
		fx2 -= 10
		fireCount += 1

	# Bullets
	if bulletX >= 800 or bulletX <= 0:
		bulletX = 480
		bullet_state = "ready"

	if isBulletFireL:
		bulletX = x
		bulletX -= 15

	if isBulletFireR:
		bulletX = x
		bulletX += 15


	hitbox = (x + 17, y + 2, 31, 57)
	pygame.draw.rect(win, (175,175,175), (hitbox[0], hitbox[1] - 20, 50, 10))
	pygame.draw.rect(win, (120,120,120), (hitbox[0], hitbox[1] - 20, 50 - (5 * (10 - health)), 10))

	if health <= 0:
		life -= 1
		health = 0

	# Enemies=======================================================================

	if Eright and not(stickl) and not(stickr):
		win.blit(ENEMYR[enemyWalkCount // 3], (a, b))
		enemyWalkCount += 1
	if Eleft and not(stickl) and not(stickr):
		win.blit(ENEMYL[enemyWalkCount // 3], (a, b))
		enemyWalkCount += 1

	if stickr:
		win.blit(STICKR[enemyWalkCount // 3], (a, b))
		enemyWalkCount += 1
	if stickl:
		win.blit(STICKL[enemyWalkCount // 3], (a, b))
		enemyWalkCount += 1

	hitboxEnemy = (a+10, b+5, 29,  52)
	pygame.draw.rect(win, (175,175,175), (hitboxEnemy[0], hitboxEnemy[1] - 20, 50, 10))
	pygame.draw.rect(win, (120,120,120), (hitboxEnemy[0], hitboxEnemy[1] - 20, 50 - (5 * (10 - enemy_health)), 10))

	if health <= 0:
		health = 10
		life -= 1

	health += 0.01
	if health >= 10:
		health = 10

	if life <= 0:
		life = 3
		score_value = 0

	# THE BOSS--------------------------------------------------------------------------------------------------------------------

	bx += Bmove
	if bx >= 734:
		Bmove *= -1
	if bx <= 0:
		Bmove *= -1

	if Bmove == 5 and time_left % 7 > 1 and time_left % 10 > 1:
		win.blit(BOSSL[0], (bx, by))
	elif Bmove == -5 and time_left % 7 > 1 and time_left % 10 > 1:
		win.blit(BOSSR[0], (bx, by))

	# To make BOSS Health bar
	hitboxBoss = (bx+10, by+5, 29,  52)
	pygame.draw.rect(win, (175,175,175), (hitboxBoss[0], hitboxBoss[1] - 20, 50, 10))
	pygame.draw.rect(win, (120,120,120), (hitboxBoss[0], hitboxBoss[1] - 20, 50 - (5 * (10 - boss_health)), 10))

	boss_collision = isBossCollision(x, y, bx, by)
	if boss_collision:
		health -= 2.5

	if time_left % 7 <= 1:

		boss_fire = True

		if Bmove == 5:
			win.blit(BOSSL[1], (bx, by))
		if Bmove == -5:
			win.blit(BOSSR[1], (bx, by))

	elif time_left % 10 <= 1:
		if Bmove == 5:
			win.blit(BOSSR[2], (bx, by))
		if Bmove == -5:
			win.blit(BOSSL[2], (bx, by))

	# Movement of the fire from BOSS's mouth *nati*
	if boss_fire:
		if Bmove == 5:
			boss_fx += 10
			win.blit(BOSSR[3], (boss_fx, 420))
		if Bmove == -5:
			boss_fx -= 10
			win.blit(BOSSL[3], (boss_fx, 420))

	boss_fire_collision = isBossFireCollision(x, y, boss_fx, boss_fy)
	if boss_fire_collision:
		if Bmove == 5:
			x += 20
			health -= 0.1
		elif Bmove == -5:
			x -= 20
			health -= 0.1

	boss_fire_bullet_collision = isBulletBossCollision(bx, by, bulletX, bulletY)
	if boss_fire_bullet_collision:
		boss_health -= 5
		bulletX = x

	if boss_fx >= 790 or boss_fx <= 0 or boss_fire_collision:
		boss_fire = False
	if boss_fire == False:
		boss_fx = bx
	print(health)

	boss_health += 0.2
	if boss_health >= 10:
		boss_health = 10

# Main loop
run = True
while run:
	clock.tick(27)  # FRAMES PER SECOND - FPS
	win.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# To get the list of keypresses
	keys = pygame.key.get_pressed()

	# KEYBOARD BINDINGS
	if keys[pygame.K_RIGHT] and x < 800 - width + 25:
		x  += 5
		left = False
		right = True
	elif keys[pygame.K_LEFT] and x > -25:
		x -= 5
		right = False
		left = True
	else:
		right = False
		left = False

	if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]  and x < 800 - width + 25:
		x  += 7
		left = False
		right = True
	elif keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT] and x > -25:
		x -= 7
		right = False
		left = True

	if keys[pygame.K_x]:
		playerSnatchR = True
		isBulletFireullR = True
		bullet_state = "fire"
	if keys[pygame.K_z]:
		playerSnatchL = True
		isBulletFireullL = True
		bullet_state = "fire"

	if keys[pygame.K_z] and keys[pygame.K_x]:
		playerSnatchR = False
		playerSnatchL = False
	if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] and keys[pygame.K_x]:
		playerSnatchR = False
		playerSnatchL = False

	# KEYS UP
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			r = True
			l = False
		if event.key == pygame.K_LEFT:
			l = True
			r = False

	# Jumping of the skull
	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -13:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.2 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 13

	# Working of the crusher using time module!
	elapsed_time = int(time.time()) + 3
	time_left = int(elapsed_time - start_time)

	# Working of the crusher and skulls!

	# CRUSHER

	if crusher_distance <= 80:
		d = 370
	else:
		d = 392

	if time_left % 10 == 0:
		cy += 20
	if cy >= d or time_left%10 == 3:
		cy -= 30

	if cy < -125:
		cy = -125

	redraw()  # Player, Enemy, Collisions
	lifes()

	# SKULLS
	if time_left%10 == 5:
		win.blit(skullR[1], (0, 320))
		win.blit(skullL[1], (736, 320))
		isFireR = True
		isFireL = True
	else:
		win.blit(skullR[0], (0, 320))
		win.blit(skullL[0], (720, 320))

	if fx1 >= 720 or fire_collision1:
		isFireR = False
		fx1 = 10
	if fx2 <= 22 or fire_collision2:
		isFireL = False
		fx2 = 720

	if fire_collision1:
		x += 35
	if fire_collision2:
		x -= 35

	# Working of the enemy
	enemy_distance_r = x-a
	enemy_distance_l = a-x
	if x > a and enemy_distance_r > 65:
		a += 6
		Eright = True
		Eleft = False
	if x < a and enemy_distance_l > 50:
		a -= 6
		Eright = False
		Eleft = True

	collision = isEnemyCollision(x, y, a, b)

	if collision:
		if Eright:
			stickr = True
			stickl = False
			health -= 0.25

		elif Eleft:
			stickl = True
			stickr = False
			health -= 0.25

	else:
		stickr = False
		stickl = False

	timer()
	show_score()
	pygame.display.update()
