import pygame

class GameVariables:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SQUARE_SIZE = 50
    FPS = 60

    Muni_Size = 20
    Munition_heigh = 50
    Munition_width = 30

    FONT_BIG:pygame.sysfont.Font = None
    FONT_MIDDLE:pygame.sysfont.Font = None
    FONT_SMALL:pygame.sysfont.Font = None

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont(name="comic sans", size=55, bold = True)
        GameVariables.FONT_MIDDLE =  pygame.sysfont.SysFont(name="comic sans", size=40, bold = True)
        GameVariables.FONT_SMALL =  pygame.sysfont.SysFont(name="comic sans", size=25, bold = True)

class GameScreens:
    MENUE = "MENUE"
    PLAY = "PLAY"
    EXIT = "EXIT"
    PAUSE = "PAUSE"
    SETTINGS = "SETTINGS"
    actual = MENUE
