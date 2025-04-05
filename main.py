import pygame
pygame.init()

from mainMenu import *
from help import *
from highScores import *
from results import *
from gamePaused import *
from gameRunning import *
from levelSelection import *

gameStates = {"mainMenu": True, "help": False, "highScores": False, "levelSelection": False, "gameRunning": False, "gamePaused": False, "results": False}

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qix Game")
activeGame = False
running = True
while running:
    pygame.display.update()
    if gameStates["mainMenu"]:
        renderMenu(screen)
    elif gameStates["help"]:
        renderHelp(screen)
    elif gameStates["highScores"]:
        renderHighScores(screen)
    elif gameStates["levelSelection"]:
        renderSelection(screen)
    elif gameStates["gameRunning"]:
        renderGame(screen)
    elif gameStates["gamePaused"]:
        renderPaused(screen)
    elif gameStates["results"]:
        renderResults(screen)
        
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running=False 
        if gameStates["mainMenu"]:
            stage = inputMenu(event)
            if stage: gameStates["mainMenu"], gameStates[stage] = False, True
            if stage == "highScores": updateScores()
        elif gameStates["levelSelection"]:
            boardPercentRequired = selectionInput(event)
            if boardPercentRequired:
                if boardPercentRequired == "return":
                    gameStates["levelSelection"], gameStates["mainMenu"] = False, True
                else:    
                    gameStates["levelSelection"], gameStates["gameRunning"] = False, True
                    resetGame(boardPercentRequired)
        elif gameStates["help"]:
            if inputHelp(event): 
                if activeGame:
                    gameStates["help"], gameStates["gameRunning"] = False, True
                    triggerFreeze(3000)
                else: 
                    gameStates["help"], gameStates["mainMenu"] = False, True
        elif gameStates["highScores"]:
            if inputHighScores(event):
                gameStates["highScores"], gameStates["mainMenu"] = False, True
        elif gameStates["gameRunning"]:
            if inputGame(event): 
                gameStates["gameRunning"], gameStates["gamePaused"] = False, True
            if isGameOver(): 
                setScoreAndDifficulty(getScore(), getDifficulty())
                appendScore()
                gameStates["gameRunning"], gameStates["results"] = False, True
        elif gameStates["gamePaused"]:
            state = inputPaused(event)
            if state:
                if state == "gameRunning": triggerFreeze(3000)
                gameStates["gamePaused"], gameStates[state] = False, True
                activeGame = True
        elif gameStates["results"]:
            if resultsInput(event):
                gameStates["results"], gameStates["mainMenu"] = False, True
                resetMenuValues()
                activeGame = False
            
pygame.quit()