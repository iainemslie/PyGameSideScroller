import pygame
from player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.player_group = pygame.sprite.Group()

        self.setup()

    def setup(self):
        Player(self.player_group, (self.display_surface.get_width() /
               2, self.display_surface.get_height() - 32))

    def run(self, dt):
        self.display_surface.fill('beige')
        self.player_group.update(dt)
        self.player_group.draw(self.display_surface)
