import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.image = pygame.Surface((32, 32))
        self.image.fill('red')
        self.rect = self.image.get_frect(center=position)

        self.direction = pygame.Vector2()
        self.speed = 400

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = pygame.Vector2()

        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1

        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)
