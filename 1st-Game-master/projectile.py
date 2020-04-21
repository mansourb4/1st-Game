import pygame

# Définir la classe qui va gérer le projectile de notre joueur

class Projectile(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.damage = 5