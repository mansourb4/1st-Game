import pygame
pygame.init() #charger les composants de pygame

#creer une premiere classe qui va représenter le joueur
class Player

 #generer la fenetre du jeu
pygame.display.set_caption("Posage Haram") #Affichage de l'ecran + titre du jeu
screen = pygame.display.set_mode((1080, 720)) #reglage de la taille de l'ecran

#importer et charger l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')


running = True #variable running qui definit si la fenetre est en cours d'execution

#boucle tant que cette condition est vraie
while running :

    #appliquer arrier plan du jeu
    screen.blit(background, (0, -200)) #la fonction blit va permettre de pouvoir injecter l'image à un endroit spécifique de la fenetre

    #mettre à jour l'ecran
    pygame.display.flip() #.flip() permet de rafraichir l'écran

    #si le joueur ferme cette fenetre
    for event in pygame.event.get() : #boucle qui va verifier les évènements actuels de l'utilisateur
        #vérifier que l'évènement est fermeture de fenetre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("Fermeture du jeu...")
