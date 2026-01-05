import pygame
import os
import sys
from pygame import Color
from pygame.locals import K_SPACE, QUIT
from abc import ABC, abstractmethod

WHITE = Color(255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY_SURFACE.fill(WHITE)
FPS = 60
clock = pygame.time.Clock()

class GameObject(ABC):

    @abstractmethod
    def update(self, delta: float):
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface):
        pass


class Bat(GameObject):

    def __init__(self):

        self.image = pygame.image.load("bat-1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)

    def update(self, delta: float):
        
        press_space = pygame.key.get_pressed()
        self.rect.y += 500 * delta
        if press_space[K_SPACE]:
            self.rect.y -= 1000 * delta
        

    def draw(self, surface: pygame.surface):
        image_rect = self.image.get_rect(center=(self.rect.x, self.rect.y))
        surface.blit(self.image, image_rect)


def main():
    delta = 0.0
    bat = Bat()
    objects = [bat]
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update game objects
        for obj in objects:
            obj.update(delta)

        # Draw everything
        DISPLAY_SURFACE.fill(WHITE)  # Clear screen <- try commenting this out!
        for obj in objects:
            obj.draw(DISPLAY_SURFACE)

        # Display and tick
        pygame.display.update()
        delta = clock.tick(FPS) / 1000.0  # seconds passed since last frame


if __name__ == "__main__":
    main()