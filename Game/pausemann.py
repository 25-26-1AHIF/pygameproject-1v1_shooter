import pygame
from Game.sprite import Sprite

class Pausemann:

    def __init__(self, screen):

        self.screen = screen
        self.x = 50
        self.y = 430
        self.dx = 1

        # ai chatgpt... wie mache ich das sich der skin jedes mal weselt wenn er am rand ankommt?
        self.direction = 1
        self.skin = 0
        self.frame_counter = 0
        self.sprites = [
            Sprite("bilder/Pausemann.png", 4, pygame.Rect(0, 0, 100, 100), 8),
            Sprite("bilder/Pausemannrückwärts.png", 4, pygame.Rect(0, 0, 100, 100), 8)
        ]
        for i in self.sprites:
            i.load_spritesheet()
        self.sprite = self.sprites[self.skin]
        self.sprite.load_spritesheet()

    # ai chatgpt... wie mache ich das sich der skin jedes mal weselt wenn er am rand ankommt?
    def skin_switch(self):

        self.skin += 1
        if self.skin > 1:
            self.skin = 0

        if self.skin == 0:
            self.sprite = Sprite("bilder/Pausemann.png", 4, pygame.Rect(0, 0, 100, 100), 8)

        if self.skin == 1:
            self.sprite = Sprite("bilder/Pausemannrückwärts.png", 4, pygame.Rect(0, 0, 100, 100), 8)

    def move(self):

        self.x += self.dx * self.direction

        if self.x < -20:
            self.direction = 1
            self.skin_switch()

        if self.x > 900:
            self.direction = -1
            self.skin_switch()

    def update_and_draw(self):
        # ai chatgpt... wie mache ich das sich der skin jedes mal weselt wenn er am rand ankommt?
        self.sprite.load_spritesheet()
        self.sprite.draw(self.screen, self.x, self.y, self.frame_counter)
        self.move()
        self.frame_counter += 1