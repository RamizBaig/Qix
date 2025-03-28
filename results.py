import pygame
pygame.init()

def resultsInput(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            return True

def setScoreAndDifficulty(newScore, levelDifficulty):
    global score, difficulty
    score = newScore
    difficulty = levelDifficulty

def renderResults(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix", True, (255, 255, 255))
    hint2 = font1.render("Score: " + (str)(score), True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 30))
    screen.blit(hint2, (400 - hint2.get_width() // 2, 370))

def appendScore():
    file = open("scores" + difficulty + ".txt", 'a')
    file.write("\n"+(str)(score))
    file.close()
    