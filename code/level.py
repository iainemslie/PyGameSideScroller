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
        # sky background
        bg_path = get_bg_paths(level1[0])
        self.bg = pygame.image.load(bg_path[0])

        for z in range(0, 7):
            bg_paths = get_bg_paths(level1[z])
            for index, path in enumerate(bg_paths):
                BGSprite((SCREEN_WIDTH * z, 0), path,
                         self.all_sprites, (index + 1) * 15, index + 1)

    def spawn_enemies(self):
        spawn_position_y = randint(32, SCREEN_HEIGHT - 32)
        if not self.spawn_timer.active:
            self.enemy_list.append(
                Enemy((SCREEN_WIDTH + 100, spawn_position_y),
                      enemy_img_path,
                      (self.all_sprites, self.collision_sprites), 10))
            self.spawn_timer.activate()

    def run(self, dt):
        self.display_surface.fill('black')
        self.display_surface.blit(self.bg, (0, 0))
        self.spawn_timer.update()
        self.spawn_enemies()
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surface)
