import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Sapphire(Enemy):
    WIDTH = 50
    HEIGHT = 30
    SPEED_X = 8
    SPEED_Y = 2

    def __init__(self, x, y):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, x, y)
        self.rect = self.image.get_rect()