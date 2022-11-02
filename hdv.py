import pygame
from background import Background

class HDV:

    def __init__(self):
        self.back = Background()
        self.hdv1_img = pygame.image.load('sprites/Clashofclans-HDV-level-1.png')
        self.hdv1_rect = self.back.background_rect

    def moving_hdv(self, x, y, getx, gety):
        if x > getx and self.hdv1_rect.centerx < 1710:
            self.moving_left_hdv(x, getx)
        if x < getx and self.hdv1_rect.centerx > 210:
            self.moving_rigth_hdv(x, getx)
        if y > gety and self.hdv1_rect.centery < 700:
            self.moving_top_hdv(y, gety)
        if y < gety and self.hdv1_rect.centery > 350:
            self.moving_bot_hdv(y, gety)

    def moving_left_hdv(self, x, getx):
        velocity = 6
        self.hdv1_rect.x += velocity

    def moving_rigth_hdv(self, x, getx):
        velocity = 6
        self.hdv1_rect.x -= velocity

    def moving_top_hdv(self, y, gety):
        velocity = 3
        self.hdv1_rect.y += velocity

    def moving_bot_hdv(self, y, gety):
        velocity = 3
        self.hdv1_rect.y -= velocity  
  