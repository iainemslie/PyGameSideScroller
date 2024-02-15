from settings import *
from player import Player
from enemy import Enemy
from timer import Timer
from random import randint
from os.path import join
# from background import Background


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        bg_path = join('resources', 'scrolling_city_background',
                       '1 Backgrounds', '1', 'Night', '1.png')
        self.bg = self.image = pygame.image.load(bg_path)

        self.enemy_list = []

        self.spawn_timer = Timer(1000)

        self.setup()

    def setup(self):
        Player((32, SCREEN_HEIGHT / 2),
               self.all_sprites,
               self.collision_sprites)
        self.spawn_timer.activate()

    def spawn_enemies(self):
        spawn_position_y = randint(32, SCREEN_HEIGHT - 32)
        if not self.spawn_timer.active:
            self.enemy_list.append(
                Enemy((self.all_sprites, self.collision_sprites),
                      (SCREEN_WIDTH + 100, spawn_position_y)))
            self.spawn_timer.activate()

    def destroy_enemies(self):
        for enemy in self.enemy_list:
            if enemy.rect.right < 0:
                self.enemy_list.pop()

    def run(self, dt):
        self.display_surface.fill('black')
        self.display_surface.blit(self.bg, (0, 0))
        self.spawn_timer.update()
        self.spawn_enemies()
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surface)
        self.destroy_enemies()
