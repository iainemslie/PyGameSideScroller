import pygame
from missile import Missile
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites):
        super().__init__(groups)
        self.groups = groups
        self.image = pygame.image.load("images/Ship2.png")
        self.rect = self.image.get_frect(center=position)

        self.screen_width = pygame.display.get_surface().get_width()

        self.collision_sprites = collision_sprites

        self.direction = pygame.Vector2()
        self.speed = 400

        self.missile_timer = Timer(200)

        self.missile_list = []

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = pygame.Vector2()

        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1

        if keys[pygame.K_SPACE] and not self.missile_timer.active:
            self.missile_timer.activate()
            self.missile_list.append(Missile(self.groups,
                                             (self.rect.center[0], self.rect.top)))

        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

    def move(self, dt):
        if self.rect.left < 0:
            self.rect.x = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        else:
            self.rect.x += self.direction.x * self.speed * dt

    def check_collisions(self):
        for sprite in self.collision_sprites:
            for missile in self.missile_list:
                if sprite.rect.colliderect(missile.rect):
                    sprite.image.fill('blue')

    def destroy_missiles(self):
        for missile in self.missile_list:
            if missile.rect.bottom < 0:
                self.missile_list.pop()

    def update(self, dt):
        self.input()
        self.missile_timer.update()
        self.move(dt)
        self.check_collisions()
        self.destroy_missiles()
