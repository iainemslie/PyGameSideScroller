import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.groups = groups
        self.image = pygame.Surface((32, 32))
        # self.image = pygame.image.load("images/Ship2.png")
        self.image.fill('red')
        self.rect = self.image.get_frect(center=position)
