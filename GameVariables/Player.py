import pygame
from GameVariables.GameVariables import GameVariables as GV
from GameVariables.Rocket import Rocket, Rockets
from GameVariables.GameVariables import Controls



class Player1:
    def __init__(self, screen):
        self.screen = screen
        self.x = 50
        self.y = GV.SCREEN_HEIGHT // 2
        self.dx = 6
        self.rockets = Rockets(screen)
        self.image = pygame.image.load("bilder/Personarmnachrechts.png")


    def shoot(self):
        muni_x = self.x + 25
        muni_y = self.y
        rocket = Rocket(self.screen, muni_x, muni_y, +8, 0)
        self.rockets.add_rocket(rocket)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[Controls.P1_LEFT]:
            self.x -= self.dx

        if keys[Controls.P1_RIGHT]:
            self.x += self.dx

        if keys[Controls.P1_UP]:
            self.y -= self.dx

        if keys[Controls.P1_DOWN]:
            self.y += self.dx

        if self.x < -20:
            self.x = -20
        if self.x > 915:
            self.x = 915
        if self.y < 10:
            self.y = 10
        if self.y > 500:
            self.y = 500

    def update_and_draw(self):
        self.move()
        self.rockets.update_and_draw()
        self.screen.blit(self.image, (self.x, self.y))


class Player2:
    def __init__(self, screen):
        self.image = pygame.image.load("bilder/Personarmnachlinks.png")
        self.screen = screen
        self.x = GV.SCREEN_WIDTH - 150
        self.y = GV.SCREEN_HEIGHT // 2
        self.dx = 6
        self.rockets = Rockets(screen)

    def shoot(self):
        muni_x = self.x + 25
        muni_y = self.y
        rocket = Rocket(self.screen, muni_x, muni_y, -8, 0)
        self.rockets.add_rocket(rocket)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[Controls.P2_LEFT]:
            self.x -= self.dx

        if keys[Controls.P2_RIGHT]:
            self.x += self.dx

        if keys[Controls.P2_UP]:
            self.y -= self.dx

        if keys[Controls.P2_DOWN]:
            self.y += self.dx

        if self.x < 0:
            self.x = 0
        if self.x > 930:
            self.x = 930
        if self.y < 10:
            self.y = 10
        if self.y > 500:
            self.y = 500


    def update_and_draw(self):
        self.move()
        self.rockets.update_and_draw()
        self.screen.blit(self.image, (self.x, self.y))


