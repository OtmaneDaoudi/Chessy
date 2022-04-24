import pygame
import os

WIDTH,HEIGHT = 900,500
BACKGROUND_COLOR = (128,128,128)
FPS = 60

#may cause an error with other plateforms depending on path separation
BOARD_IMAGE = pygame.image.load('Assets/board.png') 

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Chess')

def draw_window():
    WIN.fill(BACKGROUND_COLOR)
    WIN.blit(BOARD_IMAGE,(0,0)) #draw image
    pygame.display.update() #update the windows with all the drawings


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)  #set game fps = 60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window() #call draw function to draw all the stuff we want 
        
    pygame.quit()

if __name__ == '__main__':
    main()