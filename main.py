# Your game should have a main script that ties everything together and starts the game loop.
# Main game script: Your game should have a main script that ties everything together
# and starts the game loop.
#scp -r <folder>/ cmurmu@access.computing.clemson.edu <folder location>

import pygame
from Stuff import FrameViewer
from Stuff import GameLoop
from Stuff import paddle
from Stuff import pong

#assigning python files to variable for easy future modification
f = FrameViewer
p = paddle
po = pong

# Initializing the game
pygame.init()

#Draw Game Screen
screen = f.drawDisplay()

#Fetch the Game Screen Color
screenColor = f.shareScreenColor()

#Draw Paddles
paddle, paddle_2 = p.paddleDraw(screen)

#Fetch paddle colors
paddleColor1, paddleColor2 = p.sharePaddleColor()

#Draw pong
pong = po.pongDraw(screen)

#Fetch pong color
pongColor = po.sharePongColor()

font = f.defineFont()

#calling Game loop from the main
GameLoop.gameLoop(screen, screenColor, paddle, paddle_2, paddleColor1, paddleColor2, pong, pongColor, font)



