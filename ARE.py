import pygame

pygame.init()
fenetre = pygame.display.set_mode((1100,800))
fond = pygame.image.load("Pays attaquant.jpg").convert_alpha()
fenetre.blit(fond,(0,0))
pygame.display.flip()

bleu = (0,4,168)
arial_font = pygame.font.SysFont("SWSimp",20)

etats_unis = [((111,127),(126,137)),((87,123),(114,145)),((69,125),(104,149)),((48,134),(94,156)),((18,146),(55,162)),((9,163),(39,170)),((58,156),(89,163)),((76,164),(89,175)),((67,202),(77,215)),((68,216),(152,231)),((152,220),(180,231)),((52,231),(193,245)),((41,245),(85,284)),((63,284),(85,292)),((85,245),(181,299)),((181,245),(195,291)),((195,250),(205,288)),((205,247),(221,268)),((221,245),(232,260)),((232,241),(240,254)),((240,235),(251,246)),((102,299),(114,315)),((114,299),(150,308)),((164,299),(178,320))]
EU = set()

for position in etats_unis:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    EU.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            EU.add((xh+x,yh+y))

royaume_uni = [((445,210),(460,222)),((462,196),(472,207)),((463,207),(479,215)),((463,215),(483,226))]
RU = set()

for position in royaume_uni:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    RU.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            RU.add((xh+x,yh+y))

france = [((479,227),(488,233)),((488,228),(492,233)),((492,230),(495,233)),((464,232),(473,243)),((472,233),(491,259)),((469,243),(474,256)),((475,257),(488,261)),((492,233),(499,256)),((498,233),(501,240)),((499,246),(502,256))]
FR = set()

for position in france:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    FR.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            FR.add((xh+x,yh+y))

israel = [((596,295),(600,311))]
IS = set()

for position in israel:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    IS.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            IS.add((xh+x,yh+y))

coree_du_nord = [((911,243),(920,250)),((907,247),(910,249)),((905,250),(918,256)),((903,254),(904,256)),((902,257),(918,264)),((906,265),(915,267))]
CN = set()

for position in coree_du_nord:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    CN.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            CN.add((xh+x,yh+y))

russie = [((564,149),(593,162)),((567,163),(581,173)),((601,153),(608,158)),((618,124),(631,147)),((630,122),(649,129)),((639,118),(653,123)),((681,103),(725,111)),((567,174),(892,202)),((570,203),(697,211)),((576,212),(641,225)),((588,225),(635,229)),((604,229),(640,252)),((620,252),(642,256)),((632,256),(644,261)),((641,211),(678,800)),((699,201),(849,214)),((733,213),(793,222)),((804,214),(850,221)),((581,169),(924,175)),((892,175),(911,179)),((597,159),(922,169)),((617,153),(681,159)),((659,134),(674,154)),((674,134),(683,153)),((682,134),(952,158)),((691,127),(897,134)),((698,115),(750,127)),((896,130),(950,134)),((951,132),(968,144)),((951,148),(966,159)),((922,158),(962,166)),((937,166),(952,189)),((951,177),(960,196)),((959,184),(967,204)),((892,193),(911,202)),((872,201),(915,212)),((884,212),(923,220)),((913,219),(928,242))]
RUS = set()

for position in russie:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    RUS.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            RUS.add((xh+x,yh+y))

chine = [((850,204),(871,213)),((852,214),(883,226)),((884,222),(912,242)),((885,242),(901,261)),((863,232),(867,236)),((854,236),(867,243)),((849,244),(866,250)),((867,226),(884,336)),((872,336),(884,343)),((884,270),(899,339)),((899,284),(905,332)),((906,296),(914,326)),((834,250),(866,334)),((824,307),(829,311)),((781,244),(795,254)),((769,234),(780,254)),((765,233),(768,304)),((769,253),(833,307)),((782,307),(807,311)),((759,228),(768,233)),((759,233),(766,304)),((751,237),(760,245)),((749,246),(759,282)),((741,260),(748,279)),((734,264),(742,272))]
CH = set()

for position in chine:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    CH.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            CH.add((xh+x,yh+y))

inde = [((814,325),(821,334)),((808,309),(823,324)),((796,313),(807,322)),((791,319),(801,345)),((781,319),(791,357)),((758,317),(781,385)),((765,385),(775,394)),((759,306),(764,317)),((750,299),(758,366)),((744,300),(751,356)),((727,330),(744,343)),((734,318),(744,331)),((738,313),(744,318)),((740,307),(744,313)),((741,287),(748,299)),((748,284),(756,299))]
IN = set()

for position in inde:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    IN.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            IN.add((xh+x,yh+y))

pakistan = [((729,280),(747,286)),((729,287),(739,312)),((740,300),(743,306)),((723,292),(728,302)),((718,300),(722,302)),((712,303),(733,325)),((734,313),(737,317)),((720,325),(733,329)),((703,310),(711,325)),((699,310),(702,315))]
PA = set()

for position in pakistan:
    haut, bas = position
    xh, yh = haut
    xb, yb = bas

    PA.add((xh,yh))

    for x in range(xb-xh+1):
        for y in range(yb-yh+1):
            PA.add((xh+x,yh+y))
            
pays_bombe = {'Etats-Unis' : EU, 'Royaume-Uni' : RU, 'France' : FR, 'Russie' : RUS, 'Chine' : CH, 'Corée du Nord' : CN, 'Inde' : IN, 'Pakistan' : PA, 'Israël' : IS}
nom_pays = {'Etats-Unis' : (77,248), 'Royaume-Uni' : (355,179), 'France' : (448,260), 'Russie' : (719,162), 'Chine' : (797,272), 'Corée du Nord' : (905,270), 'Inde' : (747,323), 'Pakistan' : (630,270), 'Israël' : (576,315)}


launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

        elif event.type == pygame.MOUSEMOTION:
            for pays, positions in pays_bombe.items():
                nom = arial_font.render(pays, True, bleu)

                if (event.pos[0], event.pos[1]) not in positions:
                    fenetre.blit(fond,(0,0))
                    pygame.display.flip()

                elif (event.pos[0], event.pos[1]) in positions and pays == 'Israël':
                    fenetre.blit(nom,nom_pays[pays])
                    pygame.display.flip()
                    
                elif (event.pos[0], event.pos[1]) in positions:
                    break

            if pays != 'Israël':
                fenetre.blit(nom,nom_pays[pays])
                pygame.display.flip()
