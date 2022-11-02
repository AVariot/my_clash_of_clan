import pygame
from background import Background
from hdv import HDV

class Game:

    def __init__(self):
        self.back = Background()
        self.hdv = HDV()

    # Pour faire les modifs du jeu pendant le jeu
    def update(self, screen):
        screen.blit(self.back.background_img, self.back.background_rect)
        screen.blit(self.hdv.hdv1_img, self.back.background_rect.center)
        pygame.display.flip()
        pygame.display.update()
