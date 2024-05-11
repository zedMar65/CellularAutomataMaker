import pygame
from deps import grid
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BOX_SIZE = 800
TILE_SIZE = 20
CELL_COLOR = (55, 0, 0)
SECONDARY_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
CELL_SIZE = TILE_SIZE
BUTTON1 = [BOX_SIZE +10, 10, SCREEN_WIDTH-BOX_SIZE-20, 80]
BUTTON2 = [BOX_SIZE +10, 100, SCREEN_WIDTH-BOX_SIZE-20, 80]

# Function to paint alive cells:
def paintCells(cells, screen):
    for cell in cells:
        pygame.draw.rect(screen, CELL_COLOR, pygame.Rect(cell[0]*CELL_SIZE, cell[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # draw a line and a start/stop/1 step button:
    pygame.draw.rect(screen, SECONDARY_COLOR, pygame.Rect(BOX_SIZE, 0, 5, SCREEN_HEIGHT))
    pygame.draw.rect(screen, SECONDARY_COLOR, pygame.Rect(BUTTON1))
    pygame.draw.rect(screen, SECONDARY_COLOR, pygame.Rect(BUTTON2))
    font = pygame.font.Font(None, 36)
    text1 = font.render('Start/Stop', True, BACKGROUND_COLOR)
    text2 = font.render('1 Step', True, BACKGROUND_COLOR)
    text_rect1 = text1.get_rect(center=(BUTTON1[0]+BUTTON1[2]//2, BUTTON1[1]+BUTTON1[3]//2))
    text_rect2 = text2.get_rect(center=(BUTTON2[0]+BUTTON2[2]//2, BUTTON2[1]+BUTTON2[3]//2))
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
    
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Automata")
    Game = grid.Grid(2, 3, 3, BOX_SIZE, TILE_SIZE)  
    StartTime = time.time()
    running = True
    Simulating = [False, False]
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
              # set cells to alive
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # check for button presses
                    if pos[0] > BOX_SIZE:
                        if pos[0] >= BUTTON1[0] and pos[0] <= BUTTON1[0]+BUTTON1[2]:
                            if pos[1] >=10 and pos[1] <= 90:
                                if Simulating[0]:
                                    Simulating = [False, False]
                                else:
                                    Simulating = [True, True]
                            elif pos[1] >=100 and pos[1] <= 180:
                                Simulating = [True, False]
                    else:
                        Game.set(int(pos[0]/TILE_SIZE)+1, int(pos[1]/TILE_SIZE)+1)
            # Itteration loop ewery .5 seconds
            if time.time()-0.5 >= StartTime:
                StartTime = time.time()
                screen.fill(BACKGROUND_COLOR)

                # main loop
                if Simulating[0] and Simulating[1]:
                    Game.simulate()
                elif Simulating[0] and not Simulating[1]:
                    Game.simulate()
                    Simulating[0] = False
                    
            # screen update
            paintCells(Game.cells, screen)
            pygame.display.flip()
        except KeyboardInterrupt:
            running = False
        except Exception as e:
            print(e)

    pygame.quit()