import pygame
from background import Background

class HDV:

    def __init__(self):
        self.back = Background()
        self.hdv1_img = pygame.image.load('sprites/Clashofclans-HDV-level-1.png')
        self.hdv1_hp = 600
        self.hdv_lv = 1
