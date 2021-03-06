# BCI GUI for dataset 2, 8 stimuli
import math
import os
import pygame
from pygame.locals import *
import win32api
import win32con
import win32gui
import Aerofoil_point_gen
import Cambered_aero
pygame.init()

# Defining sizes and font
# WIDTH, HEIGHT = 800, 800  
WIDTH, HEIGHT = pygame.display.Info().current_w - 100, pygame.display.Info().current_h - 150
BACKGROUND = (0, 0, 0) #black
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
TRAN = (255, 0, 128)
font = pygame.font.SysFont(None, 40)
option_font = pygame.font.SysFont(None, 25)
BUTTON_HEIGHT = 100
BUTTON_WIDTH = 100
Chord_length = 100
Thickness = 10
Extrude_thickness = 100
M = 0.02
P = 0.4
Max_len_dia = pygame.image.load('Max_len_dia.png')
Max_thick_dia = pygame.image.load('Max_thick_dia.png')
M_dia = pygame.image.load('M_diagram.png')
P_dia = pygame.image.load('P_diagram.png')




STIM = [8, 9, 10, 11, 12, 13, 14, 15]

# Displaying window size
WIN = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
pygame.display.set_caption("BCI Menus")


def Image(Image, width, height, x,y):
    Resized = pygame.transform.smoothscale(Image, (width, height))
    WIN.blit(Resized, (x,y))


# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*TRAN), 0, win32con.LWA_COLORKEY)

# Set window transparency colour 
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*TRAN), 0, win32con.LWA_COLORKEY)

def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_window():
    WIN.fill(TRAN)
    # WIN.fill(BLACK)

def Get_aero_ID():
    global Thickness
    global Chord_length
    global M
    global P
    Suffix = 'NACA'
    xx = int(Chord_length / Thickness)
    Suffix += str(round(M * 100))
    Suffix += str(round(P * 10))
    Suffix += str(xx)
    return Suffix
 

Main_menu_loc = {
    '8' : [150, 150],
    '9' : [WIDTH - (150 + BUTTON_WIDTH), 150],
    '10': [150, HEIGHT - (150 + BUTTON_HEIGHT)],
    '11': [WIDTH - (150 + BUTTON_WIDTH), HEIGHT - (150 + BUTTON_HEIGHT)]
}

Loc_1 = {
    '8' : [125, 125],
    '9' : [350, 125],
    '10' : [575, 125],
    '11' : [125, 350],
    '12' : [575, 350],
    '13' : [125, 575],
    '14' : [350, 575],
    '15' : [575, 575]
}

Loc_2 = {
    '8' : [50, 50],
    '9' : [WIDTH - (50 + BUTTON_WIDTH), 50],
    '10' : [50, HEIGHT / 2 - (BUTTON_HEIGHT / 2)],
    '11' : [WIDTH - (50 + BUTTON_WIDTH), HEIGHT / 2 - (BUTTON_HEIGHT / 2)],
    '12' : [50, HEIGHT - (50 + BUTTON_HEIGHT)],
    '13' : [WIDTH - (50 + BUTTON_WIDTH), HEIGHT - (50 + BUTTON_HEIGHT)],
    '14' : [WIDTH / 2 - (BUTTON_WIDTH / 2), 50],
    '15' : [WIDTH / 2 - (BUTTON_WIDTH / 2), HEIGHT - (50 + BUTTON_HEIGHT)]
}

AeroFoil_locs = {
    '8' : [50, 50],
    '9' : [WIDTH - (50 + BUTTON_WIDTH), 50],
    '10' : [50, HEIGHT / 2 - (BUTTON_HEIGHT / 2)],
    '11' : [WIDTH - (50 + BUTTON_WIDTH), HEIGHT / 2 - (BUTTON_HEIGHT / 2)],
    '12' : [WIDTH / 2 - (150 + BUTTON_HEIGHT), 50],
    '13' : [WIDTH /2 + 150, 50],
    '14' : [WIDTH / 2 - 125, 100],
    '15' : [WIDTH / 2 - (BUTTON_WIDTH / 2), HEIGHT - (50 + BUTTON_HEIGHT)]
}


# Button creation
def Main_Button(freq, x, y, count, phase_off): #Phase offset in terms of pi
    Bri = 0.5 * (1+ math.sin(2 * math.pi * freq *(count / 60) + phase_off * math.pi))
    button_param = pygame.Rect(x, y, BUTTON_HEIGHT, BUTTON_WIDTH)
    rgb_colour = round(Bri * 255.0)
    colour = (rgb_colour, rgb_colour, rgb_colour)
    pygame.draw.rect(WIN, colour, button_param)

def Button(freq, dict, count, phase_off): #Phase offset in terms of pi
    Bri = 0.5 * (1+ math.sin(2 * math.pi * freq *(count / 60) + phase_off * math.pi))
    x, y = dict[str(freq)]
    button_param = pygame.Rect(x, y, BUTTON_HEIGHT, BUTTON_WIDTH)
    rgb_colour = round(Bri * 255.0)
    colour = (rgb_colour, rgb_colour, rgb_colour)
    # pygame.draw.rect(WIN, colour, button_param)
    pygame.draw.rect(WIN, BLACK, button_param)

