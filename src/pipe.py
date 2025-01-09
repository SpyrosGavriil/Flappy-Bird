import pygame
import os
import random

# Set up the paths relative to the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imgs")

# Load pipe image using the adjusted path
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "pipe.png")))

class Pipe:
    """
    The Pipe class manages the movement, positioning, and collision detection of pipes.
    """
    GAP = 200  # Space between the top and bottom pipe
    VEL = 5  # Speed at which the pipes move

    def __init__(self, x):
        """
        Initializes a new Pipe object at the given x-coordinate.
        """
        self.x = x
        self.height = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)  # Flipped image for the top pipe
        self.PIPE_BOTTOM = PIPE_IMG
        self.passed = False  # Tracks if the bird has passed the pipe
        self.set_height()

    def set_height(self):
        """Randomly sets the height of the top and bottom pipes."""
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        """Moves the pipe towards the left by decreasing the x-coordinate."""
        self.x -= self.VEL

    def draw(self, win):
        """Draws the top and bottom pipes on the screen."""
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        """Checks for collision between the bird and the pipe."""
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # Calculate offsets for pixel-perfect collision detection
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        # Check for overlap between masks
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        # Return True if there was a collision
        return bool(b_point or t_point)
