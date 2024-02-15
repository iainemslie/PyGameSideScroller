from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def draw(self, target_pos):
        for sprite in sorted(self, key=lambda sprite: sprite.z):
            # offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, sprite.rect.topleft)
