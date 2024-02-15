from settings import *
from missile import Missile
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprites):
        super().__init__(groups)
        self.groups = groups
        self.image = pygame.image.load("images/Ship2.png")
        self.rect = self.image.get_frect(center=position)

        self.collision_sprites = collision_sprites

        self.direction = pygame.Vector2()
        self.speed = 400

        self.missile_timer = Timer(250)

        self.missile_list = []

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = pygame.Vector2()

        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1

        if keys[pygame.K_SPACE] and not self.missile_timer.active:
            self.missile_timer.activate()
            self.missile_list.append(Missile(self.groups,
                                             (self.rect.center[0] + 32, self.rect.center[1])))

        self.direction.y = input_vector.normalize().y if input_vector else input_vector.y

    def move(self, dt):
        if self.rect.top < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        else:
            self.rect.y += self.direction.y * self.speed * dt

    def check_collisions(self):
        for sprite in self.collision_sprites:
            for missile in self.missile_list:
                if sprite.rect.colliderect(missile.rect):
                    sprite.image.fill('blue')

    def destroy_missiles(self):
        for missile in self.missile_list:
            if missile.rect.left > SCREEN_WIDTH:
                self.missile_list.pop()

    def update(self, dt):
        self.input()
        self.missile_timer.update()
        self.move(dt)
        self.check_collisions()
        self.destroy_missiles()
