# Your game should have a game loop that updates the game's state, draws the game on the screen, and handles input events.
# Game Loop: A game loop is a repeating process that controls the flow of a game.
# It updates the game's state, draws the game on the screen, and handles input events.

import pygame
from Stuff import paddle
from Stuff import Controller
from sys import exit
from Stuff import pong
from Stuff import Model

mod = Model

def gameLoop(screen, screenColor, paddle_surface, paddle_surface_2, paddleColor1, paddleColor2, pongBall, pongColor, font):
    # while loop to keep the window available until quit
    while True:
    # get events from the queue & handle events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # calling the paddle movement function
        Controller.move_rect(paddle_surface, paddle_surface_2)

        # Draw background
        screen.blit(screenColor, (0,0))

        # redraw the paddle at the position at which it is moved
        pygame.draw.rect(screen, paddleColor1, (paddle.PADDLE_X, paddle.PADDLE_Y, paddle.PADDLE_WIDTH, paddle.PADDLE_HEIGHT))

        # redraw the paddle at the position at which it is moved
        pygame.draw.rect(screen, paddleColor2, (paddle.PADDLE_X_2, paddle.PADDLE_Y_2, paddle.PADDLE_WIDTH, paddle.PADDLE_HEIGHT))

        #fetch the new position of the ball as it moves
        Controller.updateBallPosition(paddle_surface)

        # draw the ball
        pygame.draw.circle(screen, pongColor, (pong.BALL_X, pong.BALL_Y), pong.BALL_RADIUS)

        # Draw the scores
        paddleScore = font.render("Paddle Hit: " + str(mod.PADDLE_HIT), True, (247,247,0))
        wallHit = font.render("Wall Hit: " + str(mod.WALL_HIT), True, (247,247,0))
        screen.blit(paddleScore, (400 // 4, 200 // 10))
        screen.blit(wallHit, (400 * 5 // 4, 200 // 10))

        # display screen until quit
        pygame.display.update()