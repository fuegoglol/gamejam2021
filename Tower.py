import pygame
import math
from Pip import Pip
from Utils import Utils

class Tower:
    """
    Tower :\n
    Attibuts :\n
    \tsprite : sprite of the Tower (pygame image)
    \tname : name of the fruit or vegetable (not given in the constructor)  (string)
    \trate : fire rate of the tower (int)
    \tdamage : level of damage of the tower (int)
    \tenergy : level of energy of the tower (int)
    \tcoordinates : the coordinates of the tower (tupple of int) (default (0,0))
    \ttowerRange : the range of fire of the fower (int) (default 5)
    """

    sleepingFrames = [pygame.image.load('assets/particles/zzz.png').subsurface([i*32,0,32,32]) for i in range(3)]
    wateringCan = pygame.image.load('assets/ui/watering_can.png')

    def __init__(self, tower, coordinates):
        """
        Tower : constructor of a Tower\n
        Arguments :\n
        \tsprite : sprite of the Tower (path png)
        \tname : name of the fruit or vegetable (not given in the constructor)  (string)
        \trate : fire rate of the tower (int)
        \tdamage : the level of damage of the tower (int)
        \tcoordinates : the coordinates of the tower (tupple of int) (default (10,10))
        \ttowerRange : the range of fire of the fower (int) (default 5)\n
        Return :\n
        None
        """

        self.coordinates = coordinates
        self.energy = 100
        self.energyMax = self.energy
        self.tick = 0
        self.animTick = 0

        self.sprite = tower['sprite']
        self.name = tower['name']
        self.rate = tower['fire_rate']
        self.damage = tower['damage']
        self.towerRange = tower['range']
        self.energy_consumption = tower['energy_consumption']
        self.max_attack = tower['max_attack']
        self.sleeping_time = tower['sleeping_time']
        self.price = tower['price']
        self.ricochet = tower['ricochet']
        self.path_mine = tower['path_mine']
        self.path_border = tower['path_border']
        self.generator = tower['generator']
        self.poison = tower['poison']
        self.confusing = tower['confusing']

    def draw(self, screen):
        """
        Draw the tower\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """            

        # sprite
        screen.blit(self.sprite, self.coordinates)
        
        x,y = self.coordinates

        #watering can hover
        mx, my = pygame.mouse.get_pos()
        if mx >= x and mx <= x + 32 and my >= y and my <= y + 32:
            pygame.draw.circle(screen, (255, 0, 0, 128), (x + 16, y + 16), self.towerRange, 1)
            if not self.generator and self.energy > 0 and self.energy <= self.energyMax // 2:
                screen.blit(Tower.wateringCan, (mx, my))


        # sleeping
        if self.energy <= 0:
            if self.animTick >= 120:
                self.animTick = 0
                
            screen.blit(Tower.sleepingFrames[self.animTick // 40], (x, y - 10))
            self.animTick += 1

        else: # energy bars
            for n in range(max(2, int((self.energy/self.energyMax) * 5))):
                w = 4
                pygame.draw.rect(screen, Utils.BLUE, (x + w + n*(w + 1), y + 30, w, 3))

    def update(self, enemies):
        pips = []
        water = 0
        if self.energy > 0:
            self.tick += 1
            if self.tick >= 60 // self.rate:
                self.tick = 0
                attack = 0
                if self.generator:
                    water += self.damage
                    self.energy -= self.energy_consumption
                    if self.energy <= 0:
                        self.tick = 0
                    attack += 1
                    
                pos1 = (self.coordinates[0] + 16, self.coordinates[1] + 16)
                for enemy in enemies[::-1]:
                    if attack < self.max_attack:
                        pos2 = (enemy.pos[0] * 32 + enemy.pos_in_tile[0] + 16, enemy.pos[1] * 32 + enemy.pos_in_tile[1] + 16)
                        distance = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

                        if distance < self.towerRange:
                            if self.path_mine and not enemy.fly:
                                enemy.blocked = True
                                enemy.hp -= self.damage
                                self.energy -= self.energy_consumption

                            elif self.path_border:
                                enemy.blocked = True
                                enemy.hp -= self.damage
                                self.energy -= self.energy_consumption
                                
                            elif not self.path_border and not self.path_mine:
                                pips.append(Pip(self.coordinates, enemy, self.damage, self.ricochet, self.poison, self.confusing))
                                self.energy -= self.energy_consumption
                            
                            if self.energy <= 0:
                                self.tick = 0
                            attack += 1
        else:
            if self.tick >= 60 * self.sleeping_time:
                self.tick = 0
                self.energy = self.energyMax

            self.tick += 1
            
        return pips, water
