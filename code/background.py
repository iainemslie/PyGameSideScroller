from settings import *


class Background(pygame.sprite.Sprite):
    def __init__(self, groups, position, image_path, speed):
        super().__init__(groups)
        self.groups = groups
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_frect(topleft=position)

        self.direction = pygame.Vector2()
        self.speed = speed

    def move(self, dt):
        self.direction.x = -1
        self.rect.x += self.direction.x * self.speed * dt

    def update(self, dt):
        self.move(dt)
