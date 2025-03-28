import pygame

scores={"Easy": [], "Medium": [], "Hard": []}

def renderHighScores(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix High Scores", True, (255, 255, 255))
    screen.blit(title, (400 - title.get_width() // 2, 50))
    hint1 = font2.render("Hint: Use \'ESC\' or \'SPACE\' or \'ENTER\' to return", True, (255,255,255))
    screen.blit(hint1, (400 - hint1.get_width() // 2, 540))

    difficulties = ["Easy", "Medium", "Hard"]
    for i in range (len(difficulties)):
        difficulty = difficulties[i]
        
        difficultyLevelText = font1.render(difficulty + " Difficulty", True, (255, 255, 255))
        FirstScore = font2.render("1st Place: " + str(scores[difficulty][0]), True, (255,255,255))
        secondScore = font2.render("2nd Place: " + str(scores[difficulty][1]), True, (255,255,255))
        thirdScore = font2.render("3rd Place: " + str(scores[difficulty][2]), True, (255,255,255))
        
        screen.blit(difficultyLevelText, (150 + 250 * i - title.get_width() // 2, 150))
        screen.blit(FirstScore, (150 + 250 * i - FirstScore.get_width() // 2, 240))
        screen.blit(secondScore, (150 + 250 * i - secondScore.get_width() // 2, 340))
        screen.blit(thirdScore, (150 + 250 * i - thirdScore.get_width() // 2, 440))

    
def inputHighScores(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
            return True
        
def updateScores():
    global scores
    for difficulty in ["Easy", "Medium", "Hard"]:
        file = open("scores" + difficulty + ".txt", "r")
        scoreList = []
        for line in file:
            scoreList.append(int(line.strip()))
        scoreList.sort()
        scoreList.reverse()
        file.close()
        scores[difficulty] = scoreList
        