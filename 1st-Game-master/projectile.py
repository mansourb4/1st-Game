import pygame

# Définir la classe qui va gérer le projectile de notre joueur

class Projectile(pygame.sprite.Sprite) :
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/rasengan.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.damage = 5
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y + 193

    def remove(self):
        # supprimer projectile quand en dehors de l'écran
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        # verifier si projectile plus présent sur écran
        if self.rect.x > 1080 :
            self.remove()
