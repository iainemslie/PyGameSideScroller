from settings import *
from sprites import Sprite


class Missile(Sprite):
    def __init__(self, position, image_path, groups, z=10):
        self.image = pygame.Surface((4, 4))
        self.image.fill('lightblue')
        super().__init__(position, self.image, groups, z)
        self.groups = groups
        self.rect = self.image.get_frect(center=position)
        self.z = z

        self.direction = pygame.Vector2()
        self.direction.x = 1
        self.speed = 400

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt

    def check_offscreen(self):
        if self.rect.x > SCREEN_WIDTH + 10:
            self.kill()

    def update(self, dt):
        self.move(dt)
        self.check_offscreen()
