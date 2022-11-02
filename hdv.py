import pygame
from background import Background

class HDV:

    def __init__(self):
        self.back = Background()
        self.hdv1_img = pygame.image.load('sprites/Clashofclans-HDV-level-1.png')
        self.hdv1_rect = self.hdv1_img.get_rect()
        self.hdv1_zone_plus_x = self.back.background_rect.centerx + 108
        self.hdv1_zone_moin_x = self.back.background_rect.centerx - 108
        self.hdv1_zone_plus_y = self.back.background_rect.centery + 110
        self.hdv1_zone_moin_y = self.back.background_rect.centery - 110
        self.hdv1_hp = 600
        self.hdv_lv = 1
