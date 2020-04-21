import pygame
pygame.init() #charger les composants de pygame
from game import Game

# Générer la fenetre du jeu
pygame.display.set_caption("KANDYMAN") #Affichage de l'ecran + titre du jeu
screen = pygame.display.set_mode((1080, 720)) #reglage de la taille de l'ecran

# importer et charger l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg') # Charge l'image de l'arrière plan

# Charger le jeu
game = Game()

running = True #variable running qui definit si la fenetre est en cours d'execution

# Boucle tant que cette condition est vraie
while running :

    # Appliquer arrière plan du jeu
    screen.blit(background, (0, -200)) #la fonction blit va permettre de pouvoir injecter l'image à un endroit spécifique de la fenetre

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width(): #and game.player.rect.x < screen.get_width :
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0 : #and game.player.rect.x > screen.get_width() :
        game.player.move_left()

    print(game.player.rect.x)
    #mettre à jour l'ecran
    pygame.display.flip() #.flip() permet de rafraichir l'écran

    #si le joueur ferme cette fenetre
    for event in pygame.event.get() : #boucle qui va verifier les évènements actuels de l'utilisateur
        #vérifier que l'évènement est fermeture de fenetre
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("Fermeture du jeu...")
        # Détécter si le joueur enclenche une touche du clavier
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True #Confirmation qu'une touche est utilisée
        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False #Confirmation que la touche n'est plus utilisée
