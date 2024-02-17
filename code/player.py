from settings import *
from missile import Missile
from timer import Timer
from os.path import join
from sprites import Sprite


class Player(Sprite):
    def __init__(self, position, image_path, all_sprites, collision_sprites, missile_sprites, z=10):
        self.image = pygame.image.load(join(image_path))
        super().__init__(position, self.image, (all_sprites), z)
        self.all_sprites = all_sprites
        self.rect = self.image.get_frect(topleft=position)
        self.z = z

        self.collision_sprites = collision_sprites

        self.direction = pygame.Vector2()
        self.speed = 400

        self.missile_timer = Timer(250)
        self.missile_sprites = missile_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = pygame.Vector2()

        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1

        if keys[pygame.K_SPACE] and not self.missile_timer.active:
            self.missile_timer.activate()
            Missile((self.rect.center[0] + 32, self.rect.center[1]),
                    '',
                    (self.all_sprites, self.missile_sprites),
                    10,
                    )

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
            for missile in self.missile_sprites:
                if sprite.rect.colliderect(missile.rect):
                    sprite.kill()
                    missile.kill()
            # collide with player
            if sprite.rect.colliderect(self.rect):
                sprite.kill()

    def update(self, dt):
        self.input()
        self.missile_timer.update()
        self.move(dt)
        self.check_collisions()
