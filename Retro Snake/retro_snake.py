"""
Retro snake game created by Ulo Freitas.
Using online tutorial by Kite for educational purposes.
"""
import pygame
import sys
import random

gameover = False
# The code for the snake and its behavior.
# The snake is made up of it's length, a list of the coordinates
# of its body blocks, and the direction it's heading in.
class snake(object):
    def __init__(self):
        self.length = 10

        # positions is a lsit tracking the coordinates (x, y) of all the
        # body blocks of the snake. New blocks are added to the end.
        starting_x = SCREEN_WIDTH / 2
        starting_y = SCREEN_HEIGHT / 2
        starting_position = (starting_x, starting_y)
        self.positions = [starting_position]

        self.direction = UP
        self.color = (17, 24, 47)
        self.draw(background)

    def get_current_position(self):
        return self.positions[0]

    # Point represents one of the four directions the snake can turn in
    def turn(self, point):
        # If the snake is moving UP, we cannot turn DOWN
        if self.direction == UP:
            if point == DOWN:
                return
            else:
                self.direction = point
        # If the snake is moving DOWN, we cannot turn UP
        elif self.direction == DOWN:
            if point == UP:
                return
            else:
                self.direction = point
        # If the snake is moving LEFT, we cannot turn RIGHT
        elif self.direction == LEFT:
            if point == RIGHT:
                return
            else:
                self.direction = point
        # If the snake is moving RIGHT, we cannot turn LEFT
        elif self.direction == RIGHT:
            if point == LEFT:
                return
            else:
                self.direction = point


    def move(self):
        print ("in move!")
        print (f"positions: {self.positions}")
        cur_head = self.get_current_position()
        cur_x = cur_head[0]
        cur_y = cur_head[1]
        x = self.direction[0]
        y = self.direction[1]
        # new_x = cur_x + ((x * GRID_SIZE) % SCREEN_WIDTH)
        # new_y = cur_y + ((y * GRID_SIZE) % SCREEN_HEIGHT)

        new = ((cur_head[0]+(x*GRID_SIZE)), (cur_head[1]+(y*GRID_SIZE)))
        # new = (((cur_head[0]+(x*GRID_SIZE))%SCREEN_WIDTH), (cur_head[1]+(y*GRID_SIZE))%SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.gameover()
        elif (self.outOfBounds() == True):
            print ("END OF GAME!! out of bounds!")
            self.gameover()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

        # new_position = (new_x, new_y)
        # if len(self.positions) > 2 and new_position in self.positions[2:]:
        #     self.reset()
        # else:
        #     self.positions.insert(0, new_position)
        #     if len(self.positions) > self.length:
        #         self.positions.pop()
        # print (f"positions: {self.positions}")

        ## TODO ADD CHECK FOR IF THE SNAKE IS MORE THAN 2

    def gameover(self):
        print ("in gameover()")
        gameover = True
        gameover_box = pygame.Rect(0, 0, (SCREEN_WIDTH - 120), 80)
        gameover_box.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        pygame.draw.rect(background, (255, 255, 255), gameover_box)
        self.direction = GAMEOVER

    def reset(self):
        self.length = 1

        # positions is a lsit tracking the coordinates (x, y) of all the
        # body blocks of the snake. New blocks are added to the end.
        starting_x = SCREEN_WIDTH / 2
        starting_y = SCREEN_HEIGHT / 2
        starting_position = (starting_x, starting_y)
        self.positions = [starting_position]

        self.direction = UP

    def draw(self, background):
        # print (f"\nIn draw! positions = {self.positions}")
        for position in self.positions:
            block = pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(background, self.color, block)
            pygame.draw.rect(background, (0, 0, 0), block, 1)

    def outOfBounds(self):
        head = self.positions[0]
        head_x = head[0]
        head_y = head[1]
        # print (f"out of bounds! head_x: {head_x}, head_y: {head_y}")
        if (head_x < 0 or head_x > SCREEN_WIDTH):
            return True
        elif (head_y < 0 or head_y > SCREEN_HEIGHT):
            return True
        else:
            return False


# The food
class food(object):
    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, background):
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
GAMEOVER = (0, 0)

# Function which draws the grid
def drawGrid(background):
    for x in range(int(NUM_GRIDS_X)):
        for y in range(int (NUM_GRIDS_Y)):
            rect_x = x * GRID_SIZE
            rect_y = y * GRID_SIZE
            next_rect = pygame.Rect(rect_x, rect_y, GRID_SIZE, GRID_SIZE)
            color_1 = (162, 209, 73)
            color_2 = (170, 215, 82)
            if ((x + y) % 2 == 1):
                pygame.draw.rect(background, color_1, next_rect)
            else:
                pygame.draw.rect(background, color_2, next_rect)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# creating a name for your game
pygame.display.set_caption("Retro Snake Game")
# creating a clock/ framerate
clock = pygame.time.Clock()

surface_width_height = screen.get_size()
background = pygame.Surface(surface_width_height)
drawGrid(background)

snake = snake()
food = food()

count = 0

while True:
    # Event loop (checking for player input)
    for event in pygame.event.get():
        # gets all of the "events" in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if gameover:
                print (f"event loop: GAME OVER {count}")
                if event.type == pygame.K_SPACE or event.type == pygame.K_r:
                    print ("GAME OVER RESTART")
                    gameover = False
                    snake.reset()

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake.turn(UP)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake.turn(DOWN)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake.turn(RIGHT)
    #         elif event.type == pygame.K_SPACE or event.type == pygame.K_r:
    #             print ("GAME OVER RESTART")
    #             gameover = False
    #             snake.reset()
    #             drawGrid(background)
    #             snake.move()
    #             snake.draw(background)

    # Draw all of our elements! (like the draw function in trinket)
    drawGrid(background)
    if (gameover == False):
        print ("\nGAME NOT OVER")
        snake.move()
        snake.draw(background)
    # else:
    #     print ("\nelse")
    #     for event in pygame.event.get():
    #         print ("event loop")
    #         # gets all of the "events" in pygame
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()
    #         elif event.type == pygame.K_SPACE or event.type == pygame.K_r:
    #             print ("GAME OVER RESTART")
    #             gameover = False
    #             snake.reset()
    #             drawGrid(background)
    #             snake.move()
    #             snake.draw(background)
    screen.blit(background, (0, 0))
    pygame.display.update()  # This will update the screen to the player!
    clock.tick(5) # like our framerate in trinket! tells pygame to to do this while true loop 60 times per second