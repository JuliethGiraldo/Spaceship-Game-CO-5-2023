import pygame
from game.components.bullets.bullet_handler import BulletHandler
from game.utils.constants import BULLET_SPACESHIP_TYPE, SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.power_type = DEFAULT_TYPE
        self.has_power = False
        self.power_time = 0

    def update(self, user_input, Bullet):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(BulletHandler)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
        elif self.rect.left <= 0:
            self.rect.x = SCREEN_WIDTH - self.rect.width

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.x = 0


    def move_up(self):
        if self.rect.y > (SCREEN_HEIGHT)// 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT)-60:
            self.rect.y += 10

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True

    
    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)

    def set_power_image(self, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (40, 60))

    def set_default_image(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
