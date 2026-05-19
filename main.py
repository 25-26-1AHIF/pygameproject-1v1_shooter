import time
import pygame

from GameVariables.GameVariables import GameVariables as gv
from GameVariables.GameVariables import GameScreens as gs
from GameVariables.Player import Player1, Player2


def menue_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| MENÜ |||")

    mainscreen_bild = pygame.image.load("bilder/mainscreen.jpeg")
    mainscreen_bild = pygame.transform.scale(
        mainscreen_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    )


    titel_text = gv.FONT_BIG.render(" 1 vs 1 Shooter ", True, "white")
    starten_text = gv.FONT_MIDDLE.render(" Start ", True, "white")
    schließen_text = gv.FONT_MIDDLE.render(" Quit ", True, "white")
    keybinds_text = gv.FONT_MIDDLE.render(" Keybinds ", True, "white")

    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 50))

    starten_button = pygame.Rect(0, 170, 220, 70)
    schließen_button = pygame.Rect(0, 370, 220, 70)
    keybinds_button = pygame.Rect(0, 270, 220, 70)
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

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

        screen.blit(mainscreen_bild, (0, 0))

        # HOVER Farben
        starten_farbe = gv.lila_farbe
        schließen_farbe = gv.lila_farbe
        keybinds_farbe = gv.lila_farbe

        if starten_button.collidepoint(mouse_pos):
            starten_farbe = gv.hellblau_farbe

        if schließen_button.collidepoint(mouse_pos):
            schließen_farbe = gv.hellblau_farbe

        if keybinds_button.collidepoint(mouse_pos):
            keybinds_farbe = gv.hellblau_farbe

        pygame.draw.rect(screen, starten_farbe, starten_button, border_radius=10)
        pygame.draw.rect(screen, schließen_farbe, schließen_button, border_radius=10)
        pygame.draw.rect(screen, keybinds_farbe, keybinds_button, border_radius=10)

        pygame.draw.rect(screen, "red", titel_text_rect, border_radius=10)

        screen.blit(titel_text, titel_text_rect)
        screen.blit(starten_text, starten_button)
        screen.blit(schließen_text, schließen_button)
        screen.blit(keybinds_text, keybinds_button)

        clock.tick(gv.FPS)
        pygame.display.flip()
    pygame.quit()


def pause_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| PAUSE |||")

    Pausescreen_bild = pygame.image.load("bilder/chatgpt Pause screen.png")
    Pausescreen_bild = pygame.transform.scale(
        Pausescreen_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    )
    pause_text = gv.FONT_BIG.render(" GAME PAUSIERT ", True, "white")
    leer_text = gv.FONT_MIDDLE.render(" Leertaste um Fortzufahren ", True,  gv.hellgrau_farbe)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return gs.PLAY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return gs.MENUE
        screen.blit(Pausescreen_bild, (0,0))

        pause_box = pygame.Rect(150, 140, 700, 250)

        pygame.draw.rect(screen, gv.grau_farbe, pause_box, border_radius=25)
        pygame.draw.rect(screen, gv.hellblau_farbe, pause_box, 4, border_radius=25)
        screen.blit(pause_text, (gv.SCREEN_WIDTH/4,150))
        screen.blit(leer_text, (gv.SCREEN_WIDTH/4-20, 250))
        clock.tick(gv.FPS)
        pygame.display.flip()
    pygame.quit()


