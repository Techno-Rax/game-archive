import pygame
import math
import time

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,500))
font = pygame.font.Font('freesansbold.ttf', 12)


t = 0
pressed = False

scale_img = pygame.image.load("scale.png")
theta = 0

blue = (48, 184, 179)
white = (255,255,255)
yellow = (196, 212, 23)

# Variables & Constants
g = 10
u = 0
ax = 0
ay = -g
x, y = 38, 456

def draw():
	global length
	screen.blit(scale_img, (0, 0))
	ball = pygame.draw.rect(screen, blue, (x, y, 15, 15))

	if pressed == False:
		line = pygame.draw.line(screen, blue, (52, 457), (mx, my), 1)
	

def write():
	global length
	angle = font.render(f'Angle: {round(theta*(180/math.pi))}°', True, blue)
	screen.blit(angle, (650,50))
	vel = font.render(f'Velocity: {u}', True, blue)
	screen.blit(vel, (650,80))
	velCOMP = font.render(f'V: (x: {round(ux)}, y: {round(vy)})', True, blue)
	screen.blit(velCOMP, (650,110))
	time = font.render(f'Time: {round(t)}', True, blue)
	screen.blit(time, (650,140))
	time = font.render(f'(x,y): ({round(x)},{round(y)})', True, blue)
	screen.blit(time, (650,170))
	if y >= 458:
		TOF = font.render(f'TOF: {round(T)}', True, yellow)
		screen.blit(TOF, (650,200))
		RANGE = font.render(f'RANGE: {round(R)}', True, yellow)
		screen.blit(RANGE, (650,230))
		HEIGHT = font.render(f'MAX H: {round(Hmax)}', True, yellow)
		screen.blit(HEIGHT, (650,260))

def move():
	global x,y,ux,vy, pressed, t, elapsed, start

	if pressed:
		if ux <= 3:
			x += int(ux)
		if ux > 3:
			x += int(ux)/5
			
		y += -int(vy)/5

run = True
while run:

	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pressed = True


	mx, my = pygame.mouse.get_pos()

	if pressed == False:
		u = round(math.sqrt(math.pow(mx-52, 2) + math.pow(my-457, 2)))//3
		start = time.time()
		
		try:
			theta = math.atan((457-my)/(mx-52))
		except ZeroDivisionError:
			theta = (math.pi)/2

	if pressed:
		elapsed = time.time()
		t = elapsed - start

	uy = u*math.sin(theta)
	vy = (uy + ay*t)
	ux = (u*math.cos(theta))

	T = 2*u*math.sin(theta)/g
	Hmax = u*u*(math.sin(theta))**2/(2*g)
	R = u*u*math.sin(2*theta)/g

	if y >= 458:
		y = 458

	draw()
	write()
	move()
	
	pygame.display.update()
