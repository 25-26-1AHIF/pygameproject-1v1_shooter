import pygame

from GameVariables.GameVariables import GameVariables as gv
from GameVariables.GameVariables import GameScreens as gs

def menue_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter  ||| MENÜ |||")

    titel_text = gv.FONT_BIG.render("1 vs 1 Shooter", True, "white")
    starten_text = gv.FONT_MIDDLE.render("Start", True, "white")
    schließen_text = gv.FONT_MIDDLE.render("Quit", True, "white")
    keybinds_text = gv.FONT_MIDDLE.render("Keybinds", True, "white")

    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 75))
    starten_text_rect = starten_text.get_rect(center=(70, 200))
    schließen_text_rect = schließen_text.get_rect(center=(65, 400))
    keybinds_text_rect = keybinds_text.get_rect(center=(110, 300))

    starten_button = pygame.Rect(20, 170, 220, 70)
    schließen_button = pygame.Rect(20, 370, 220, 70)
    keybinds_button = pygame.Rect(20, 270, 220, 70)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return gs.EXIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                if starten_button.collidepoint(event.pos):
                    return gs.PLAY
                if schließen_button.collidepoint(event.pos):
                    return gs.EXIT
                if keybinds_button.collidepoint(event.pos):
                    return gs.SETTINGS

        screen.fill("blue")
        pygame.draw.rect(screen, "red", starten_text_rect, border_radius=10)
        pygame.draw.rect(screen, "red", schließen_text_rect, border_radius=10)
        pygame.draw.rect(screen, "darkgreen", titel_text_rect, border_radius=10)
        pygame.draw.rect(screen, "red", keybinds_text_rect, border_radius=10)
        #border radius ist recharchiert
        screen.blit(titel_text, titel_text_rect)
        screen.blit(starten_text, starten_text_rect)
        screen.blit(schließen_text, schließen_text_rect)
        screen.blit(keybinds_text, keybinds_text_rect)


        clock.tick(gv.FPS)
        pygame.display.flip()
    pygame.quit()



def pause_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| PAUSE |||")

    pause_text = gv.FONT_BIG.render("GAME PAUSIERT", True, "white")
    leer_text = gv.FONT_MIDDLE.render("Leertaste um Fortzufahren", True, "purple")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   return gs.PLAY
        screen.fill("green")
        screen.blit(pause_text, (150,100))
        screen.blit(leer_text, (150, 400))
        clock.tick(gv.FPS)
        pygame.display.flip()

    pygame.quit()



def settings_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| Settings |||")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return gs.MENUE
        screen.fill("yellow")
        clock.tick(gv.FPS)
        pygame.display.flip()

    pygame.quit()

def play_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫  1vs1 Shooter 🔫 ||| PLAY |||")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
               if event.key == pygame.K_ESCAPE:
                    return gs.MENUE
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                    return gs.PAUSE
            if event.type == pygame.QUIT:
                running = False
        screen.fill("pink")
        clock.tick(gv.FPS)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    gv.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:

        if gs.actual == gs.MENUE:
            gs.actual = menue_screen(screen, clock)


        elif gs.actual == gs.PLAY:
            gs.actual = play_screen(screen, clock)

        elif gs.actual == gs.PAUSE:
            gs.actual = pause_screen(screen, clock)

        elif gs.actual == gs.SETTINGS:
            gs.actual = settings_screen(screen, clock)


        elif gs.actual == gs.EXIT:
            break

    pygame.quit()
