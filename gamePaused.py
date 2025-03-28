import pygame

def renderPaused(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Game Paused", True, (255, 255, 255))
    hint1 = font2.render("Press spacebar to return", True, (255,255,255))
    hint2 = font2.render("Press enter to view help menu", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    screen.blit(hint1, (400 - hint1.get_width() // 2, 240))
    screen.blit(hint2, (400 - hint2.get_width() // 2, 260))
    
def inputPaused(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            return "gameRunning"
        if event.key == pygame.K_RETURN:
            return "help"