#Setup Pygame
from sys import exit
import time
import pygame
pygame.init()
screen = pygame.display.set_mode((480,480))


while True:
	pygame.display.flip()
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_RIGHT]:
        	print "right"
        if keystate[pygame.K_LEFT]:
		print "left"
	if keystate[pygame.K_DOWN]:
		print "down"
	if keystate[pygame.K_UP]:
		print "up"
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
            		exit(0)
