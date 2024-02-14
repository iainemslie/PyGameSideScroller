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

        self.player_group = pygame.sprite.Group()

        self.spawn_timer = Timer(1000)

        self.setup()

    def setup(self):
        Player(self.player_group, (self.screen_width /
               2, self.screen_height - 64))
        self.spawn_timer.activate()

    def spawn_enemies(self):
        spawn_position_x = randint(0, self.screen_width)
        if not self.spawn_timer.active:
            Enemy(self.player_group, (spawn_position_x, 100))
            self.spawn_timer.activate()

    def run(self, dt):
        self.display_surface.fill('black')
        self.spawn_timer.update()
        self.spawn_enemies()
        self.player_group.update(dt)
        self.player_group.draw(self.display_surface)
