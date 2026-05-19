import pygame
from GameVariables.GameVariables import GameVariables as GV
from GameVariables.Rocket import Rocket, Rockets



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
        if keys[pygame.K_a]:
            self.x -= self.dx
        if keys[pygame.K_d]:
            self.x += self.dx
        if keys[pygame.K_w]:
            self.y -= self.dx
        if keys[pygame.K_s]:
            self.y += self.dx

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
        if keys[pygame.K_LEFT]:
            self.x -= self.dx
        if keys[pygame.K_RIGHT]:
            self.x += self.dx
        if keys[pygame.K_UP]:
            self.y -= self.dx
        if keys[pygame.K_DOWN]:
            self.y += self.dx


    def update_and_draw(self):
        self.move()
        self.rockets.update_and_draw()
        self.screen.blit(self.image, (self.x, self.y))


