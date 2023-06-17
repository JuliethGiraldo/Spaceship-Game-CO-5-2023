import pygame
import random

from game.utils.constants import SCREEN_WIDTH

class Power:
    POWER_WIDTH = 30
    POWER_HEIGHT = 30

    def __init__(self, image ,type):
       self.image = image
       self.type = type
       self.image = pygame.transform