def settings_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    pygame.init()
    pygame.display.set_caption("||| 🔫 1vs1 Shooter 🔫 ||| Settings |||")


    settings_bild = pygame.image.load("bilder/chatgpt settigs screen.png")

    settings_bild = pygame.transform.scale(
        settings_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    )

    titel_text = gv.FONT_BIG.render(" 1 vs 1 Shooter ", True, "black")
    Player_1_text = gv.FONT_MIDDLE.render(" Player 1 ", True, "black")
    Player_2_text = gv.FONT_MIDDLE.render(" Player 2 ", True, "black")


    titel_text_rect = titel_text.get_rect(center=(gv.SCREEN_WIDTH / 2, 50))
    Player_1_text_rect = Player_1_text.get_rect(center=(275, 175))
    Player_2_text_rect = Player_2_text.get_rect(center=(700, 175))

    P1_springen_text = gv.FONT_SMALL.render(" Springen:    W    ", True, "white")
    P1_rechts_text = gv.FONT_SMALL.render(" Rechts:    D    ", True, "white")
    P1_links_text  = gv.FONT_SMALL.render(" Links:    A    ", True, "white")
    P1_schießen_text = gv.FONT_SMALL.render(" Schießen:    E    ", True, "white")


    P2_springen_text = gv.FONT_SMALL.render(" Springen:    ^    ", True, "white")
    P2_rechts_text = gv.FONT_SMALL.render(" Rechts:    >    ", True, "white")
    P2_links_text = gv.FONT_SMALL.render(" Links:    <    ", True, "white")
    P2_schießen_text = gv.FONT_SMALL.render("Schießen: Right Shift", True, "white")

    P1_links_rect = pygame.Rect(180, 220, 270, 55)
    P1_rechts_rect = pygame.Rect(180, 300, 270, 55)
    P1_springen_rect = pygame.Rect(180, 380, 270, 55)
    P1_schießen_rect = pygame.Rect(180, 460, 270, 55)

    P2_links_rect = pygame.Rect(600, 220, 270, 55)
    P2_rechts_rect = pygame.Rect(600, 300, 270, 55)
    P2_springen_rect = pygame.Rect(600, 380, 270, 55)
    P2_schießen_rect = pygame.Rect(600, 460, 270, 55)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return gs.MENUE
        screen.blit(settings_bild, (0,0))

        rect = pygame.Rect(80, 110, 850, 450)

        pygame.draw.rect(screen, gv.grau_farbe, rect, border_radius=25)
        pygame.draw.rect(screen, gv.hellblau_farbe, rect, 4, border_radius=25)

        pygame.draw.rect(screen, gv.hellgrau_farbe, Player_1_text_rect, border_radius=10)
        pygame.draw.rect(screen,gv.hellgrau_farbe , Player_2_text_rect, border_radius=10)
        pygame.draw.rect(screen, "red", titel_text_rect, border_radius=10)
        screen.blit(titel_text, titel_text_rect)
        screen.blit(Player_1_text, Player_1_text_rect)
        screen.blit(Player_2_text, Player_2_text_rect)

        pygame.draw.rect(screen, gv.hellblau_farbe, P1_springen_rect, border_radius=10)
        pygame.draw.rect(screen, gv.hellblau_farbe, P1_links_rect, border_radius=10)
        pygame.draw.rect(screen, gv.hellblau_farbe, P1_rechts_rect, border_radius=10)
        pygame.draw.rect(screen, gv.hellblau_farbe, P1_schießen_rect,  border_radius=10)
        screen.blit(P1_springen_text, P1_springen_rect)
        screen.blit(P1_rechts_text, P1_rechts_rect)
        screen.blit(P1_links_text, P1_links_rect)
        screen.blit(P1_schießen_text, P1_schießen_rect)

        pygame.draw.rect(screen, gv.hellblau_farbe, P2_springen_rect, border_radius=10)
        pygame.draw.rect(screen, gv.hellblau_farbe, P2_links_rect, border_radius=10)
        pygame.draw.rect(screen, gv.hellblau_farbe, P2_rechts_rect, border_radius=10)
        pygame.draw.rect(screen, gv.hellblau_farbe, P2_schießen_rect, border_radius=10)
        screen.blit(P2_springen_text, P2_springen_rect)
        screen.blit(P2_links_text, P2_links_rect)
        screen.blit(P2_rechts_text, P2_rechts_rect)
        screen.blit(P2_schießen_text, P2_schießen_rect)


        clock.tick(gv.FPS)
        pygame.display.flip()

    pygame.quit()


def play_screen(screen: pygame.Surface, clock: pygame.time.Clock):
    hintergrund = pygame.image.load("bilder/Hintergrundgame.jpeg")
    hintergrund = pygame.transform.scale(hintergrund, (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))

    pygame.display.set_caption("||| PLAY |||")

    player1 = Player1(screen)
    player2 = Player2(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return gs.EXIT

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return gs.MENUE
                if event.key == pygame.K_SPACE:
                    return gs.PAUSE

                # Player1 schießt mit E
                if event.key == pygame.K_e:
                    player1.shoot()

                # Player2 schießt mit rechter SHIFT
                if event.key == pygame.K_RSHIFT:
                    player2.shoot()

        screen.blit(hintergrund, (0, 0))

        player1.update_and_draw()
        player2.update_and_draw()

        pygame.display.flip()
        clock.tick(gv.FPS)



def sieger_screen(screen: pygame.Surface ,clock: pygame.time.Clock):
    hintergrundwinner1_bild = pygame.image.load("bilder/mainscreen.jpeg")
    hintergrundwinner1_bild = pygame.transform.scale(
        hintergrundwinner1_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    )

    hintergrundwinner2_bild = pygame.image.load("bilder/mainscreen.jpeg")
    hintergrundwinner2_bild = pygame.transform.scale(
        hintergrundwinner2_bild,
        (gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT)
    )

    pygame.init()
    pygame.display.set_caption("||| 🔫  1vs1 Shooter 🔫 ||| WINNER |||")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
               if event.key == pygame.K_ESCAPE:
                    return gs.MENUE
            if event.type == pygame.QUIT:
                running = False
   #     if winner == Player1:
    #        screen.blit(hintergrundwinner1_bild, (0, 0))
     #   if winner == Player2:
      #      screen.blit(hintergrundwinner2_bild, (0, 0))
        clock.tick(gv.FPS)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    gv.init()
    screen = pygame.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:

        if gs.actual == gs.MENUE:
            print("Menü Screen")
            gs.actual = menue_screen(screen, clock)

        elif gs.actual == gs.PLAY:
            print("Play Screen")
            gs.actual = play_screen(screen, clock)

        elif gs.actual == gs.PAUSE:
            print("Pause Screen")
            gs.actual = pause_screen(screen, clock)

        elif gs.actual == gs.SETTINGS:
            print("Settings Screen")
            gs.actual = settings_screen(screen, clock)

        elif gs.actual == gs.WINNER:
            print("Winner Screen")
            gs.actual = settings_screen(screen, clock)
            time.sleep(5)
            gs.actual = gs.MENUE

        elif gs.actual == gs.EXIT:
            print("Game beendet")
            break