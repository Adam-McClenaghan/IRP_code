import pygame
import win32api
import win32con
import win32gui

pygame.init()
screen = pygame.display.set_mode((800, 600)) # For borderless, use pygame.NOFRAME
done = False
Transparent = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)

# Set window transparency color
hwnd = pygame.display.get_wm_info() #["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*Transparent), 0, win32con.LWA_COLORKEY)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(Transparent)  # Transparent background
    pygame.draw.rect(screen, dark_red, pygame.Rect(30, 30, 60, 60))
    pygame.display.update()