#Setup Pygame
from sys import exit
import time
import pygame
import RPi.GPIO as GPIO
pygame.init()
screen = pygame.display.set_mode((480,480))

#Setup the Pi to use BCM mode
GPIO.setmode(GPIO.BCM)
#Output the pins 17,18,22,23

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#Lets create 4 functions

def forwards(state):
	GPIO.output(17,state)
	GPIO.output(22,state)

def backwards(state):
	GPIO.output(18,state)
	GPIO.output(23,state)

def left(state):
	GPIO.output(17,state)
	GPIO.output(23,state)

def right (state):
	GPIO.output(18,state)
	GPIO.output(22,state)

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
