import pygame
pygame.init()
from player import Player

# Création d'une seconde classe qui va représenter notre jeu
class Game :

    def __init__(self):
        # Générer le joueur
        self.player = Player()
        self.pressed = {} # Associer les touches enclenchées par des valeurs booléennes
