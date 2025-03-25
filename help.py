import pygame

def renderHelp(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix Help", True, (255, 255, 255))
    hint1 = font2.render("some instrcutions 1", True, (255,255,255))
    hint2 = font2.render("some instructions 2", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    screen.blit(hint1, (400 - hint1.get_width() // 2, 240))
    screen.blit(hint2, (400 - hint2.get_width() // 2, 340))
    
def inputHelp(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            return True