import random

"""
On choisi le pays attanquant et le pays qui attaque. Un allié du pays qui a été attaqué, choisi aléatoirement, défend ce dernier en ripostant sur l'attaquant et ainsi de suite.
On pourra ajouter des conditions comme l'état du pays (si il est encore opérationnel) par exemple.
"""
def guerre_mondiale(pays_attaquant, pays_attaque):

    noms_pays = ['Belgique', 'Canada', 'Danemark', 'Etats-Unis', 'France', 'Islande', 'Italie', 'Luxembourg', 'Norvège', 'Pays-Bas', 'Portugal', 'Royaume-Uni', 'Grèce', 'Turquie', 'Allemagne', 'Espagne', 'République-Tchèque', 'Pologne', 'Hongrie', 'Bulgarie', 'Estonie', 'Lettonie', 'Lituanie', 'Roumanie', 'Slovaquie', 'Slovénie', 'Albanie', 'Croatie', 'Monténégro', 'Chine', 'Russie', 'Kazakhstan', 'Kirghizistan', 'Tadjikistan', 'Ouzbékistan', 'Inde', 'Pakistan', 'Corée du Nord', 'Israël'] 
    pays = {'Belgique' : (0, 'OTAN'), 'Canada' : (0, 'OTAN'), 'Danemark' : (0, 'OTAN'), 'Etats-Unis' : (6450, 'OTAN'), 'France' : (300, 'OTAN'), 'Islande' : (0, 'OTAN'), 'Italie' : (0, 'OTAN'), 'Luxembourg' : (0, 'OTAN'), 'Norvège' : (0, 'OTAN'), 'Pays-Bas' : (0, 'OTAN'), 'Portugal' : (0, 'OTAN'), 'Royaume-Uni' : (215, 'OTAN'), 'Grèce' : (0, 'OTAN'), 'Turquie' : (0, 'OTAN'), 'Allemagne' : (0, 'OTAN'), 'Espagne' : (0, 'OTAN'), 'République-Tchèque' : (0, 'OTAN'), 'Pologne' : (0, 'OTAN'), 'Hongrie' : (0, 'OTAN'), 'Bulgarie' : (0, 'OTAN'), 'Estonie' : (0, 'OTAN'), 'Lettonie' : (0, 'OTAN'), 'Lituanie' : (0, 'OTAN'), 'Roumanie' : (0, 'OTAN'), 'Slovaquie' : (0, 'OTAN'), 'Slovénie' : (0, 'OTAN'), 'Albanie' : (0, 'OTAN'), 'Croatie' : (0, 'OTAN'), 'Monténégro' : (0, 'OTAN'), 'Chine' : (270, 'OCS'), 'Russie' : (6600, 'OCS'), 'Kazakhstan' : (0, 'OCS'), 'Kirghizistan' : (0, 'OCS'), 'Tadjikistan' : (0, 'OCS'), 'Ouzbékistan' : (0, 'OCS'), 'Inde' : (130, 'OCS'), 'Pakistan' : (140, 'OCS'), 'Corée du Nord' : (15, 'NONE'), 'Israël' : (80, 'NONE')}

    attaque = True

    while attaque:
        
        nb_bombes_attaquant, alliance_attaquant = pays[pays_attaquant]
        nb_bombes_attaque, alliance_attaque = pays[pays_attaque]

        print('Le pays attaquant est : ' + pays_attaquant + ', il a ' + str(nb_bombes_attaquant) + ' bombes')
        print('Le pays attaqué est : ' + pays_attaque + ', il a ' + str(nb_bombes_attaque) + ' bombes')

#        alliance = ''
#        nb_bombes = 0
#        pays_test = set()
        
        #Liste_allies: list[int]
        Liste_allies = [p for p,(_,alliance) in pays.items() if alliance == alliance_attaque ] 
        #Cette liste pose problème pour la Corée du Nord et Israël car ils appartiennent tout les deux à "NONE" donc sont considérés comme alliés 
        #On peut faire un cas particulier pour ces deux pays ou alors mettre des str distincts au niveau de leur "alliance" dans le tuple
        riposte = random.randint(0,len(Liste_allies)-1)
        nb_bombes,_ = pays[Liste_allies[riposte]]
        if nb_bombes != 0: 
            pays[Liste_allies[riposte]] = (nb_bombes - 1, alliance_attaque)        
        
#        while alliance != alliance_attaque or nb_bombes == 0:
#            riposte = random.randint(0,len(pays)-1)
#            pays_test.add(riposte)
#            
#            attaquant = noms_pays[riposte]
#            nb_bombes, alliance = pays[attaquant]
#
#            if len(pays_test) == len(pays):
#                attaque = False

#        pays[attaquant] = (nb_bombes - 1, alliance)

        pays_attaque = pays_attaquant
        pays_attaquant = attaquant

    print('Le dernier pays attaqué est la/le-s ' + pays_attaque + ' par la/le-s ' + pays_attaquant)
    
    return pays[pays_attaquant]




pays = {'Belgique' : (0, 'OTAN'), 'Canada' : (0, 'OTAN'), 'Danemark' : (0, 'OTAN'), 'Etats-Unis' : (6450, 'OTAN'), 'France' : (300, 'OTAN'), 'Islande' : (0, 'OTAN'), 'Italie' : (0, 'OTAN'), 'Luxembourg' : (0, 'OTAN'), 'Norvège' : (0, 'OTAN'), 'Pays-Bas' : (0, 'OTAN'), 'Portugal' : (0, 'OTAN'), 'Royaume-Uni' : (215, 'OTAN'), 'Grèce' : (0, 'OTAN'), 'Turquie' : (0, 'OTAN'), 'Allemagne' : (0, 'OTAN'), 'Espagne' : (0, 'OTAN'), 'République-Tchèque' : (0, 'OTAN'), 'Pologne' : (0, 'OTAN'), 'Hongrie' : (0, 'OTAN'), 'Bulgarie' : (0, 'OTAN'), 'Estonie' : (0, 'OTAN'), 'Lettonie' : (0, 'OTAN'), 'Lituanie' : (0, 'OTAN'), 'Roumanie' : (0, 'OTAN'), 'Slovaquie' : (0, 'OTAN'), 'Slovénie' : (0, 'OTAN'), 'Albanie' : (0, 'OTAN'), 'Croatie' : (0, 'OTAN'), 'Monténégro' : (0, 'OTAN'), 'Chine' : (270, 'OCS'), 'Russie' : (6600, 'OCS'), 'Kazakhstan' : (0, 'OCS'), 'Kirghizistan' : (0, 'OCS'), 'Tadjikistan' : (0, 'OCS'), 'Ouzbékistan' : (0, 'OCS'), 'Inde' : (130, 'OCS'), 'Pakistan' : (140, 'OCS'), 'Corée du Nord' : (15, 'NONE'), 'Israël' : (80, 'NONE')}

#Un exemple de la liste que j'ai créé sur l'OTAN
OTAN = [p for p,(_,alliance) in pays.items() if alliance == 'OTAN' ] 

print(OTAN)
#En bas c'est le problème dont je parle dans le commentaire
NN = [p for p,(_,alliance) in pays.items() if alliance == 'NONE' ] 

print(NN)
