import pygame
import math


def mouvement(x_attaquant, y_attaquant, x_attaque, y_attaque, fond):
    pygame.init()
    fenetre = pygame.display.set_mode((1100,800))
    fenetre.blit(fond,(0,0))
    
    rotate = 0

    if x_attaque < x_attaquant and y_attaque < y_attaquant:
        rotate = math.degrees(math.pi - math.atan((y_attaquant - y_attaque)/(x_attaquant - x_attaque)))
                                
    elif x_attaque < x_attaquant and y_attaque > y_attaquant:
        rotate = math.degrees(math.atan((y_attaque - y_attaquant)/(x_attaquant - x_attaque)) + math.pi)
                                
    elif x_attaque > x_attaquant and y_attaque < y_attaquant:
        rotate = math.degrees(-math.atan((x_attaque - x_attaquant)/(y_attaquant - y_attaque)) + math.pi/2)
                                
    elif x_attaque > x_attaquant and y_attaque > y_attaquant:
        rotate = math.degrees(math.atan((x_attaque - x_attaquant)/(y_attaque - y_attaquant)) + 3*math.pi/2)
                                
    bombe_rotate = pygame.transform.rotate(pygame.image.load('Images/bombe.png').convert_alpha(), rotate)
    rect = bombe_rotate.get_rect()
    xb, yb = rect.center
    
    fenetre.blit(bombe_rotate, (x_attaquant - xb, y_attaquant - yb))
    pygame.display.flip()
    
    class MySprite(pygame.sprite.Sprite):
        def __init__(self):
            super(MySprite, self).__init__()

            self.images = []
            self.images.append(bombe_rotate)
            self.images.append(pygame.image.load('Images/explosion/11.png'))
            self.images.append(pygame.image.load('Images/explosion/22.png'))
            self.images.append(pygame.image.load('Images/explosion/33.png'))
            self.images.append(pygame.image.load('Images/explosion/44.png'))
            self.images.append(pygame.image.load('Images/explosion/55.png'))
            self.images.append(pygame.image.load('Images/explosion/66.png'))

            self.index = 0

            self.image = self.images[self.index]
            
            self.x = x_attaquant
            self.y = y_attaquant
            
            self.rect = pygame.Rect(self.x - xb, self.y - yb, 2*xb, 2*yb)

        def update(self):

            if self.index >= len(self.images) - 1:
                return False
            
            elif x_attaque <= x_attaquant and y_attaque <= y_attaquant:
                a = (x_attaquant - x_attaque, y_attaque - y_attaquant)
                x, y = a

                b = -y_attaquant - (y/x)*x_attaquant
                
                if self.x > x_attaque and self.y > y_attaque:
                    self.index = 0
                    self.x -= 10
                    self.y = abs((y/x)*self.x + b)

                    self.rect = (self.x-xb, self.y-yb, 2*xb, 2*yb)        
                    self.image = self.images[self.index]

                elif self.x <= x_attaque and self.y <= y_attaque:
                    self.index += 1
                    self.x = x_attaque
                    self.y = y_attaque

                    self.rect = (self.x - 27.5, self.y - 27.5, 2*xb, 2*yb)        
                    self.image = self.images[self.index]

            elif x_attaque <= x_attaquant and y_attaque >= y_attaquant:
                a = (x_attaquant - x_attaque, y_attaque - y_attaquant)
                x, y = a

                b = -y_attaquant - (y/x)*x_attaquant
                
                if self.x > x_attaque and self.y < y_attaque:
                    self.index = 0
                    self.x -= 10
                    self.y = abs((y/x)*self.x + b)

                    self.rect = (self.x-xb, self.y-yb, 2*xb, 2*yb)        
                    self.image = self.images[self.index]


                elif self.x <= x_attaque and self.y >= y_attaque:
                    self.index += 1
                    self.x = x_attaque
                    self.y = y_attaque

                    self.rect = (self.x - 27.5, self.y - 27.5, 2*xb, 2*yb)         
                    self.image = self.images[self.index]

            elif x_attaque >= x_attaquant and y_attaque <= y_attaquant:
                a = (x_attaque - x_attaquant, y_attaquant - y_attaque)
                x, y = a

                b = -y_attaquant - (y/x)*x_attaquant
                
                if self.x < x_attaque and self.y > y_attaque:
                    self.index = 0
                    self.x += 10
                    self.y = abs((y/x)*self.x + b)

                    self.rect = (self.x-xb, self.y-yb, 2*xb, 2*yb)        
                    self.image = self.images[self.index]

                elif self.x >= x_attaque and self.y <= y_attaque:
                    self.index += 1
                    self.x = x_attaque
                    self.y = y_attaque

                    self.rect = (self.x - 27.5, self.y - 27.5, 2*xb, 2*yb)         
                    self.image = self.images[self.index]

            elif x_attaque >= x_attaquant and y_attaque >= y_attaquant:
                a = (x_attaque - x_attaquant, y_attaquant - y_attaque)
                x, y = a
                
                b = -y_attaquant - (y/x)*x_attaquant
                                    
                if self.x < x_attaque and self.y < y_attaque:
                    self.index = 0
                    self.x += 10
                    self.y = abs((y/x)*self.x + b)

                    self.rect = (self.x-xb, self.y-yb, 2*xb, 2*yb)        
                    self.image = self.images[self.index]

                elif self.x >= x_attaque and self.y >= y_attaque:
                    self.index += 1
                    self.x = x_attaque
                    self.y = y_attaque

                    self.rect = (self.x - 27.5, self.y - 27.5, 2*xb, 2*yb)    
                    self.image = self.images[self.index]
                    
    
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()

    while my_sprite.update() == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        my_group.update()
        my_group.draw(fenetre)
        pygame.display.update()

        fenetre.blit(fond,(0,0))

        clock.tick(100)

    return False
