import pygame


class Missile(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.image = pygame.Surface((4, 4))
        self.image.fill('lightblue')
        self.rect = self.image.get_frect(center=position)

        self.direction = pygame.Vector2()
        self.direction.x = 1
        self.speed = 400

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt

    def update(self, dt):
        self.move(dt)
