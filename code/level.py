import pygame
from player import Player
from enemy import Enemy
from timer import Timer
from random import randint


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.screen_width = self.display_surface.get_width()
        self.screen_height = self.display_surface.get_height()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.enemy_list = []

        self.spawn_timer = Timer(1000)

        self.setup()

    def setup(self):
        Player((self.screen_width / 2, self.screen_height - 64),
               self.all_sprites,
               self.collision_sprites)
        self.spawn_timer.activate()

    def spawn_enemies(self):
        spawn_position_x = randint(32, self.screen_width - 32)
        if not self.spawn_timer.active:
            self.enemy_list.append(
                Enemy((self.all_sprites, self.collision_sprites),
                      (spawn_position_x, -100)))
            self.spawn_timer.activate()

    def destroy_enemies(self):
        for enemy in self.enemy_list:
            if enemy.rect.top > self.screen_height:
                self.enemy_list.pop()

    def run(self, dt):
        self.display_surface.fill('black')
        self.spawn_timer.update()
        self.spawn_enemies()
        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surface)
        self.destroy_enemies()
