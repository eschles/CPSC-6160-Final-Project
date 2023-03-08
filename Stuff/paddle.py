# Based on user input
# Entities (Things): Your game should have entities that represent things in the game, such as the player character or objects in the game world.
# Player Character: Your game should have a player character that the player can control.

import pygame
from Stuff import FrameViewer

displayScreen = FrameViewer

#Defining specifics of Paddle
PADDLE_SIZE = PADDLE_WIDTH, PADDLE_HEIGHT = 16, 100
PADDLE_POS = PADDLE_X, PADDLE_Y = 0, (displayScreen.SCREEN_HEIGHT - PADDLE_HEIGHT) / 2
PADDLE_POS_2 = PADDLE_X_2, PADDLE_Y_2 = 784, (displayScreen.SCREEN_HEIGHT - PADDLE_HEIGHT) / 2

paddleColor1 = ('black')
paddleColor2 = ('black')

paddle_speed = 1000 #keeping speed highest for faster control on the paddle

# Create the paddle surface
paddle_surface = pygame.Rect((PADDLE_X, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
paddle_surface_2 = pygame.Rect((PADDLE_X_2, PADDLE_Y_2, PADDLE_WIDTH, PADDLE_HEIGHT))

def paddleDraw(screen):
    paddle = pygame.draw.rect(screen, paddleColor1, paddle_surface)
    paddle_2 = pygame.draw.rect(screen, paddleColor2, paddle_surface_2)
    return paddle, paddle_2

def sharePaddleColor():
    return paddleColor1, paddleColor2