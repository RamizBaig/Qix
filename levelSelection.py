import pygame
pygame.init()

options = [["Easy", "Medium", "Hard"], ["", "Start", ""]]
selected = {"Easy": False, "Medium": True, "Hard": False}

pos = (1, 1)

def selectionInput(event):
    global pos
    global selected
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_DOWN | pygame.K_s:
                pos = (1, 1)
            case pygame.K_UP | pygame.K_w:
                pos = (pos[0], 0)
            case pygame.K_LEFT | pygame.K_a:
                pos = (max(0, pos[0]-1), 0)
            case pygame.K_RIGHT | pygame.K_d:
                pos = (min(2, pos[0]+1), 0)
                
            case pygame.K_SPACE | pygame.K_RETURN:
                if pos[1] == 0:
                    selected = {"Easy": False, "Medium": False, "Hard": False}
                    selected[options[0][pos[0]]] = True
                else:
                    if selected["Easy"]: return 65
                    elif selected["Medium"]: return 75
                    elif selected["Hard"]: return 85
            
            case pygame.K_ESCAPE:
                return "return"

                
def renderSelection(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Select Game Difficulty", True, (255, 255, 255))
    hint1 = font2.render("Hint: use the arrow keys and spacebar to navigate", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    screen.blit(hint1, (400 - hint1.get_width() // 2, 560))
    
    pygame.draw.rect(screen, (200,200, 30), pygame.Rect(40+250*pos[0], 140+200*pos[1], 220, 120))
    for j in range(len(options[0])):
        color = (50, 220, 100) if selected[options[0][j]] else (200, 40, 40)
        pygame.draw.rect(screen, color, pygame.Rect(50+250*j, 150, 200, 100))
        name = font2.render(options[0][j], True, (0,0,0))
        screen.blit(name, (150+250*j - name.get_width()//2, 200-name.get_height()//2))
    
    pygame.draw.rect(screen, (80,80,80), pygame.Rect(300, 350, 200, 100))
    name = font2.render(options[1][1], True, (0,0,0))
    screen.blit(name, (400 - name.get_width()//2, 400-name.get_height()//2))
    
    hint2 = font2.render("Hint: Use \'ESC\' to return", True, (255,255,255))
    screen.blit(hint2, (400 - hint2.get_width() // 2, 540))
                
    