import pygame
# Initialisierung
pygame.init()
pygame.display.set_caption("Hello pygame")
screen = pygame.display.set_mode((640, 480))
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
