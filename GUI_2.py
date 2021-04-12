# BCI GUI for dataset 2, 8 stimuli
import math
import os
import pygame
from pygame.locals import *
pygame.init()

# Defining sizes and font
WIDTH, HEIGHT = 800, 800    
BACKGROUND = (0, 0, 0) #black
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 40)
option_font = pygame.font.SysFont(None, 25)
BUTTON_HEIGHT = 100
BUTTON_WIDTH = 100


STIM = [8, 9, 10, 11, 12, 13, 14, 15]

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

# Button creation
def Button(freq, x, y, count, phase_off): #Phase offset in terms of pi
    Bri = 0.5 * (1+ math.sin(2 * math.pi * freq *(count / 60) + phase_off * math.pi))
    button_param = pygame.Rect(x, y, BUTTON_HEIGHT, BUTTON_WIDTH)
    rgb_colour = round(Bri * 255.0)
    colour = (rgb_colour, rgb_colour, rgb_colour)
    pygame.draw.rect(WIN, colour, button_param)

#Add text on top of buttons  
def addText(Text, x, y): # x and y correspond to coords of button to place text on
    global BUTTON_HEIGHT
    global BUTTON_WIDTH
    WIN.blit(option_font.render(Text, True, RED), (x + (BUTTON_WIDTH - (len(Text) * 11)), y + BUTTON_HEIGHT/2))
    

#Compares input frequency to stimulus frequencies
def get_inputfreq():
    filename = '/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.CSV'
    f = open(filename, "r")

    val = (f.read(2))
    strippedval = val.strip()
    excel_val = str(strippedval)
    if excel_val.isdigit() == True:
        reg_val = int(excel_val)
         
        if reg_val == STIM[0]:
            Menu_1()
        elif reg_val == STIM[1]:
            Menu_2()
        elif reg_val == STIM[2]:
            Menu_3()
        elif reg_val == STIM[3]:
            Menu_4()

    else:
        print('no value detected',  type(excel_val), excel_val)

def Submenu_freq():
    filename = '/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.CSV'
    f = open(filename)
    Submenu_freq.outcome = True

    val = (f.read(2))
    stripped_val = val.strip()
    excel_val = str(stripped_val)
    if excel_val.isdigit():
        reg_val = int(excel_val)
        if reg_val == STIM[0]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('8')
        elif reg_val == STIM[1]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('9')
        elif reg_val == STIM[2]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('10')
        elif reg_val == STIM[3]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('11')
        elif reg_val == STIM[4]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('12')
        elif reg_val == STIM[5]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('13')
        elif reg_val == STIM[6]:
            f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
            f.write('14')
        elif reg_val == STIM[7]:
            Submenu_freq.outcome = False


# Main menu loop 
def main_menu():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    
    
    while True:
        clock.tick(FPS)
        draw_window()
        draw_text('Main menu', font, WHITE , WIN, 330, 400)
        if count >= FPS: count = 0
        
        Button(8, 150, 350, count, 0)
        Button(9, 550, 350, count, 1)
        Button(10, 350, 150, count, 0.5)
        Button(11, 350, 550, count, 1.5)

        addText("Menu 10Hz", 150, 350)
        addText("Menu 9Hz", 550, 350)
        addText("Menu 8Hz", 350, 150)
        addText("Menu 11Hz", 350, 550)
        
        #compare time of last update and opens file
        if os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv') > Last_mod:
            get_inputfreq()

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

        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        count += 1
        #print(count)
        pygame.display.update()

# Define submenus
def Menu_1():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    sub_count = 0
    running = True
    while running:
        clock.tick(FPS)
        draw_window()
        draw_text('Menu 8Hz', font, WHITE , WIN, 320, 400)
        if sub_count >= 60: sub_count = 0

        Button(8, 125, 125, sub_count, 0)
        Button(9, 350, 125, sub_count, 0.25)
        Button(10, 575, 125, sub_count, 0.5)
        Button(11, 125, 350, sub_count, 0.75)
        Button(12, 575, 350, sub_count, 1)
        Button(13, 125, 575, sub_count, 1.25)
        Button(14, 350, 575, sub_count, 1.5)
        Button(15, 575, 575, sub_count, 1.75)

        addText("Option 1", 125, 125)
        addText("Option 2", 350, 125)
        addText("Option 3", 575, 125)
        addText("Option 4", 125, 350)
        addText("Option 5", 575, 350)
        addText("Option 6", 125, 575)
        addText("Option 7", 350, 575)
        addText("Back", 575, 575)

        if os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv') > Last_mod:
            Submenu_freq()
            running = Submenu_freq.outcome

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    running = False
                elif event.key == K_BACKSPACE:
                    running = False
        sub_count += 1
        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        pygame.display.update()


def Menu_2():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    running = True
    while running:
        clock.tick(FPS)
        draw_window()
        draw_text('Menu 6Hz', font, WHITE , WIN, 20, 20)
        if count >= 60: count = 0

        Button(4, 150, 350, count, 0)
        Button(3, 550, 350, count, 0)
        Button(2, 350, 150, count, 0)
        Button(1, 350, 550, count, 0)

        addText("Option 1", 160, 400)
        addText("Option 2", 560, 400)
        addText("Option 3", 360, 200)
        addText("Back", 380, 600)

        if os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv') > Last_mod:
            Submenu_freq()
            running = Submenu_freq.outcome

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_UP:
                    running = False
        count += 1
        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        pygame.display.update()


def Menu_3():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    running = True
    while running:
        clock.tick(FPS)
        draw_window()
        draw_text('Menu 7Hz', font, WHITE , WIN, 20, 20)
        if count >= 60: count = 0

        Button(5, 150, 350, count, 0)
        Button(6, 550, 350, count, 0)
        Button(7, 350, 150, count, 0)
        Button(8, 350, 550, count, 0)

        addText("Option 1", 160, 400)
        addText("Option 2", 560, 400)
        addText("Option 3", 360, 200)
        addText("Back", 380, 600)

        if os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv') > Last_mod:
            Submenu_freq()
            running = Submenu_freq.outcome

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_RIGHT:
                    running = False
        count += 1
        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        pygame.display.update()


def Menu_4():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    running = True
    while running:
        clock.tick(FPS)
        draw_window()
        draw_text('Menu 8Hz', font, WHITE , WIN, 20, 20)
        if count >= 60: count = 0

        Button(5, 150, 350, count, 0)
        Button(6, 550, 350, count, 0)
        Button(7, 350, 150, count, 0)
        Button(8, 350, 550, count, 0)

        addText("Option 1", 160, 400)
        addText("Option 2", 560, 400)
        addText("Option 3", 360, 200)
        addText("Back", 380, 600)

        if os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv') > Last_mod:
            Submenu_freq()
            running = Submenu_freq.outcome

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_LEFT:
                    running = False
        count += 1
        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        pygame.display.update()

#Watch_func()

main_menu()
