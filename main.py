import pygame
import sys
from game import Game
import time

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
shopButton = pygame.image.load("shopIcon.png")
shopButton = pygame.transform.scale(shopButton, (50, 50))
shopBorder = pygame.image.load("shopBorder.png")
shopBorder = pygame.transform.scale(shopBorder, (width, height))
presents1 = pygame.image.load("presents.png")
presents1 = pygame.transform.scale(presents1, (300, 200))
presents2 = pygame.image.load("presents2.png")
presents2 = pygame.transform.scale(presents2, (300, 200))
presents3 = pygame.image.load("presents4.png")
presents3 = pygame.transform.scale(presents3, (300, 200))
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
        

        #shop button
        shopButton_rect = shopButton.get_rect()
        shopButton_rect.center = (1200, 100)
        SCREEN.blit(shopButton, shopButton_rect)

        #adding presents to the screen for certain presents increments
        if game.get_presents() >= 1000:
            SCREEN.blit(presents1, (300, 550))
        if game.get_presents() >= 10000:
            SCREEN.blit(presents2, (0, 550))
        if game.get_presents() >= 100000:
            SCREEN.blit(presents3, (550, 500))
        if game.get_presents() >= 1000000:
            SCREEN.blit(presents1, (650, 550))
        if game.get_presents() >= 10000000:
            SCREEN.blit(presents3, (800, 500))
        

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if treeButton_rect.collidepoint(pygame.mouse.get_pos()):
                    game.clicked_tree()
                    pygame.display.update()
                if shopButton_rect.collidepoint(pygame.mouse.get_pos()):
                    shop()
                    pygame.display.update()
                
        
        
        pygame.display.update()

        

