import pygame

def renderHelp(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix Help", True, (255, 255, 255))
    hint1 = font2.render(" 1. You may use WASD/Arrow Keys to move", True, (255,255,255))
    hint2 = font2.render("2a. You must hold Spacebar to start an incursion", True, (255,255,255))
    hint3 = font2.render("2b. Holding Spacebar allows you to do a slow incursion", True, (255,255,255))
    hint4 = font2.render("2c. Slow Incursions give more points", True, (255,255,255))
    hint5 = font2.render(" 3. You get 3 lives to claim as much of the board to progress to harder levels", True, (255,255,255))
    hint6 = font2.render(" 4. Avoid the sparcs on the walls when on a boundary", True, (255,255,255))
    hint7 = font2.render(" 5. Avoid the qix while claiming land in the board", True, (255,255,255))
    
    screen.blit(title, (400 - title.get_width()//2, 50))
    screen.blit(hint1, (100, 150))
    screen.blit(hint2, (100, 200))
    screen.blit(hint3, (100, 250))
    screen.blit(hint4, (100, 300))
    screen.blit(hint5, (100, 350))
    screen.blit(hint6, (100, 400))
    screen.blit(hint7, (100, 450))
    
    tip = font2.render("Hint: Use \'ESC\' or \'SPACE\' or \'ENTER\' to return", True, (255,255,255))
    screen.blit(tip, (400 - tip.get_width() // 2, 540))
    
def inputHelp(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
            return True