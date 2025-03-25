import pygame
pygame.init()
options = {"Start": True, "Highscores": False, "Help": False}
highlightedButton = 0

def renderMenu(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix", True, (255, 255, 255))
    hint1 = font2.render("Hint: use the arrow keys and spacebar to navigate", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    screen.blit(hint1, (400 - hint1.get_width() // 2, 540))
    
    pygame.draw.rect(screen, (200,200, 30), pygame.Rect(290, 140+highlightedButton*100, 220, 100))

    i = 0
    for option in options:        
        color = (50, 120, 200)
        pygame.draw.rect(screen, color, pygame.Rect(300, 150+100*i, 200, 80))
        name = font2.render(option, True, (0,0,0))
        screen.blit(name, (400 - name.get_width()//2, 190+100*i-name.get_height()//2))
        i+=1

def inputMenu(event):
    global highlightedButton
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_SPACE | pygame.K_RETURN:
                stages = ["gameRunning", "highScores", "help"]
                return stages[highlightedButton]
            case pygame.K_DOWN | pygame.K_s:
                highlightedButton = min(highlightedButton+1, 2)
            case pygame.K_UP | pygame.K_w:
                highlightedButton = max(highlightedButton-1, 0)
    
def resetMenuValues():
    global highlightedButton
    highlightedButton = 0