def shop():
    
    pygame.display.set_caption("Shop")
    while True:
        pygame.draw.rect(SCREEN, (150, 0, 20), (175, 70, 950, 550))
        SCREEN.blit(shopBorder, (0, 0))


        ELF_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        ELF_TEXT = ELF_TEXT.render(f"Elves: {str(game.get_elves())}", True, "white")
        ELF_TEXT_RECT = ELF_TEXT.get_rect()
        ELF_TEXT_RECT.center = (400, 200)
        SCREEN.blit(ELF_TEXT, ELF_TEXT_RECT)
        BUY_ELF_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUY_ELF_TEXT = BUY_ELF_TEXT.render(f"Buy Elf", True, "white")
        BUY_ELF_TEXT_RECT = BUY_ELF_TEXT.get_rect()
        BUY_ELF_TEXT_RECT.center = (400, 250)
        SCREEN.blit(BUY_ELF_TEXT, BUY_ELF_TEXT_RECT)
    

        SANTA_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        SANTA_TEXT = SANTA_TEXT.render(f"Santa: {str(game.get_santas())}", True, "white")
        SANTA_TEXT_RECT = SANTA_TEXT.get_rect()
        SANTA_TEXT_RECT.center = (400, 300)
        SCREEN.blit(SANTA_TEXT, SANTA_TEXT_RECT)
        BUT_SANTA_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUT_SANTA_TEXT = BUT_SANTA_TEXT.render(f"Buy Santa", True, "white")
        BUT_SANTA_TEXT_RECT = BUT_SANTA_TEXT.get_rect()
        BUT_SANTA_TEXT_RECT.center = (400, 350)
        SCREEN.blit(BUT_SANTA_TEXT, BUT_SANTA_TEXT_RECT)

        REINDEER_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        REINDEER_TEXT = REINDEER_TEXT.render(f"Reindeer: {str(game.get_reindeers())}", True, "white")
        REINDEER_TEXT_RECT = REINDEER_TEXT.get_rect()
        REINDEER_TEXT_RECT.center = (400, 400)
        SCREEN.blit(REINDEER_TEXT, REINDEER_TEXT_RECT)
        BUY_REINDEER_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUY_REINDEER_TEXT = BUY_REINDEER_TEXT.render(f"Buy Reindeer", True, "white")
        BUY_REINDEER_TEXT_RECT = BUY_REINDEER_TEXT.get_rect()
        BUY_REINDEER_TEXT_RECT.center = (400, 450)
        SCREEN.blit(BUY_REINDEER_TEXT, BUY_REINDEER_TEXT_RECT)

        SLEIGH_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        SLEIGH_TEXT = SLEIGH_TEXT.render(f"Sleigh: {str(game.get_sleighs())}", True, "white")
        SLEIGH_TEXT_RECT = SLEIGH_TEXT.get_rect()
        SLEIGH_TEXT_RECT.center = (400, 500)
        SCREEN.blit(SLEIGH_TEXT, SLEIGH_TEXT_RECT)
        BUY_SLEIGH_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUY_SLEIGH_TEXT = BUY_SLEIGH_TEXT.render(f"Buy Sleigh", True, "white")
        BUY_SLEIGH_TEXT_RECT = BUY_SLEIGH_TEXT.get_rect()
        BUY_SLEIGH_TEXT_RECT.center = (400, 550)
        SCREEN.blit(BUY_SLEIGH_TEXT, BUY_SLEIGH_TEXT_RECT)

        WORKSHOP_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        WORKSHOP_TEXT = WORKSHOP_TEXT.render(f"Workshop: {str(game.get_workshops())}", True, "white")
        WORKSHOP_TEXT_RECT = WORKSHOP_TEXT.get_rect()
        WORKSHOP_TEXT_RECT.center = (800, 200)
        SCREEN.blit(WORKSHOP_TEXT, WORKSHOP_TEXT_RECT)
        BUY_WORKSHOP_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUY_WORKSHOP_TEXT = BUY_WORKSHOP_TEXT.render(f"Buy Workshop", True, "white")
        BUY_WORKSHOP_TEXT_RECT = BUY_WORKSHOP_TEXT.get_rect()
        BUY_WORKSHOP_TEXT_RECT.center = (800, 250)
        SCREEN.blit(BUY_WORKSHOP_TEXT, BUY_WORKSHOP_TEXT_RECT)

        FACTORY_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        FACTORY_TEXT = FACTORY_TEXT.render(f"Factory: {str(game.get_factories())}", True, "white")
        FACTORY_TEXT_RECT = FACTORY_TEXT.get_rect()
        FACTORY_TEXT_RECT.center = (800, 300)
        SCREEN.blit(FACTORY_TEXT, FACTORY_TEXT_RECT)
        BUY_FACTORY_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUY_FACTORY_TEXT = BUY_FACTORY_TEXT.render(f"Buy Factory", True, "white")
        BUY_FACTORY_TEXT_RECT = BUY_FACTORY_TEXT.get_rect()
        BUY_FACTORY_TEXT_RECT.center = (800, 350)
        SCREEN.blit(BUY_FACTORY_TEXT, BUY_FACTORY_TEXT_RECT)

        PRESENTS_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        PRESENTS_TEXT = PRESENTS_TEXT.render(f"Presents: {str(game.get_presents())}", True, "white")
        PRESENTS_TEXT_RECT = PRESENTS_TEXT.get_rect()
        PRESENTS_TEXT_RECT.center = (800, 500)
        SCREEN.blit(PRESENTS_TEXT, PRESENTS_TEXT_RECT)

        SAVE_CHRISTMAS_TEXT = pygame.font.Font("freesansbold.ttf", 40)
        SAVE_CHRISTMAS_TEXT = SAVE_CHRISTMAS_TEXT.render(f"Save Christmas!", True, "white")
        SAVE_CHRISTMAS_TEXT_RECT = SAVE_CHRISTMAS_TEXT.get_rect()
        SAVE_CHRISTMAS_TEXT_RECT.center = (800, 400)
        SCREEN.blit(SAVE_CHRISTMAS_TEXT, SAVE_CHRISTMAS_TEXT_RECT)
        BUY_SAVE_CHRISTMAS_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        BUY_SAVE_CHRISTMAS_TEXT = BUY_SAVE_CHRISTMAS_TEXT.render(f"Buy Save Christmas!", True, "white")
        BUY_SAVE_CHRISTMAS_TEXT_RECT = BUY_SAVE_CHRISTMAS_TEXT.get_rect()
        BUY_SAVE_CHRISTMAS_TEXT_RECT.center = (800, 450)
        SCREEN.blit(BUY_SAVE_CHRISTMAS_TEXT, BUY_SAVE_CHRISTMAS_TEXT_RECT)


        NOT_ENOUGH_TEXT = pygame.font.Font("freesansbold.ttf", 20)
        NOT_ENOUGH_TEXT = NOT_ENOUGH_TEXT.render(f"Not enough presents!", True, "white")

        NOT_ENOUGH_TEXT_RECT = NOT_ENOUGH_TEXT.get_rect()
        NOT_ENOUGH_TEXT_RECT.center = (600, 600)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BUY_ELF_TEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    x = game.get_presents()
                    if x >= 10:
                        game.buy_elf()
                    else:
                        SCREEN.blit(NOT_ENOUGH_TEXT, (500,850))
                        
                if BUT_SANTA_TEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    x = game.get_presents()
                    if x >= 100:
                        game.buy_santa()
                    else:
                        SCREEN.blit(NOT_ENOUGH_TEXT, (500,850))
                if BUY_REINDEER_TEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    x = game.get_presents()
                    if x >= 1000:
                        game.buy_reindeer()
                    else:
                        SCREEN.blit(NOT_ENOUGH_TEXT, (500,850))
                if BUY_SLEIGH_TEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    x = game.get_presents()
                    if x >= 10000:
                        game.buy_sleigh()
                    else:
                        SCREEN.blit(NOT_ENOUGH_TEXT, (500,850))
                if BUY_WORKSHOP_TEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    x = game.get_presents()
                    if x >= 100000:
                        game.buy_workshop()
                    else:
                        SCREEN.blit(NOT_ENOUGH_TEXT, (500,850))
                if BUY_FACTORY_TEXT_RECT.collidepoint(pygame.mouse.get_pos()):
                    x = game.get_presents()
                    if x >= 1000000:
                        game.buy_factory()
                    else:
                        SCREEN.blit(NOT_ENOUGH_TEXT, (500,850))
        pygame.display.update()


main_menu()
