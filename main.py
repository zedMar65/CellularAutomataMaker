import pygame
from deps import grid
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BOX_SIZE = 800
TILE_SIZE = 50
CELL_COLOR = (55, 0, 0)
SECONDARY_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
CELL_SIZE = TILE_SIZE


# Function to paint alive cells:
def paintCells(cells, screen):
    for cell in cells:
        pygame.draw.rect(screen, CELL_COLOR, pygame.Rect(cell[0]*CELL_SIZE, cell[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # draw a line and a start/stop/1 step button:
    pygame.draw.rect(screen, SECONDARY_COLOR, pygame.Rect(BOX_SIZE, 0, 5, SCREEN_HEIGHT))
    




if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Automata")
    Game = grid.Grid(2, 3, 3, BOX_SIZE, TILE_SIZE)  
    StartTime = time.time()
    running = True
    Simulating = False
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
              # set cells to alive
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    Game.set(int(pos[0]/TILE_SIZE)+1, int(pos[1]/TILE_SIZE)+1)
            # Itteration loop ewery .5 seconds
            if time.time()-0.5 >= StartTime:
                StartTime = time.time()
                screen.fill(BACKGROUND_COLOR)

                # main loop
                if Simulating:
                    Game.simulate()
                    
            # screen update
            paintCells(Game.cells, screen)
            pygame.display.flip()
        except KeyboardInterrupt:
            running = False
        except Exception as e:
            print(e)

    pygame.quit()