import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    framerate = 100
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updateable:
            item.update(dt)

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit framerate
        dt = clock.tick(framerate) / 1000


if __name__ == "__main__":
    main()
