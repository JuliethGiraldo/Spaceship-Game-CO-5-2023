import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Sapphire(Enemy):
    WIDTH = 50
    HEIGHT = 30


    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.SPEED_X = 8
        self.SPEED_Y = 2
        self.INTERVAL = 80