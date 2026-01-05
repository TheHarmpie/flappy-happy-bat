import pygame
from pygame import Color
from pygame.locals import QUIT, Rect
import sys

# Initialize pygame
pygame.init()

# Constants
FPS = 60
WHITE = Color(255, 255, 255)

# Screen information
SCREEN_WIDTH = int(1920 * 0.5)
SCREEN_HEIGHT = int(1080 * 0.5)

# Display setup
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURFACE.fill(WHITE)

clock = pygame.time.Clock()

delta = 0
a = 50
def main():
    global delta
    global a
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY_SURFACE.fill(WHITE)

        # draw objects
   


        # Display and tick
        pygame.display.update()
        delta = clock.tick(FPS) / 1000.0  # seconds passed since last frame


        
if __name__ == "__main__":
    main()