import pygame

class Pipe():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(ASSET_PATH, "pillar.png"))
        self.rect = self.image.get_rect()
        
    def update(self, delta:float):
        self.rect.move_ip(600 * delta, 0)

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.rect)