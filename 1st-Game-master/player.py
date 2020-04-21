import pygame
pygame.init()

# Création d'une premiere classe qui va représenter le joueur
class Player(pygame.sprite.Sprite) : # pygame.sprite.Sprite afin de représenter la classe en tant que composant graphique du jeu

    def __init__(self):
        super().__init__() # Afin d'initialiser la class sprite
        self.health = 100
        self.max_health = 100 # Afin de récupérer le nombre de points de vie max du joueur
        self.attack = 10
        self.velocity = 5 # Vitesse de déplacement du joueur
        self.jump = 10
        self.image = pygame.image.load('assets/player.png') # Charge l'image du joueur
        self.rect = self.image.get_rect() # Récupère les coordonnées de l'image afin de pouvoir la faire bouger
        self.rect.x = 400 # Abscisse du joueur
        self.rect.y = 500 # Ordonnée du joueur

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.jump

    def move_down(self):
        self.rect.y += self.jump
