import pygame
from GameVariables.GameVariables import GameVariables as GV

class Rocket:
    def __init__(self, screen, xpos, ypos, dx, dy):
        self.screen = screen
        self.xpos = xpos
        self.ypos = ypos
        self.dx = dx
        self.dy = dy
        self.width = 10
        self.height = 10
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    def update_and_draw(self):
        self.xpos += self.dx
        self.ypos += self.dy
        self.rect.topleft = (self.xpos, self.ypos)
        pygame.draw.rect(self.screen, "yellow", self.rect)


class Rockets:
    def __init__(self, screen):
        self.screen = screen
        self.rockets = []

    def add_rocket(self, rocket):
        self.rockets.append(rocket)

    def update_and_draw(self):
        for rocket in self.rockets[:]:
            rocket.update_and_draw()

            if rocket.ypos < 0 or rocket.ypos > GV.SCREEN_HEIGHT:
                self.rockets.remove(rocket)


