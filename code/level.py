from settings import *
from player import Player
from enemy import Enemy
from timer import Timer
from random import randint
from os.path import join
from sprites import BGSprite
from utils import get_bg_paths
from groups import AllSprites


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.missile_sprites = pygame.sprite.Group()

        self.enemy_list = []

        self.spawn_timer = Timer(1000)

        self.setup()

    def setup(self):
        self.create_background()
        Player((16, SCREEN_HEIGHT / 2),
               player_img_path,
               self.all_sprites,
               self.collision_sprites,
               self.missile_sprites,
               10)
        self.spawn_timer.activate()

    def create_background(self):
        num_in_layer = 8
        for z in range(0, num_in_layer):
            bg_paths = get_bg_paths(level1[z])
            for index, path in enumerate(bg_paths):
                BGSprite(position=(SCREEN_WIDTH * z, 0),
                         image_path=path,
                         groups=self.all_sprites,
                         speed=index * 50,
                         z=index,
                         num_in_layer=8)

    def spawn_enemies(self):
        spawn_position_y = randint(32, SCREEN_HEIGHT - 32)
        if not self.spawn_timer.active:
            self.enemy_list.append(
                Enemy((SCREEN_WIDTH + 100, spawn_position_y),
                      enemy_img_path,
                      (self.all_sprites, self.collision_sprites), 10))
            self.spawn_timer.activate()

    def run(self, dt):
        self.spawn_timer.update()
        self.spawn_enemies()
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surface)
