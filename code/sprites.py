from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups=None, z=10):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()
        self.z = z


class BGSprite(Sprite):
    def __init__(self, position, image_path, groups, speed, z, num_in_layer):
        self.image = pygame.image.load(image_path)
        super().__init__(position, self.image, groups, z)
        self.groups = groups
        self.rect = self.image.get_frect(topleft=position)
        self.z = z
        self.num_in_layer = num_in_layer

        self.direction = pygame.Vector2()
        self.speed = speed

    def move(self, dt):
        self.direction.x = -1
        self.rect.x += self.direction.x * self.speed * dt
        # wrap
        if self.rect.x <= -SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH * (self.num_in_layer - 1)

    def update(self, dt):
        self.move(dt)