#Add text on top of buttons  
def addText(freq, dict, Text): # x and y correspond to coords of button to place text on
    x, y = dict[str(freq)]
    global BUTTON_HEIGHT
    global BUTTON_WIDTH
    WIN.blit(option_font.render(Text, True, RED), (x + 20, y + BUTTON_HEIGHT/2))

def Value_text(Text, x, y):
    WIN.blit(option_font.render(Text, True, RED), (x, y))

def Disp_aero_ID(x,y):
    Classification = Get_aero_ID()
    draw_text('Aerofoil ID: ' + Classification, font, BLACK, WIN, x, y)


  
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
            pygame.draw.rect(WIN, GREEN, 125, 125, BUTTON_WIDTH, BUTTON_HEIGHT, 3)
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
        
def manual_freq(frequency):
    f = open('/Users/Adam/Desktop/IRP_CODE/GUI_outcome.csv', 'w')
    f.write(str(frequency))

def correct_guess(freq, dict, colour):
    x, y = dict[str(freq)]
    pygame.draw.rect(WIN, colour, (x, y, BUTTON_WIDTH + 10, BUTTON_HEIGHT + 10), 30)





# Main menu loop 
def main_menu():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    
    
    while True:
        clock.tick(FPS)
        draw_window()
        # draw_text('Main menu', font, WHITE , WIN, 330, 400)
        if count >= FPS: count = 0
        
        Main_Button(8, 150, 150, count, 0)
        Main_Button(9, WIDTH - (150 + BUTTON_WIDTH), 150, count, 1)
        Main_Button(10, 150, HEIGHT - (150 + BUTTON_HEIGHT), count, 0.5)
        Main_Button(11, WIDTH - (150 + BUTTON_WIDTH), HEIGHT - (150 + BUTTON_HEIGHT), count, 1.5)

        addText(8, Main_menu_loc, "Menu 8Hz")
        addText(9, Main_menu_loc, "Menu 9Hz")
        addText(10, Main_menu_loc, "Menu 10Hz")
        addText(11, Main_menu_loc, "Menu 11Hz")
        
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
        # draw_text('Menu 8Hz', font, WHITE , WIN, 320, 400)
        if sub_count >= 60: sub_count = 0

        Button(8, Loc_1, sub_count, 0)
        Button(9, Loc_1, sub_count, 0.25)
        Button(10, Loc_1, sub_count, 0.5)
        Button(11, Loc_1, sub_count, 0.75)
        Button(12, Loc_1, sub_count, 1)
        Button(13, Loc_1, sub_count, 1.25)
        Button(14, Loc_1, sub_count, 1.5)
        Button(15, Loc_1, sub_count, 1.75)

        addText(8, Loc_1, 'Top view (8)')
        addText("Bottom view (9)", 350, 125)
        addText("Front view (10)", 575, 125)
        addText("Back view (11)", 125, 350)
        addText("Left view (12)", 575, 350)
        addText("Right view (13)", 125, 575)
        addText("Previous view (14)", 350, 575)
        addText("Back (15)", 575, 575)

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
    sub_count = 0
    running = True
    while running:
        clock.tick(FPS)
        draw_window()
        # draw_text('X', font, WHITE , WIN, 400, 175)
        # draw_text('Y', font, WHITE , WIN, 400, 375)
        # draw_text('Z', font, WHITE , WIN, 400, 575)
        if sub_count >= 60: sub_count = 0

        Button(8, Loc_2, sub_count, 0)
        Button(9, Loc_2, sub_count, 0.25)
        Button(10, Loc_2, sub_count, 0.5)
        Button(11, Loc_2, sub_count, 0.75)
        Button(12, Loc_2, sub_count, 1)
        Button(13, Loc_2, sub_count, 1.25)
        Button(14, Loc_2, sub_count, 1.5)
        Button(15, Loc_2, sub_count, 1.75)

        addText(8, Loc_2, '<< X (8)')
        addText(9, Loc_2, " X >> (9)")
        addText(10, Loc_2, "<< Y (10)")
        addText(11, Loc_2, "Y >> (11)")
        addText(12, Loc_2, "<< Z (12)")
        addText(13, Loc_2, "Z >> (13)")
        addText(14, Loc_2, "In (14)")
        addText(15, Loc_2, "Out (15)")

        if os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv') > Last_mod:
            Submenu_freq()
            running = Submenu_freq.outcome

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    running = False
                elif event.key == K_ESCAPE:
                    running = False
                elif event.key == K_1:
                    manual_freq(8)
                    correct_guess(8, Loc_2, RED)
                elif event.key == K_2:
                    manual_freq(9)
                    correct_guess(9, Loc_2, RED)
                elif event.key == K_3:
                    manual_freq(10)
                    correct_guess(10, Loc_2, RED)
                elif event.key == K_4:
                    manual_freq(11)
                    correct_guess(11, Loc_2, RED)
                elif event.key == K_5:
                    manual_freq(12)
                    correct_guess(12, Loc_2, RED)
                elif event.key == K_6:
                    manual_freq(13)
                    correct_guess(13, Loc_2, RED)
                elif event.key == K_7:
                    manual_freq(14)
                    correct_guess(14, Loc_2, RED)
                elif event.key == K_8:
                    manual_freq(15)
                    correct_guess(15, Loc_2, RED)
        sub_count += 1
        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        pygame.display.update()

