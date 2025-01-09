import pygame
import os

# Set up the paths relative to the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, "imgs")

# Load bird images using the adjusted path
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird3.png"))),
]

class Bird:
    """
    The Bird class handles bird movement, animation, and physics.
    """
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25  # Max tilt angle during the jump
    ROT_VELOCITY = 20
    ANIMATION_TIME = 5  # Animation frame rate for flapping

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        """Makes the bird jump by setting an upward velocity."""
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        """Calculates bird's movement based on physics."""
        self.tick_count += 1
        d = self.vel * self.tick_count + 1.5 * self.tick_count**2
        if d >= 16:  # Terminal velocity
            d = 16
        elif d < 0:
            d -= 2  # Adjust slight upward movement

        self.y = self.y + d

        # Tilt the bird based on movement
        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VELOCITY

    def draw(self, win):
        """Draw the bird and handle animation."""
        self.img_count += 1
        # Animation cycling through images
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # Tilt handling for falling animation
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # Rotating the bird image
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        """Return the mask for pixel-perfect collision detection."""
        return pygame.mask.from_surface(self.img)
