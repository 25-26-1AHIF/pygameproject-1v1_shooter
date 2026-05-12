import pygame
# Initialisierung
pygame.init()
pygame.display.set_caption("1v1 Shooter")
screen = pygame.display.set_mode((1080, 780))

# Status der Main Loop (weitermachen solange True)
running = True

# Die Main Loop (Game Loop)
while running:
    # Jedes Ereignis (Event) durchgehen
 for event in pygame.event.get():
    # Das Spiel verlassen, falls der Benutzer das Fenster schließen möchte
 if event.type == pygame.QUIT:
    running = False

 # Weitere Events abfragen (z.B. Tastatureingaben)
 # Update der Spiellogik
 # Neu zeichnen der Grafiken
 # Das Display updaten
 pygame.display.flip()
# PyGame sauber beenden (cleanup)
pygame.quit()