def Menu_3():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    running = True
    global Chord_length
    global Thickness
    global Extrude_thickness 
    global M 
    global P

    Thick_change = 1
    Chord_change = 10
    Extrude_change = 10

    while running:
        clock.tick(FPS)
        draw_window()
        # draw_text('Aerofoil Generator', font, WHITE , WIN, 20, 20)
        if count >= 60: count = 0

        Button(8, AeroFoil_locs, count, 0)
        Button(9, AeroFoil_locs, count, 0.25)
        Button(10, AeroFoil_locs, count, 0.5)
        Button(11, AeroFoil_locs, count, 0.75)
        Button(12, AeroFoil_locs, count, 1)
        Button(13, AeroFoil_locs, count, 1.25)
        # Button(14, AeroFoil_locs, count, 1.5)
        Button(15, AeroFoil_locs, count, 1.75)

        Image(Max_len_dia, 200, 100, 50, 200)
        Image(Max_thick_dia, 200, 100, WIDTH - 50 - 200, 200)
        Value_text('C = ' + str(Chord_length), 150, 200)
        Value_text('T = ' + str(Thickness), WIDTH - 150, 240)
        Disp_aero_ID(WIDTH / 2 - 150, HEIGHT - 200)
        
        addText(8, Loc_2, 'UP')
        addText(10, Loc_2,'DOWN')
        addText(9, Loc_2, 'UP')
        addText(11, Loc_2, 'DOWN')
        addText(12, AeroFoil_locs, 'UP')
        addText(13, AeroFoil_locs, 'DOWN')
        addText(14, AeroFoil_locs, ' Extrude thickness = ' + str(Extrude_thickness))
        addText(15, AeroFoil_locs, 'Generate')

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
                elif event.key == K_1:
                    Chord_length += Chord_change
                elif event.key == K_2:
                    Chord_length -= Chord_change
                elif event.key == K_3:
                    Thickness += Thick_change
                elif event.key == K_4:
                    Thickness -= Thick_change
                elif event.key == K_5:
                    Extrude_thickness += Extrude_change
                elif event.key == K_6:
                    Extrude_thickness -= Extrude_change
                elif event.key == K_7:
                    Menu_4()
                    correct_guess(14, Loc_2, RED)
                elif event.key == K_8:
                    Cambered_aero.Cambered_aero(Chord_length, Thickness, M, P)
        count += 1
        Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
        pygame.display.update()


def Menu_4():
    Last_mod = os.path.getmtime('C:/Users/Adam/Documents/MENG_yr3/IRP_papers/pytest.csv')
    FPS = 60
    clock = pygame.time.Clock()
    count = 0
    running = True
    global M
    global P
    global Extrude_thickness

    M_change = 0.01
    P_change = 0.1
    Extrude_change = 10
    
    while running:
        clock.tick(FPS)
        draw_window()
        draw_text('Camber settings', font, WHITE , WIN, 20, 20)
        if count >= 60: count = 0

        Button(8, AeroFoil_locs, count, 0)
        Button(9, AeroFoil_locs, count, 0.25)
        Button(10, AeroFoil_locs, count, 0.5)
        Button(11, AeroFoil_locs, count, 0.75)
        # Button(12, AeroFoil_locs, count, 1)
        # Button(13, AeroFoil_locs, count, 1.25)
        # Button(14, AeroFoil_locs, count, 1.5)
        Button(15, AeroFoil_locs, count, 1.75)

        Image(P_dia, 250, 100, WIDTH - 50 - 200, 200)
        Image(M_dia, 250, 100, 50, 200)
        Value_text('M = ' + str(round(M * 100)) + '%', 235, 210)
        Value_text('P = ' + str(round(P * 100)) + '%', WIDTH - 100, 270)
        addText(8, AeroFoil_locs, 'Up')
        addText(9, AeroFoil_locs, 'Up')
        addText(10, AeroFoil_locs, 'Down')
        addText(11, AeroFoil_locs, 'Down')
        addText(15, AeroFoil_locs, 'Back')


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_RIGHT:
                    running = False
                elif event.key == K_1:
                    M += M_change
                elif event.key == K_2:
                    M -= M_change
                elif event.key == K_3:
                    P += P_change
                elif event.key == K_4:
                    P -= P_change
                elif event.key == K_5:
                    Extrude_thickness += Extrude_change
                elif event.key == K_6:
                    Extrude_thickness -= Extrude_change
                elif event.key == K_7:
                    Menu_4()
                    correct_guess(14, Loc_2, RED)
                elif event.key == K_8:
                    running = False

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
