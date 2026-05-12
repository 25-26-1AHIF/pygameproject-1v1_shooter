import pygame
from GameVariables.GameVariables import GameVariables as gv

def main_screen(screen: pygame.Surface ,clock: pygame.time.Clock, ):
    pygame.init()
    pygame.display.set_caption("1v1 Shooter")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(gv.FPS)
        screen.fill("blue")
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    main_screen(screen, clock)