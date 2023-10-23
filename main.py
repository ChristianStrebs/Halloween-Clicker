import pygame
import sys
from game import Game

pygame.init()
main_clock = pygame.time.Clock()
height = 720
width = 1280
SCREEN = pygame.display.set_mode((width, height))
BG = pygame.image.load("background.jpg")
BG = pygame.transform.scale(BG, (width, height))
oj_button = pygame.image.load("Oj.png")
gameBG = pygame.image.load("gameBG3.jpg")
gameBG = pygame.transform.scale(gameBG, (width, height))
treeButton = pygame.image.load("tree2nobg.png")
game= Game()
game.run()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        pygame.display.set_caption("Main Menu")
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        MENU_TEXT = MENU_TEXT.render("Save Christmas!", True, "white")
        MENU_TEXT_RECT = MENU_TEXT.get_rect()
        MENU_TEXT_RECT.center = (width/2, 100)
        
        SCREEN.blit(MENU_TEXT, MENU_TEXT_RECT)

        oj_button_rect = oj_button.get_rect()
        oj_button_rect.center = (width/2, height/2)
        SCREEN.blit(oj_button, oj_button_rect)

        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if oj_button_rect.collidepoint(MENU_MOUSE_POS):
                    
                    play()
                    
                
        
        pygame.display.update()



        



def play():
    pygame.display.set_caption("Play")
    
    while True:
        main_clock.tick(600)
        game.run()
        #elf
        elfButton = pygame.Rect(300, 100, 100, 100)
        elfButton.center = (300, 100)
        SCREEN.blit(SCREEN, (300, 100))

        
        #Tree
        SCREEN.blit(gameBG, (0, 0))
        treeButton_rect = treeButton.get_rect()
        treeButton_rect.center = (300, 400)
        SCREEN.blit(treeButton, treeButton_rect)
        
        #presents text
        PRESENTS_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        PRESENTS_TEXT = PRESENTS_TEXT.render(f"Presents: {str(game.get_presents())}", True, "white")
        PRESENTS_TEXT_RECT = PRESENTS_TEXT.get_rect()
        PRESENTS_TEXT_RECT.center = (width/2, 100)
        SCREEN.blit(PRESENTS_TEXT, PRESENTS_TEXT_RECT)

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if treeButton_rect.collidepoint(pygame.mouse.get_pos()):
                    game.clicked_tree()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    shop()
                
        
        
        pygame.display.update()

        

def shop():
    
    pygame.display.set_caption("Shop")
    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                play()
        pygame.display.update()


main_menu()
