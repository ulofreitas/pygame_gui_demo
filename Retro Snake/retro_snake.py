"""
Retro snake game created by Ulo Freitas.
Using online tutorial by Kite for educational purposes.
"""
import pygame
import sys
import random


# The code for the snake and its behavior.
class snake(object):
    def __init__(self):
        pass

    def get_current_position(self):
        pass

    def turn(self, point):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass


# The food
class food(object):
    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass


# Screen constants
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# Grid constants
GRID_SIZE = 40
NUM_GRIDS_X = SCREEN_WIDTH / GRID_SIZE
NUM_GRIDS_Y = SCREEN_HEIGHT / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Function which draws the grid
def drawGrid(surface):
    for x in range(int(NUM_GRIDS_X)):
        for y in range(int (NUM_GRIDS_Y)):
            rect_x = x * GRID_SIZE
            rect_y = y * GRID_SIZE
            next_rect = pygame.Rect(rect_x, rect_y, GRID_SIZE, GRID_SIZE)
            color_1 = (82, 148, 62)
            color_2 = (118, 189, 96)
            if ((x + y) % 2 == 1):
                pygame.draw.rect(surface, color_1, next_rect)
            else:
                pygame.draw.rect(surface, color_2, next_rect)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# creating a name for your game
pygame.display.set_caption("Retro Snake Game")
# creating a clock/ framerate
clock = pygame.time.Clock()

surface_width_height = screen.get_size()
surface = pygame.Surface(surface_width_height)
drawGrid(surface)

snake = snake()
food = food()


while True:
    # Event loop (checking for player input)
    for event in pygame.event.get():
        # gets all of the "events" in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw all of our elements! (like the draw function in trinket)
    screen.blit(surface, (0, 0))
    pygame.display.update()  # This will update the screen to the player!
    clock.tick(60) # like our framerate in trinket! tells pygame to to do this while true loop 60 times per second