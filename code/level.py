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

        self.enemy_list = []

        self.spawn_timer = Timer(1000)

        self.setup()

    def setup(self):
        self.create_background()
        print(player_img_path)
        Player((16, SCREEN_HEIGHT / 2),
               player_img_path,
               self.all_sprites,
               self.collision_sprites,
               10)
        self.spawn_timer.activate()

    def create_background(self):
        self.bg_paths = get_bg_paths(level1["background"])

        bg_path = join(self.bg_paths[0])
        self.bg = pygame.image.load(bg_path)

        bg2_path = join(self.bg_paths[1])
        bg2 = BGSprite((0, 0), bg2_path, self.all_sprites, 15, 2)

        bg3_path = join(self.bg_paths[2])
        bg3 = BGSprite((0, 0), bg3_path, self.all_sprites, 25, 3)

        bg5_path = join(self.bg_paths[4])
        bg5 = BGSprite((0, 0), bg5_path, self.all_sprites, 45, 4)

    def spawn_enemies(self):
        spawn_position_y = randint(32, SCREEN_HEIGHT - 32)
        if not self.spawn_timer.active:
            self.enemy_list.append(
                Enemy((SCREEN_WIDTH + 100, spawn_position_y),
                      enemy_img_path,
                      (self.all_sprites, self.collision_sprites), 10))
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
