import pygame

from GameVariables.GameVariables import GameVariables as gv
from GameVariables.GameVariables import GameScreens as gs

def menue_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    mainscreen_bild = pygame.image.load("bilder/mainscreen.jpeg")
    mainscreen_bild = pygame.transform.scale(
        mainscreen_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    )
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| MENÜ |||")

    titel_text = gv.FONT_BIG.render("1 vs 1 Shooter", True, "white")
    starten_text = gv.FONT_MIDDLE.render("Start", True, "white")
    schließen_text = gv.FONT_MIDDLE.render("Quit", True, "white")
    keybinds_text = gv.FONT_MIDDLE.render("Keybinds", True, "white")

    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 75))
    starten_text_rect = starten_text.get_rect(center=(70, 200))
    schließen_text_rect = schließen_text.get_rect(center=(65, 400))
    keybinds_text_rect = keybinds_text.get_rect(center=(100, 300))

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

        screen.blit(mainscreen_bild, (0,0))
        #screen.fill("blue")
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

    titel_text = gv.FONT_BIG.render("1 vs 1 Shooter", True, "white")
    pause_text = gv.FONT_BIG.render("GAME PAUSIERT", True, "black")
    leer_text = gv.FONT_MIDDLE.render("Leertaste um Fortzufahren", True, "black")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return gs.PLAY
        screen.fill("green")
        screen.blit(pause_text, (150,175))
        screen.blit(leer_text, (125, 400))
        screen.blit(titel_text, (175, 50))
        clock.tick(gv.FPS)
        pygame.display.flip()


def settings_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| Settings |||")


    titel_text = gv.FONT_BIG.render("1 vs 1 Shooter", True, "black")
    Player_1_text = gv.FONT_MIDDLE.render("Player 1", True, "black")
    Player_2_text = gv.FONT_MIDDLE.render("Player 2", True, "black")


    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 75))
    Player_1_text_rect = Player_1_text.get_rect(center=(100, 200))
    Player_2_text_rect = Player_2_text.get_rect(center=(100, 400))

    P1_springen = gv.FONT_SMALL.render("Springen:      ", True, "white")
    P1_rechts = gv.FONT_SMALL.render("Rechts:      ", True, "white")
    P1_links = gv.FONT_SMALL.render("Links:        ", True, "white")

    P2_springen = gv.FONT_SMALL.render("Springen:      ", True, "white")
    P2_rechts = gv.FONT_SMALL.render("Rechts:      ", True, "white")
    P2_links = gv.FONT_SMALL.render("Links:        ", True, "white")

    P1_springen_rect = P1_springen.get_rect(center=(500, 200))
    P1_rechts_rect = P1_rechts.get_rect(center=(300, 250))
    P1_links_rect = P1_links.get_rect(center=(700, 250))

    P2_springen_rect = P2_springen.get_rect(center=(500, 400))
    P2_rechts_rect = P2_rechts.get_rect(center=(300, 450))
    P2_links_rect = P2_links.get_rect(center=(700, 450))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return gs.MENUE
        screen.fill("yellow")

        pygame.draw.rect(screen, "red", Player_1_text_rect, border_radius=10)
        pygame.draw.rect(screen, "red", Player_2_text_rect, border_radius=10)
        pygame.draw.rect(screen, "purple", titel_text_rect, border_radius=10)
        screen.blit(titel_text, titel_text_rect)
        screen.blit(Player_1_text, Player_1_text_rect)
        screen.blit(Player_2_text, Player_2_text_rect)

        pygame.draw.rect(screen, "blue", P1_springen_rect, border_radius=10)
        pygame.draw.rect(screen, "blue", P1_links_rect, border_radius=10)
        pygame.draw.rect(screen, "blue", P1_rechts_rect, border_radius=10)
        screen.blit(P1_springen, P1_springen_rect)
        screen.blit(P1_rechts, P1_links_rect)
        screen.blit(P1_links, P1_rechts_rect)

        pygame.draw.rect(screen, "blue", P2_springen_rect, border_radius=10)
        pygame.draw.rect(screen, "blue", P2_links_rect, border_radius=10)
        pygame.draw.rect(screen, "blue", P2_rechts_rect, border_radius=10)
        screen.blit(P2_springen, P2_springen_rect)
        screen.blit(P2_rechts, P2_links_rect)
        screen.blit(P2_links, P2_rechts_rect)

        clock.tick(gv.FPS)
        pygame.display.flip()

    pygame.quit()

def play_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    hintergurdgame_bild = pygame.image.load("bilder/Hintergrundgame.jpeg")
    hintergurdgame_bild = pygame.transform.scale(
        hintergurdgame_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    ) #recharschiert (alles mit bildern)
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
        screen.blit(hintergurdgame_bild, (0, 0))
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