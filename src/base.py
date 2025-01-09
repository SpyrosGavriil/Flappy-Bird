import pygame
import os

# Set up the paths relative to the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imgs")

# Load base image using the adjusted path
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "base.png")))

class Base:
    """
    The Base class handles the scrolling ground animation.
    """
    VEL = 5  # Speed at which the ground moves
    WIDTH = BASE_IMG.get_width()  # Width of the base image
    IMG = BASE_IMG

    def __init__(self, y):
        """
        Initializes the base with its y-coordinate.
        """
        self.y = y
        self.x1 = 0  # Starting x-coordinate for the first base image
        self.x2 = self.WIDTH  # Starting x-coordinate for the second base image (used for seamless looping)

    def move(self):
        """Moves the base to create a scrolling effect."""
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        # If the first base image goes off screen, reset it behind the second
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        # If the second base image goes off screen, reset it behind the first
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        """Draws both base images on the screen to create a seamless scrolling effect."""
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
