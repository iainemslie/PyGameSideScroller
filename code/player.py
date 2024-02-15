from settings import *
from missile import Missile
from timer import Timer
from os.path import join
from sprites import Sprite


class Player(Sprite):
    def __init__(self, position, image_path, groups, collision_sprites, z=10):
        self.image = pygame.image.load(join(image_path))
        super().__init__(position, self.image, groups, z)
        self.groups = groups
        self.rect = self.image.get_frect(topleft=position)
        self.z = z

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
            self.missile_list.append(Missile((self.rect.center[0] + 32, self.rect.center[1]),
                                             '',
                                             self.groups,
                                             10,
                                             ))

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
