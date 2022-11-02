import pygame

class Background():

    def __init__(self):
        self.background_img = pygame.image.load('sprites/background_in_game.jpg')
        self.background_rect = self.background_img.get_rect()
        self.background_scale = 1

    #fonction qui permet de gerer les deplacement du background
    def moving_background(self, x, y, getx, gety):
        if x > getx and self.background_rect.centerx < 1710:
            self.moving_left(x, getx)
        if x < getx and self.background_rect.centerx > 210:
            self.moving_rigth(x, getx)
        if y > gety and self.background_rect.centery < 700:
            self.moving_top(y, gety)
        if y < gety and self.background_rect.centery > 350:
            self.moving_bot(y, gety)

    def moving_left(self, x, getx):
        velocity = 6
        self.background_rect.x += velocity

    def moving_rigth(self, x, getx):
        velocity = 6
        self.background_rect.x -= velocity

    def moving_top(self, y, gety):
        velocity = 3
        self.background_rect.y += velocity

    def moving_bot(self, y, gety):
        velocity = 3
        self.background_rect.y -= velocity