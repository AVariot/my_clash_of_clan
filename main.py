import pygame
from pygame.locals import *
from game import Game
pygame.init()

# Give the window name
pygame.display.set_caption("my_clash_of_clans")
# Create the window
screen = pygame.display.set_mode((1920, 1080))
# Variable for the while
running = True
# Variable pour indiquer si on bouge la map
moving = False
# Import the Game() instance
game = Game()
# Initialisation des variables permettant de recuperer les coordonners de la
# souris avant et apres l'event de la souris
x = 0
y = 0

while running:
    screen.blit(game.back.background_img, game.back.background_rect)
    pygame.display.flip()
    pygame.display.update()
    # Boucle event
    for event in pygame.event.get():
        # Pour quitter la fenetre, cliquer sur la petite croix
        if event.type == pygame.QUIT:
            running = False
        # Ici pour detecter si la souris est rester appuyer
        elif event.type == MOUSEBUTTONDOWN:
            if game.back.background_rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        # Ici pour actionner les mouvements
        elif event.type == MOUSEMOTION and moving:
            getx = x
            gety = y
            x, y = pygame.mouse.get_pos()
            game.back.moving_background(x, y, getx, gety)


pygame.quit()