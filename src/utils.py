import pygame
import os

# Initialize fonts and load background image
pygame.font.init()
WIN_WIDTH = 500
# Set up the paths relative to the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imgs")

# Load background image and set up font
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bg.png")))
STAT_FONT = pygame.font.SysFont("comicsans", 30)

def draw_window(win, birds, pipes, base, score, gen):
    """
    Draws all game elements on the screen, including birds, pipes, base, score, and generation count.
    """
    # Draw background image
    win.blit(BG_IMG, (0, 0))

    # Draw all pipes
    for pipe in pipes:
        pipe.draw(win)

    # Render and draw the score on the top-right corner
    text = STAT_FONT.render(f"Score: {score}", 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - text.get_width() - 10, 10))

    # Render and draw the current generation count on the top-left corner
    text = STAT_FONT.render(f"Gen: {gen}", 1, (255, 255, 255))
    win.blit(text, (10, 10))

    # Draw the base and birds
    base.draw(win)
    for bird in birds:
        bird.draw(win)

    # Update the screen with all changes
    pygame.display.update()
