import random

"""
On choisi le pays attanquant et le pays qui attaque. Un allié du pays qui a été attaqué, choisi aléatoirement, défend ce dernier en ripostant sur l'attaquant et ainsi de suite.
On pourra ajouter des conditions comme l'état du pays (si il est encore opérationnel) par exemple.
"""
def guerre_nucléaire(pays_attaquant, pays_attaque):

    noms_pays = ['Belgique', 'Canada', 'Danemark', 'Etats-Unis', 'France', 'Islande', 'Italie', 'Luxembourg', 'Norvège', 'Pays-Bas', 'Portugal', 'Royaume-Uni', 'Grèce', 'Turquie', 'Allemagne', 'Espagne', 'République-Tchèque', 'Pologne', 'Hongrie', 'Bulgarie', 'Estonie', 'Lettonie', 'Lituanie', 'Roumanie', 'Slovaquie', 'Slovénie', 'Albanie', 'Croatie', 'Monténégro', 'Chine', 'Russie', 'Kazakhstan', 'Kirghizistan', 'Tadjikistan', 'Ouzbékistan', 'Inde', 'Pakistan', 'Corée du Nord', 'Israël'] 
    pays = {'Belgique' : (0, 'OTAN'), 'Canada' : (0, 'OTAN'), 'Danemark' : (0, 'OTAN'), 'Etats-Unis' : (6450, 'OTAN'), 'France' : (300, 'OTAN'), 'Islande' : (0, 'OTAN'), 'Italie' : (0, 'OTAN'), 'Luxembourg' : (0, 'OTAN'), 'Norvège' : (0, 'OTAN'), 'Pays-Bas' : (0, 'OTAN'), 'Portugal' : (0, 'OTAN'), 'Royaume-Uni' : (215, 'OTAN'), 'Grèce' : (0, 'OTAN'), 'Turquie' : (0, 'OTAN'), 'Allemagne' : (0, 'OTAN'), 'Espagne' : (0, 'OTAN'), 'République-Tchèque' : (0, 'OTAN'), 'Pologne' : (0, 'OTAN'), 'Hongrie' : (0, 'OTAN'), 'Bulgarie' : (0, 'OTAN'), 'Estonie' : (0, 'OTAN'), 'Lettonie' : (0, 'OTAN'), 'Lituanie' : (0, 'OTAN'), 'Roumanie' : (0, 'OTAN'), 'Slovaquie' : (0, 'OTAN'), 'Slovénie' : (0, 'OTAN'), 'Albanie' : (0, 'OTAN'), 'Croatie' : (0, 'OTAN'), 'Monténégro' : (0, 'OTAN'), 'Chine' : (270, 'OCS'), 'Russie' : (6600, 'OCS'), 'Kazakhstan' : (0, 'OCS'), 'Kirghizistan' : (0, 'OCS'), 'Tadjikistan' : (0, 'OCS'), 'Ouzbékistan' : (0, 'OCS'), 'Inde' : (130, 'OCS'), 'Pakistan' : (140, 'OCS'), 'Corée du Nord' : (15, 'COREE DU NORD'), 'Israël' : (80, 'ISRAEL')}

    attaque = True

    while attaque:
        
        nb_bombes_attaquant, alliance_attaquant = pays[pays_attaquant]
        nb_bombes_attaque, alliance_attaque = pays[pays_attaque]

        print('Le pays attaquant est : ' + pays_attaquant + ', il a ' + str(nb_bombes_attaquant) + ' bombes')
        print('Le pays attaqué est : ' + pays_attaque + ', il a ' + str(nb_bombes_attaque) + ' bombes')

        Liste_allies = [p for p,(bombes,alliance) in pays.items() if (alliance == alliance_attaque and bombes != 0)]
        print(len(Liste_allies))

        if len(Liste_allies) == 0:
            break
            
        riposte = random.randint(0, len(Liste_allies) - 1)
            
        attaquant = Liste_allies[riposte]
        nb_bombes, alliance = pays[attaquant]

        zero_bombes = 0

        pays[attaquant] = (nb_bombes - 1, alliance)

        pays_attaque = pays_attaquant
        pays_attaquant = attaquant

    print('Le dernier pays attaqué est la/le-s ' + pays_attaque + ' par la/le-s ' + pays_attaquant)
    
    return pays_attaquant
