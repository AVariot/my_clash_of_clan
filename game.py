import pygame
from background import Background


class Game:

    def __init__(self):
        self.back = Background()

    def update(self, screen):
        screen.blit(self.back.background_img, self.back.background_rect)
        pygame.display.flip()
        pygame.display.update()
