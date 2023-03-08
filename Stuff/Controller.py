# Controller: Your game should have a controller that controls the game's logic and handles input events.
# Inputs: Your game should handle inputs from the player, such as keyboard or mouse events.
# Event Queue: Your game should have an event queue that stores and processes input events.

from Stuff import paddle
from Stuff import FrameViewer
from Stuff import pong
from Stuff import Model
import pygame.time

p_var = paddle
f_var = FrameViewer
po_var = pong
mod = Model

# function for keyboard input for paddle up and down
def move_rect(paddle_surface, paddle_surface_2):
    #Defining clock and delt_time to make the paddle movement smooth
    clock = pygame.time.Clock()
    delta_time = clock.tick(300) / 1000.0

    #defining key press
    keys = pygame.key.get_pressed()
    
    paddle_surface.y += p_var.paddle_speed * delta_time
    paddle_surface_2.y += p_var.paddle_speed * delta_time
    
    #when Up arrow key or down arrow key is pressed to move the paddle
    if keys[pygame.K_UP] and p_var.PADDLE_Y_2 > 0:
        p_var.PADDLE_Y_2 -= (p_var.paddle_speed * delta_time)
    elif keys[pygame.K_DOWN] and p_var.PADDLE_Y_2 < f_var.SCREEN_HEIGHT - p_var.PADDLE_HEIGHT:
        p_var.PADDLE_Y_2 += (p_var.paddle_speed * delta_time)

    #when "A" (up) key or "Z" (down) key is pressed to move the paddle
    if keys[pygame.K_a] and p_var.PADDLE_Y > 0:
        p_var.PADDLE_Y -= (p_var.paddle_speed * delta_time)
    elif keys[pygame.K_z] and p_var.PADDLE_Y < f_var.SCREEN_HEIGHT - p_var.PADDLE_HEIGHT:
        p_var.PADDLE_Y += (p_var.paddle_speed * delta_time)

def updateBallPosition(paddle_surface):
    #Defining clock and delt_time to make the paddle movement smooth
    clock = pygame.time.Clock()
    delta_time = clock.tick(500) / 1000.0

    # Update ball position based on velocity and delta_time
    po_var.BALL_X += po_var.ball_velocity_x * delta_time
    po_var.BALL_Y += po_var.ball_velocity_y * delta_time

    # Check if ball hits a wall and reverse direction if necessary
    if po_var.BALL_X < po_var.BALL_RADIUS or po_var.BALL_X > (f_var.SCREEN_WIDTH - po_var.BALL_RADIUS):
        # Keep a score of the number of times ball touches the wall
        #if po_var.BALL_X < po_var.BALL_RADIUS or po_var.BALL_X > (f_var.SCREEN_WIDTH - po_var.BALL_RADIUS):
            mod.WALL_HIT += 1
        
        # reverse the ball direction for left and right wall
            po_var.ball_velocity_x = -po_var.ball_velocity_x

    if po_var.BALL_Y < po_var.BALL_RADIUS or po_var.BALL_Y > (f_var.SCREEN_HEIGHT - po_var.BALL_RADIUS):
        po_var.ball_velocity_y = -po_var.ball_velocity_y
        
    # Check if ball hits paddle 1 or paddle 2 and reverse direction (both x & y) if necessary
    if (po_var.BALL_X < (p_var.PADDLE_WIDTH + po_var.BALL_RADIUS) and po_var.BALL_Y > (p_var.PADDLE_Y) and po_var.BALL_Y < (p_var.PADDLE_Y + p_var.PADDLE_HEIGHT)) or ((po_var.BALL_X > (f_var.SCREEN_WIDTH - p_var.PADDLE_WIDTH - po_var.BALL_RADIUS)) and (po_var.BALL_Y > (p_var.PADDLE_Y_2)) and (po_var.BALL_Y < (p_var.PADDLE_Y_2 + p_var.PADDLE_HEIGHT))):
        # Keep a score of the number of times ball touches the paddle
        mod.PADDLE_HIT += 1

        # reverse ball direction
        po_var.ball_velocity_x = -po_var.ball_velocity_x
        po_var.ball_velocity_y = -po_var.ball_velocity_y
