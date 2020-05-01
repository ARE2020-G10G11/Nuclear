import pygame
import Mouvements
import Couleurs
import random
import math

pygame.init()
fenetre = pygame.display.set_mode((1100, 800))
fond = pygame.image.load("Images/Cartes/Pays attaquant.png").convert_alpha()
fenetre.blit(fond, (0, 0))
pygame.display.flip()

bleu = (0, 4, 168)
noir = (0, 0, 0)
SWSimp_font = pygame.font.SysFont("SWSimp", 30)


"""
Il y aura 3 phases : la première sera celle où on choisi l'attaquant, la seconde celle où
on choisi qui est attaqué et la dernière celle où on laisse le programme tourner.
"""

phase = 1


"""
On crée un dictionnaire ayant pour clé le nom du pays et pour valeur un tuple contenant les
informations du pays nécessaires : couleur du pays, position à laquelle la bombe partira ou
alors à laquelle la bombe explosera, nombre de bombe, position d'affichage du nombre de
bombe (pas encore utilisé), nombre de bombes nécessaire pourdétruire le pays, coéfficient
permettant de changer progressivement la couleur du pays lorsqu'il est touché, position et
dimension du pays, alliance.
"""

pays = {'Belgique' :           ((255, 237, 208, 255), (492, 226),    0, (  0,   0),    9,    100/9, (  0,   0,  50,  50), 'OTAN'),
        'Canada' :             ((255, 237, 215, 255), (158, 192),    0, (  0,   0), 2990, 100/2990, ( 74,  93, 279, 159), 'OTAN'),
        'Danemark' :           ((255, 237, 204, 255), (510, 208),    0, (  0,   0),  662,  100/662, (  0,   0,  50,  50), 'OTAN'),
        'Etats-Unis' :         ((255, 237, 216, 255), (126, 260), 6450, (130, 719), 2945, 100/2945, (  7, 123, 245, 199), 'OTAN'),
        'France' :             ((255, 237, 214, 255), (486, 244),  300, ( 90, 743),  165,  100/165, (463, 226,  42,  37), 'OTAN'),
        'Islande' :            ((255, 237, 212, 255), (430, 169),    0, (  0,   0),   31,   100/31, (  0,   0,  50,  50), 'OTAN'),
        'Italie' :             ((255, 237, 209, 255), (522, 257),    0, (  0,   0),   90,   100/90, (  0,   0,  50,  50), 'OTAN'),
        'Luxembourg' :         ((255, 237, 207, 255), (497, 230),    0, (  0,   0),    1,    100/1, (  0,   0,  50,  50), 'OTAN'),
        'Norvège' :            ((255, 237, 202, 255), (520, 172),    0, (  0,   0),  115,  100/115, (  0,   0,  50,  50), 'OTAN'),
        'Pays-Bas' :           ((255, 237, 206, 255), (511, 207),    0, (  0,   0),   12,   100/12, (  0,   0,  50,  50), 'OTAN'),
        'Portugal' :           ((255, 237, 210, 255), (445, 272),    0, (  0,   0),   28,   100/28, (  0,   0,  50,  50), 'OTAN'),
        'Royaume-Uni' :        ((255, 237, 213, 255), (473, 219),  215, (152, 767),   74,   100/74, (446, 198,  38,  32), 'OTAN'),
        'Grèce' :              ((255, 237, 191, 255), (553, 270),    0, (  0,   0),   40,   100/40, (  0,   0,  50,  50), 'OTAN'),
        'Turquie' :            ((255, 237, 188, 255), (601, 271),    0, (  0,   0),  235,  100/235, (  0,   0,  50,  50), 'OTAN'),
        'Allemagne' :          ((255, 237, 205, 255), (512, 225),    0, (  0,   0),  107,  100/107, (  0,   0,  50,  50), 'OTAN'),
        'Espagne' :            ((255, 237, 211, 255), (462, 269),    0, (  0,   0),  152,  100/152, (  0,   0,  50,  50), 'OTAN'),
        'République-Tchèque' : ((255, 237, 198, 255), (528, 232),    0, (  0,   0),   24,   100/24, (  0,   0,  50,  50), 'OTAN'),
        'Pologne' :            ((255, 237, 203, 255), (539, 221),    0, (  0,   0),   94,   100/94, (  0,   0,  50,  50), 'OTAN'),
        'Hongrie' :            ((255, 237, 196, 255), (545, 242),    0, (  0,   0),   28,   100/28, (  0,   0,  50,  50), 'OTAN'),
        'Bulgarie' :           ((255, 237, 192, 255), (563, 257),    0, (  0,   0),   33,   100/33, (  0,   0,  50,  50), 'OTAN'),
        'Estonie' :            ((255, 237, 201, 255), (560, 194),    0, (  0,   0),   14,   100/14, (  0,   0,  50,  50), 'OTAN'),
        'Lettonie' :           ((255, 237, 200, 255), (556, 201),    0, (  0,   0),   19,   100/19, (  0,   0,  50,  50), 'OTAN'),
        'Lituanie' :           ((255, 237, 199, 255), (553, 210),    0, (  0,   0),   20,   100/20, (  0,   0,  50,  50), 'OTAN'),
        'Roumanie' :           ((255, 237, 193, 255), (562, 246),    0, (  0,   0),   71,   100/71, (  0,   0,  50,  50), 'OTAN'),
        'Slovaquie' :          ((255, 237, 197, 255), (541, 235),    0, (  0,   0),   15,   100/15, (  0,   0,  50,  50), 'OTAN'),
        'Slovénie' :           ((255, 237, 195, 255), (530, 246),    0, (  0,   0),    6,    100/6, (  0,   0,  50,  50), 'OTAN'),
        'Albanie' :            ((255, 237, 190, 255), (547, 264),    0, (  0,   0),    9,    100/9, (  0,   0,  50,  50), 'OTAN'),
        'Croatie' :            ((255, 237, 194, 255), (532, 251),    0, (  0,   0),   17,   100/17, (  0,   0,  50,  50), 'OTAN'),
        'Monténégro' :         ((255, 237, 189, 255), (539, 254),    0, (  0,   0),    4,    100/4, (  0,   0,  50,  50), 'OTAN'),
        'Chine' :              ((203, 255, 185, 255), (839, 285),  270, (282, 719), 2874, 100/2874, (734, 203, 182, 141), 'OCS'),
        'Russie' :             ((203, 255, 186, 255), (761, 171), 6600, (293, 743), 5129, 100/5129, (562, 101, 406, 161), 'OCS'),
        'Kazakhstan' :         ((203, 255, 184, 255), (703, 232),    0, (  0,   0),  816,  100/816, (  0,   0,  50,  50), 'OCS'),
        'Kirghizistan' :       ((203, 255, 183, 255), (732, 259),    0, (  0,   0),   59,   100/59, (  0,   0,  50,  50), 'OCS'),
        'Tadjikistan' :        ((203, 255, 181, 255), (724, 270),    0, (  0,   0),   43,   100/43, (  0,   0,  50,  50), 'OCS'),
        'Ouzbékistan' :        ((203, 255, 182, 255), (690, 258),    0, (  0,   0),  134,  100/134, (  0,   0,  50,  50), 'OCS'),
        'Inde' :               ((203, 255, 180, 255), (765, 338),  130, (272, 767),  985,  100/985, (725, 282, 104, 114), 'OCS'),
        'Pakistan' :           ((203, 255, 179, 255), (726, 310),  140, (461, 719),  264,  100/264, (697, 278,  53,  53), 'OCS'),
        'Corée du Nord' :      ((255, 191, 196, 255), (913, 256),   15, (433, 743),   36,   100/36, (901, 242,  20,  26), 'COREE DU NORD'),
        'Israël' :             ((191, 238, 255, 255), (598, 304),   80, (518, 767),    7,    100/7, (595, 294,   6,  15), 'ISRAEL')}

