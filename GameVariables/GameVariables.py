import pygame

class GameVariables:
    FPS = 60
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 800

    FONT_BIG:pygame.sysfont.Font = None
    FONT_MIDDLE:pygame.sysfont.Font = None
    FONT_SMALL:pygame.sysfont.Font = None

    @staticmethod
    def init():
        pygame.init()
        GameVariables.FONT_BIG = pygame.sysfont.SysFont(name="arial", size=55, bold = True)
        GameVariables.FONT_MIDDLE =  pygame.sysfont.SysFont(name="arial", size=40, bold = True)
        GameVariables.FONT_SMALL =  pygame.sysfont.SysFont(name="arial", size=14, bold = True)

class GameScreens:
    MENUE = "MENUE"
    PLAY = "PLAY"
    EXIT = "EXIT"
    actual = MENUE
