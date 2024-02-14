import pygame
import sys
from player import Player
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (640, 480), pygame.NOFRAME)
        pygame.display.set_caption("Side Scroller")

        pygame.mouse.set_visible(False)

        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
