
import pygame, sys
 
GAME_SPEED = 60
LOGO_SPEED = 3
BACKGROUND_COLOR = (0, 0, 0)
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Space War')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
 
font = pygame.font.SysFont(None, 40)
fontTitel = pygame.font.SysFont(None, 80)

 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

#Function for main menu (Danny)
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('SpaceWar', fontTitel, (255, 255, 255), screen, SCREEN_WIDTH/2 -130, 20)

        mx, my = pygame.mouse.get_pos()
        #Button to start the game 
        #Position "START" Button 
        draw_text('START', font, (255, 255, 255), screen, SCREEN_WIDTH/2 - 40, 160)
        button_1 = pygame.Rect(SCREEN_WIDTH/2 - 100, 200, 200, 50)  
        #Button to exit the game
        #Position "EXIT" Button 
        draw_text('EXIT', font, (255, 255, 255), screen, SCREEN_WIDTH/2 - 30, 310)
        button_2 = pygame.Rect(SCREEN_WIDTH/2 - 100, 350, 200, 50)
        if button_1.collidepoint((mx, my)):
            #if the user clicks on the "Start" button open the game function 
            if click:
                game()
        if button_2.collidepoint((mx, my)):
             #if the user clicks on the "Exit" button close the game
            if click:
             pygame.quit()
             sys.exit()
        #Color "START" Button 
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        #Color "EXIT" Button 
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                #if the escape key in pressed while in the main menu close the game 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
     

#Spel van Mark als voorbeeld waar het spel terecht moet komen 
        logo = pygame.image.load("images/ra_logo.png").convert_alpha()
        logo_rect = logo.get_rect()
        logo_speed = [LOGO_SPEED, LOGO_SPEED]
        while not quit_game_requested():
            screen.fill(BACKGROUND_COLOR)
            bounce_if_required(logo_speed, logo_rect)
            logo_rect = logo_rect.move(logo_speed)
            screen.blit(logo, logo_rect)
            pygame.display.flip()
            mainClock.tick(GAME_SPEED)


 
#quit_game_requested kan verwijderd worden is van het voorbeeld van mark

def quit_game_requested():
    halting = False
    # De lijst met "events" is een lijst met alle gebeurtenissen die
    # plaatsvonden sinds de vorige loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting

#bounce_if_required kan verwijderd worden is van het voorbeeld van mark

def bounce_if_required(speed_tuple, position_rect):
    # Linkerkant van het scherm geraakt?
    if position_rect.left <= 0:
        speed_tuple[0] = LOGO_SPEED
    # Rechterkant van het scherm geraakt?
    elif position_rect.right >= SCREEN_WIDTH:
        speed_tuple[0] = -LOGO_SPEED

    # Bovenkant van het scherm geraakt?
    if position_rect.top <= 0:
        speed_tuple[1] = LOGO_SPEED
    # Onderkant van het scherm geraakt?
    elif position_rect.bottom >= SCREEN_HEIGHT:
        speed_tuple[1] = -LOGO_SPEED




main_menu()