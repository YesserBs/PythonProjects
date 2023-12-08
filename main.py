import pygame
import sys
import os
from random import randint

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 371, 750

# Taille de l'image
taille_image = (371, 750)

# Couleurs
blanc = (255, 255, 255)
rouge = (255, 0, 0)
i = 0
somme = 0
coups = 0
pas = 48

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Fenêtre Pygame")

# Charger l'image depuis le dossier "templates"
dossier_templates = "templates"
chemin_template1 = os.path.join(dossier_templates, "template1.jpg")
chemin_template2 = os.path.join(dossier_templates, "template2.jpg")
chemin_pion = os.path.join(dossier_templates, "pion.png")

# Vérifier si l'image existe
if os.path.exists(chemin_template1):
    # Charger l'image
    template1 = pygame.image.load(chemin_template1)
    template2 = pygame.image.load(chemin_template2)
    pion_img = pygame.image.load(chemin_pion)
    # Redimensionner l'image à la taille spécifiée
    template1 = pygame.transform.scale(template1, taille_image)
    template2 = pygame.transform.scale(template2, taille_image)
    pion_img = pygame.transform.scale(pion_img, (100, 56))
    templates = [template1, template2]
else:
    print("L'image template2.jpg n'a pas été trouvée.")
    pygame.quit()
    sys.exit()

# Position de l'image (au coin supérieur gauche de la fenêtre)
position_template1 = (0, 0)
prison = 480
position_pion = [140, prison]

# Dimensions et position du rectangle rouge
largeur_rectangle, hauteur_rectangle = 200, 60
position_rectangle = (85, 507)

# Dimensions et position du rectangle du bouton de retour
largeur_boutton_retour, hauteur_boutton_retour = 50, 30
position_boutton_retour = (10, 10)

largeur_de, hauteur_de = 100, 100
position_de = (132, 575)

# Police pour le texte "Hello world"


# Boucle principale du programme
ch = "Lancez le dé!"
def lancer_de():
    return randint(1, 6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifie si le clic de la souris est dans la zone du rectangle rouge
            x, y = event.pos
            if (
                position_rectangle[0] <= x <= position_rectangle[0] + largeur_rectangle
                and position_rectangle[1] <= y <= position_rectangle[1] + hauteur_rectangle
                and i == 0
            ):
                i = 1
            elif (
                position_boutton_retour[0] <= x <= position_boutton_retour[0] + largeur_boutton_retour
                and position_boutton_retour[1] <= y <= position_boutton_retour[1] + hauteur_boutton_retour
                and i == 1
            ):
                i = 0
                somme = 0
                ch = "Lancez le dé!"
                coups = 0
                position_pion[1] = prison


            elif (
                position_de[0] <= x <= position_de[0] + largeur_de
                and position_de[1] <= y <= position_de[1] + hauteur_de
                and i == 1
            ):
                if (somme != 9):
                    l = lancer_de()
                    ch = str(l)
                    # Lancé
                    coups += 1
                    print(l, somme)
                    if (position_pion[1] == prison and l == 6 and somme != 9):
                        position_pion[1] -= pas
                    elif (position_pion[1] != prison and (somme + l) <= 9):
                        # print("Here", somme, l)
                        if ((somme + l) <= 9):
                            somme += l
                        position_pion[1] -= pas * l
                else:
                    #ch = "Tu as gagné en " + str(coups) + " coups!"
                    print("Tu a gagné en", coups, "coups")

        elif event.type == pygame.MOUSEMOTION:
            # Afficher curseur
            x, y = event.pos
            #print(f"Position de la souris : ({x}, {y})")
        font1 = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 23)
        if (somme == 9):
            ch = str(l) + " Tu as gagné!"
        coups_surface = font1.render(ch, True, blanc)
        coups_rect = coups_surface.get_rect(center=(largeur // 2, hauteur - 33))

        ch2 = "Coups: " + str(coups)
        resultat_surface = font2.render(ch2, True, blanc)
        resultat_rect = resultat_surface.get_rect(center=(302, 27))

    # Effacer la fenêtre
    fenetre.fill(blanc)

    # Afficher l'image template1 au coin supérieur gauche de la fenêtre
    fenetre.blit(templates[i], position_template1)


    # Dessiner le rectangle rouge
    #pygame.draw.rect(fenetre, rouge, (position_rectangle[0], position_rectangle[1], largeur_rectangle, hauteur_rectangle))

    # Afficher le texte "Hello world"
    if i == 1:
        fenetre.blit(coups_surface, coups_rect)
        fenetre.blit(resultat_surface, resultat_rect)
        fenetre.blit(pion_img, position_pion)

    pygame.display.flip()
