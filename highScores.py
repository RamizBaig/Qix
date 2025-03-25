import pygame

scores=[]

def renderHighScores(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix High Scores", True, (255, 255, 255))
    FirstScore = font2.render("1st Place: " + scores[0], True, (255,255,255))
    secondScore = font2.render("2nd Place: " + scores[1], True, (255,255,255))
    thirdScore = font2.render("3rd Place: " + scores[2], True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    screen.blit(FirstScore, (400 - FirstScore.get_width() // 2, 240))
    screen.blit(secondScore, (400 - secondScore.get_width() // 2, 340))
    screen.blit(thirdScore, (400 - thirdScore.get_width() // 2, 440))

    
def inputHighScores(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
            return True
        
def updateScores():
    global scores
    file = open("scores.txt", "r")
    for line in file:
        scores.append(line.strip())
    scores.sort()
    scores.reverse()
    file.close()