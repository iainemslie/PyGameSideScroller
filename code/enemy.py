import pygame
from os.path import join
from sprites import Sprite


class Enemy(Sprite):
    def __init__(self, position, image_path, groups, z=10):
        self.image = pygame.image.load(join(image_path))
        super().__init__(position, self.image, groups, z)
        self.groups = groups
        self.rect = self.image.get_frect(center=position)
        self.z = z

        self.direction = pygame.Vector2()
        self.speed = 400

    def move(self, dt):
        self.direction.x = -1
        self.rect.x += self.direction.x * self.speed * dt

    def check_offscreen(self):
        if self.rect.x < 0:
            self.kill()

    def update(self, dt):
        self.move(dt)
        self.check_offscreen()
