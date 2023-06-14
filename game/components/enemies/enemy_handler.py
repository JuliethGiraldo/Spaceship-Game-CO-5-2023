from game.components.enemies.ship import Ship
from game.components.enemies.sapphire import Sapphire

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Sapphire())

    def update(self):
        for enemy in self.enemies:
            enemy.update()
        for enemy in self.enemies:
            enemy.update()


    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)