import  pygame
from GameVariables.GameVariables import GameVariables as GV
from GameVariables.Rocket import Rocket, Rockets



class Player1:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = GV.SCREEN_WIDTH / 2 - GV.SQUARE_SIZE / 2
        self.y = GV.SCREEN_HEIGHT - GV.SQUARE_SIZE - 1
        self.rockets = Rockets(screen)
        self.dx = 7
        self.P1_left = pygame.K_A
        self.P1_right = pygame.K_D
        self.P1_up = pygame.K_W
        self.P1_down = pygame.K_S

    def shoot(self):
        muni_x_1 = self.x + GV.SQUARE_SIZE / 2 - GV.Muni_Size / 2
        muni_y_1 = self.y - GV.MISSLE_SIZE
        return Rocket(self.screen, muni_x_1, muni_y_1, 0, -5)

    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.P1_left]:
            self.x -= self.dx
        if keys_pressed[self.P1_right]:
            self.x += self.dx
        if keys_pressed[self.P1_down]:
            self.y -= 2
        if keys_pressed[self.P1_up]:
            self.y += 2



    def update_and_draw(self):
        self.move()
        self.rockets.update_and_draw()
        pygame.draw.rect(self.screen, "red", (self.x, self.y, GV.SQUARE_SIZE, GV.SQUARE_SIZE))

class Player2:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = GV.SCREEN_WIDTH / 2 - GV.SQUARE_SIZE / 2
        self.y = GV.SCREEN_HEIGHT - GV.SQUARE_SIZE - 1
        self.rockets = Rockets(screen)
        self.dx = 7
        self.P2_left = pygame.K_LEFT
        self.P2_right = pygame.K_RIGHT
        self.P2_up = pygame.K_UP
        self.P2_down = pygame.K_DOWN

    def shoot(self):
        muni_x = self.x + GV.SQUARE_SIZE / 2 - GV.MISSLE_SIZE / 2
        muni_y = self.y - GV.MISSLE_SIZE
        return RO.Rocket(self.screen, muni_x, muni_y, 0, -5)


    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[self.P2_left]:
            self.x -= self.dx
        if keys_pressed[self.P2_right]:
            self.x += self.dx
        if keys_pressed[self.P2_up]:
            self.y -= 2
        if keys_pressed[self.P2_down]:
            self.y += 2

    def update_and_draw(self):
        self.move()
        self.rockets.update_and_draw()
        pygame.draw.rect(self.screen, "blue", (self.x, self.y, GV.SQUARE_SIZE, GV.SQUARE_SIZE))
