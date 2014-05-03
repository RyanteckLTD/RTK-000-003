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
	else:
		print "right off"

        if keystate[pygame.K_LEFT]:
		print "left"
	else:
		print "left off"
	
	if keystate[pygame.K_DOWN]:
		print "down"
	else:
		print "down off"
	
	if keystate[pygame.K_UP]:
		print "up"
	else:
		print "up off"

	#pygame loop

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
            		exit(0)
	time.sleep(0.01)
