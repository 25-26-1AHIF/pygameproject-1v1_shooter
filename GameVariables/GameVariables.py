import pygame

class GameVariables:
    FPS = 60
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 1000
    Bild_x = 300
    Bild_y = 300

    FONT_BIG:pygame.sysfont.Font = None
    FONT_MIDDLE:pygame.sysfont.Font = None
    FONT_SMALL:pygame.sysfont.Font = None


    lila_farbe = (73, 3, 41)
    grau_farbe = (20, 20, 35)
    hellblau_farbe = (120, 170, 255)
    hellgrau_farbe = (86, 89, 103)

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.font.SysFont(name="Times New Roman", size=60, bold = True)
        GameVariables.FONT_MIDDLE =  pygame.font.SysFont(name="comic sans", size=40, bold = True)
        GameVariables.FONT_SMALL =  pygame.font.SysFont(name="comic sans", size=25, bold = True)

class GameScreens:
    MENUE = "MENUE"
    PLAY = "PLAY"
    EXIT = "EXIT"
    PAUSE = "PAUSE"
    SETTINGS = "SETTINGS"
    WINNER = "WINNER"
    actual = MENUE


# Ki chatgpt wie mache ich benutzerdefinierte keybinds
# Ki chatgpt wie mache ich inputs im Pygame
# Kein Code kopiert, nur inputs geholt
class Controls:
    P1_LEFT = pygame.K_a
    P1_RIGHT = pygame.K_d
    P1_UP = pygame.K_w
#    P1_DOWN = pygame.K_s
    P1_SHOOT = pygame.K_e

    P2_LEFT = pygame.K_LEFT
    P2_RIGHT = pygame.K_RIGHT
    P2_UP = pygame.K_UP
#    P2_DOWN = pygame.K_DOWN
    P2_SHOOT = pygame.K_RSHIFT