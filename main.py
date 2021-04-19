import pygame
from game import Game
import math

pygame.init()


# fenetre

pygame.display.set_caption("PyG_KAN")
screen = pygame.display.set_mode((720, 680))

myfont = pygame.font.SysFont("monospace",36)
myfont2 = pygame.font.SysFont("elephant",36)

# Qst
bgQST = pygame.image.load('bgQST.png')
bgQST = pygame.transform.scale(bgQST, (500, 500))

bg = pygame.image.load('assets/bg4.png')
screen_size = screen.get_size()
bg_size = bg.get_size() 
bg_x = 0
bg_y =-bg_size[1] + 680


# astronault
astronault = pygame.image.load('assets/astroF.png')
astronault = pygame.transform.scale(astronault, (200, 400))
astronault_rect = astronault.get_rect()
astronault_rect.x = 55
astronault_rect.y = 45


# Button
playBtn = pygame.image.load('assets/play.png')
playBtn = pygame.transform.scale(playBtn, (400, 150))
playBtn_rect = playBtn.get_rect()
playBtn_rect.x = 160
playBtn_rect.y = 300
# charger notre jeu
game = Game()

test = True

running = True
while running :
    
    if  game.pause:
        test = False

    # apliquer l'arrier plan de notre jeu
    screen.blit(bg, (bg_x, bg_y))
    if game.is_playing:
        if bg_y < bg_size[1] :
            if  bg_y < -1850:
                bg_y +=40
            else:
                bg_y +=10
        if bg_y >= 0:
            bg_y = -1850
        screen.blit(bg, (bg_x, bg_y))
        text = myfont.render("Score {0}".format(game.player.score), 1, (255,255,255))
        screen.blit(text, (5,10))
        game.update(screen)
    else:
        if game.is_pause:
            x=game.question()
           
            for i in  range(3):
                text = myfont2.render("{}".format(x[i]), 1, (255,255,255))
                screen.blit(text, (200,350+60*i))  

            img = pygame.image.load(x[3])
            img = pygame.transform.scale(img, (100, 100))
            screen.blit(img, (310,200))

            game.pause = True
  

        else:    
            screen.blit(playBtn, playBtn_rect)
            screen.blit(astronault, astronault_rect)

    
    if test :
        pygame.display.flip()


    # events
    for event in pygame.event.get():
        #fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # pressed
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if playBtn_rect.collidepoint(event.pos):
                test = True
                game.start()
                