position_pays = pygame.image.load("Images/Cartes/positions pays.png")

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        elif event.type == pygame.MOUSEMOTION:

            """
            On créé un dictionnaire contenant les informations nécéssaires selon les phases
            de choix et une liste contenant le nom de chaque pays dans le dictionnaire.
            
            Pour la phase 1, on a besoin des pays possédants la bombe nucléaire et pour la
            seconde phase, on a besoin des pays des autres alliances que celle choisi en
            phase une.
            """
            
            if phase == 1:
                pays_phase = {nom_pays : (couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance) for nom_pays,(couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance) in pays.items() if nb_bombes != 0}
                liste_noms = [nom_pays for nom_pays in pays_phase]
                
            if phase == 2:
                pays_phase = {nom_pays : (couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance) for nom_pays,(couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance) in pays.items() if alliance != alliance_attaquante}
                liste_noms = [nom_pays for nom_pays in pays_phase]

            """
            On parcours le dictionnaire créé précédemment afin de savoir sur quel pays se
            situe la souris.

            tuple(position_pays.get_at((event.pos[0], event.pos[1]))) correspond à la
            couleur RGBA à l'emplacement de la souris sur la carte position_pays.
            
            event.pos[0] correspond à l'abscisse de la souris et event.pos[1] à l'ordonnée.
            """
            
            for nom_pays, infos in pays_phase.items():
                couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance = infos
                nom = SWSimp_font.render(nom_pays, True, bleu)
                x = int(1100/2 - math.floor(len(nom_pays)/2)*20)
                y = 694

                if tuple(position_pays.get_at((event.pos[0], event.pos[1]))) != couleur:
                    fenetre.blit(fond,(0,0))
                    pygame.display.flip()

                elif tuple(position_pays.get_at((event.pos[0], event.pos[1]))) == couleur and nom_pays == liste_noms[-1]:
                    fenetre.blit(nom, (x,y))
                    pygame.display.flip()

                elif tuple(position_pays.get_at((event.pos[0], event.pos[1]))) == couleur:
                    break

            if nom_pays != liste_noms[-1]:
                fenetre.blit(nom, (x,y))
                pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for nom_pays, infos in pays_phase.items():
                couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance = infos

                """
                On affiche la carte de la phase 2.
                """
                
                if tuple(position_pays.get_at((event.pos[0], event.pos[1]))) == couleur:
                    if phase == 1:
                        phase = 2
                        
                        pays_attaquant = nom_pays
                        pays[pays_attaquant] = couleur, pos_bombe, nb_bombes-1, pos_nb_bombe, etat, coef, pos_pays, alliance
                        alliance_attaquante = alliance
                        
                        if alliance == 'OTAN':
                            fond = pygame.image.load('Images/Cartes/OTAN first attaquant.png').convert_alpha()
                            fenetre.blit(fond, (0,0))
                            pygame.display.flip()

                        elif alliance == 'OCS':
                            fond = pygame.image.load('Images/Cartes/OCS first attaquant.png').convert_alpha()
                            fenetre.blit(fond, (0,0))
                            pygame.display.flip()

                        elif alliance == 'COREE DU NORD':
                            fond = pygame.image.load('Images/Cartes/Corée du Nord first attaquant.png').convert_alpha()
                            fenetre.blit(fond, (0,0))
                            pygame.display.flip()

                        elif alliance == 'ISRAEL':
                            fond = pygame.image.load('Images/Cartes/Israël first attaquant.png').convert_alpha()
                            fenetre.blit(fond, (0,0))
                            pygame.display.flip()

                    elif phase == 2:
                        phase = 3
                        pays_attaque = nom_pays

                        fond = pygame.image.load("Images/Cartes/positions pays.png").convert_alpha()
                        pygame.display.flip()

                        attaque = True
                        while attaque:
                            
                            couleur_attaquant, (x_attaquant, y_attaquant), nb_bombes_attaquant, pos_nb_bombe_attaquant, etat_attaquant, coef_attaquant, pos_pays_attaquant, alliance_attaquant = pays[pays_attaquant]
                            couleur_attaque, (x_attaque, y_attaque), nb_bombes_attaque, pos_nb_bombe_attaque, etat_attaque, coef_attaque, pos_pays_attaque, alliance_attaque = pays[pays_attaque]
                            
                            Mouvements.mouvement(x_attaquant, y_attaquant, x_attaque, y_attaque, fond)

                            """
                            On change la couleur du pays attaqué
                            """
                            
                            R, G, B, A = couleur_attaque
                            x, y, l, h = pos_pays_attaque

                            if couleur_attaque != (0, 0, 0, 255):
                                for i in range(x, x+l):
                                    for j in range(y, y+h):
                                        if fond.get_at((i,j)) == couleur_attaque:
                                            new_couleur, dif = Couleurs.TSV_to_RGB(couleur_attaque, coef_attaque)
                                            fond.set_at((i,j), new_couleur)

                                couleur_attaque = new_couleur
                                R, G, B, A = couleur_attaque
                                r, g, b = dif

                            if R-r < 0 or G-g < 0 or B-b < 0:
                                couleur_attaque = (0, 0, 0, 255)

                            fenetre.blit(fond,(0,0))
                            pygame.display.flip()
                            
                            pays[pays_attaque] = (couleur_attaque, (x_attaque, y_attaque), nb_bombes_attaque, pos_nb_bombe_attaque, etat_attaque - 1, coef_attaque, pos_pays_attaque, alliance_attaque)
                            
                            liste_allies = [nom_pays for nom_pays,(couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance) in pays.items() if (alliance == alliance_attaque and nb_bombes != 0 and etat > 0)]

                            if len(liste_allies) == 0:
                                break

                            riposte = random.randint(0, len(liste_allies)-1)

                            attaquant = liste_allies[riposte]
                            couleur, pos_bombe, nb_bombes, pos_nb_bombe, etat, coef, pos_pays, alliance = pays[attaquant]

                            pays[attaquant] = (couleur, pos_bombe, nb_bombes - 1, pos_nb_bombe, etat, coef, pos_pays, alliance)

                            pays_attaque = pays_attaquant
                            pays_attaquant = attaquant

pygame.quit()
