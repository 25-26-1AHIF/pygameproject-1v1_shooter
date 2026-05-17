import pygame
from GameVariables.GameVariables import GameVariables as GV



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
