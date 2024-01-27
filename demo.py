import pygame
import pygame_gui
import sys

pygame.init()

WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()

UI_MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((350, 270), (900, 50)),
    manager=UI_MANAGER,
    object_id="main_text_entry"
)

# Delete this once you choose a font!
print("There are all the built-in available Pygame Fonts: ")
print(pygame.font.get_fonts())

# FONTS
verdana_50 = pygame.font.SysFont("verdana", 50)
verdana_100 = pygame.font.SysFont("verdana", 100)

class gameState:
    # add any variables for the character here
    user_response = ""  # store/remember the text response of the user
gs = gameState()

def start_of_story():
    while True:
        SCREEN.fill((80, 160, 250))
        # 60 frames per second / 1000
        # Controls how fast cursor blinks
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # This allows us to see if we hit enter (finished our text entry)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "main_text_entry":
                # We've pressed enter for text entry

                # Update the user_response variable in the player gamestate
                # Hint: event.text contains whatever they just typed
                # TODO
                next_stage()  # move onto the next part of the story

            # Pass current event to manager
            UI_MANAGER.process_events(event)

        # Update every UI event in manager
        UI_MANAGER.update(UI_REFRESH_RATE)

        first_prompt = verdana_50.render("Welcome to this demo game! You can go in four directions: ", True, "black");
        first_prompt_rect = first_prompt.get_rect(topleft=(10, 10))

        option_1 = verdana_50.render("1. North", True, "black")
        option_1_rect = first_prompt.get_rect(topleft=(first_prompt_rect.left, first_prompt_rect.bottom + 10))

        # Can you add options for the other 3 main directions?
        # TODO

        SCREEN.blit(first_prompt, first_prompt_rect)
        SCREEN.blit(option_1, option_1_rect)


        UI_MANAGER.draw_ui(SCREEN)
        pygame.display.update()


def next_stage():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((80, 250, 199))

        your_text = verdana_50.render(f"You typed: {gs.user_response}", True, "black");
        your_text_rect = your_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        SCREEN.blit(your_text, your_text_rect)

        CLOCK.tick(60)

        pygame.display.update()


start_of_story()
