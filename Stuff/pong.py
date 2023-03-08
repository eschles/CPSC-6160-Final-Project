# Iterates through the loop

# Ball Movement:
# Apply contstant velocity in a single direction
# Upon collision, reverse velocity another direction

import pygame, sys
import random
from Stuff import FrameViewer

displayScreen = FrameViewer

# Set the size, starting position, color, and speed of the ball
BALL_SIZE = BALL_WIDTH, BALL_HEIGHT = 15, 15
BALL_RADIUS = 7
BALL_POS = BALL_X, BALL_Y = (displayScreen.SCREEN_WIDTH - BALL_RADIUS), (displayScreen.SCREEN_HEIGHT - BALL_RADIUS)/3
ball_color = ('blue')
ball_speed = 5
BALL_RADIUS = 7
#removed random speed and provided fixed speed
ball_velocity_x = 500 #random.uniform(-2, 2)
ball_velocity_y = 500 #random.uniform(-2, 2)

def pongDraw(screen):
    pong = pygame.draw.circle(screen, ball_color, BALL_POS, BALL_RADIUS)
    return pong

def sharePongColor():
    return ball_color
