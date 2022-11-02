import pygame

class Background():

    def __init__(self):
        self.background_img = pygame.image.load('sprites/background_in_game.jpg')
        self.background_rect = self.background_img.get_rect()

    def moving_background(self, x, y, getx, gety):
        print(x, getx)
        if x > getx:
            self.moving_left()
        if x < getx:
            self.moving_rigth()
        if y > gety:
            self.moving_top()
        if y < gety:
            self.moving_bot()

    
    def moving_left(self):
        self.background_rect.x += 7

    def moving_rigth(self):
        self.background_rect.x -= 7

    def moving_top(self):
        self.background_rect.y += 3

    def moving_bot(self):
        self.background_rect.y -= 3