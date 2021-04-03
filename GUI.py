# BCI GUI

import File_watcher
import pygame
from pygame.locals import *
pygame.init()

# Defining sizes and font
WIDTH, HEIGHT = 800, 800    
BACKGROUND = (0, 0, 0) #black
WHITE = (255, 255, 255)
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 40)

STIM = [5, 6, 7, 8]

# Displaying window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption("BCI Menus")

def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_window():
    WIN.fill(BACKGROUND)

button_1 = pygame.Rect(150, 350, 100, 100)
button_2 = pygame.Rect(550, 350, 100, 100)
button_3 = pygame.Rect(350, 150, 100, 100)
button_4 = pygame.Rect(350, 550, 100, 100)

def get_inputfreq():
    filename = '/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.CSV'
    f = open(filename)
    reg_val = int(f.read(1))
    print(reg_val)
    if reg_val == STIM[0]:
        Menu_1()
    elif reg_val == STIM[1]:
        Menu_2()
    elif reg_val == STIM[2]:
        Menu_3()
    elif reg_val == STIM[3]:
        Menu_4()

# Main menu loop 
def main_menu():
    
    FPS = 60
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(FPS)
        draw_window()
        draw_text('main menu', font, WHITE , WIN, 20, 20)

        pygame.draw.rect(WIN, RED, button_1)
        pygame.draw.rect(WIN, RED, button_2)
        pygame.draw.rect(WIN, RED, button_3)
        pygame.draw.rect(WIN, RED, button_4)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    get_inputfreq()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Menu_1()
                
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    Menu_2()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    Menu_3()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    Menu_4()

        pygame.display.update()

# Define submenus
def Menu_1():
    running = True
    while running:
        draw_window()
        draw_text('Menu 5Hz', font, WHITE , WIN, 20, 20)

        pygame.draw.rect(WIN, (255, 0 , 0), button_1)
        pygame.draw.rect(WIN, (255, 0 , 0), button_2)
        pygame.draw.rect(WIN, (255, 0 , 0), button_3)
        pygame.draw.rect(WIN, (255, 0 , 0), button_4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    running = False
                elif event.key == K_BACKSPACE:
                    running = False

        pygame.display.update()

def Menu_2():
    running = True
    while running:

        draw_window()
        draw_text('Menu 6Hz', font, WHITE , WIN, 20, 20)

        pygame.draw.rect(WIN, (255, 0 , 0), button_1)
        pygame.draw.rect(WIN, (255, 0 , 0), button_2)
        pygame.draw.rect(WIN, (255, 0 , 0), button_3)
        pygame.draw.rect(WIN, (255, 0 , 0), button_4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_UP:
                    running = False

        pygame.display.update()


def Menu_3():
    running = True
    while running:

        draw_window()
        draw_text('Menu 7Hz', font, WHITE , WIN, 20, 20)

        pygame.draw.rect(WIN, (255, 0 , 0), button_1)
        pygame.draw.rect(WIN, (255, 0 , 0), button_2)
        pygame.draw.rect(WIN, (255, 0 , 0), button_3)
        pygame.draw.rect(WIN, (255, 0 , 0), button_4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_RIGHT:
                    running = False

        pygame.display.update()


def Menu_4():
    running = True
    while running:

        draw_window()
        draw_text('Menu 8Hz', font, WHITE , WIN, 20, 20)

        pygame.draw.rect(WIN, (255, 0 , 0), button_1)
        pygame.draw.rect(WIN, (255, 0 , 0), button_2)
        pygame.draw.rect(WIN, (255, 0 , 0), button_3)
        pygame.draw.rect(WIN, (255, 0 , 0), button_4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_LEFT:
                    running = False

        pygame.display.update()
                    
main_menu()
