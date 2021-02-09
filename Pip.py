import pygame
import math

class Pip:
    """
    Class Pip :\n
    Attibuts :\n
    \tcoordinates : the coordinates of the pip (int) (default (10,10))
    \tsize : size of the pip (int) (default 1)
    \tdamage : damage of the pip (int) (default 1)
    """

    def __init__(self, coordinates, enemy, size = 1, damage = 1):
        """
        Constructor of the pips\n
        Arguments :\n
        \tcoordinates : the coordinates of the pip (int) (default (10,10))
        \tsize : size of the pip (int) (default 1)
        \tdamage : damage of the pip (int) (default 1)\n
        Return :\n
        None
        """
        self.coordinates = coordinates
        self.__enemy = enemy
        self.__size = size
        self.__damage = damage
        self.__surface = pygame.image.load('assets/tilesets/bullet.png').subsurface(((14, 14), (4, 4)))
    
    def move(self):
        """
        Move the pip with the direction given in the constructor
        """
        pos1 = self.coordinates
        pos2 = (self.__enemy.pos[0] * 32 + self.__enemy.pos_in_tile[0], self.__enemy.pos[1] * 32 + self.__enemy.pos_in_tile[1])
        delta1 = pos2[0] - pos1[0]
        delta2 = pos2[1] - pos1[1]
        distance = math.sqrt((delta1)**2 + (delta2)**2)
        angle = math.atan2(delta2, delta1)
        return (self.coordinates[0] + math.cos(angle) * 10, self.coordinates[1] + math.sin(angle) * 10)

    def draw(self, screen):
        """
        Attack a position\n
        Parameters :\n
        \tscreen : the pygame screen\n
        Return :\n
        None
        """

        screen.blit(self.__surface, self.coordinates)
