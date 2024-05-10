import pygame
from deps import grid
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BOX_SIZE = 800
TILE_SIZE = 80

if __name__ == "__main__":
    pygame.init()
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.set_caption("Automata")
    Game = grid.Grid(2, 3, 3, BOX_SIZE, TILE_SIZE)
    
    
    Game.set(1, 2)
    Game.set(2, 2)
    Game.set(3, 2)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # screen.fill((255, 255, 255))
        
        Game.print()
        Game.simulate()
        time.sleep(1)
        
        
        # pygame.display.flip()

    pygame.quit()