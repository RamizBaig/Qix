import pygame
pygame.init()

def resultsInput(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            return True
        
def renderResults(screen, passes):
    screen.fill((30,30,30))
    #font = pygame.font.Font(None, 50)

 