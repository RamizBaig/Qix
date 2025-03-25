import pygame
pygame.init()

from mainMenu import *
from help import *
from highScores import *
from results import *
from gamePaused import *
from gameRunning import *

gameStates = {"mainMenu": True, "help": False, "highScores": False, "gameRunning": False, "gamePaused": False, "results": False}

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qix Game")

running = True
i = 0
while running:
    i+=1
    if (i%10000 ==0): print(i)
    pygame.display.update()
    if gameStates["mainMenu"]:
        renderMenu(screen)
    elif gameStates["help"]:
        renderHelp(screen)
    elif gameStates["highScores"]:
        renderHighScores(screen)
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
        elif gameStates["help"]:
            if inputHelp(event): 
                gameStates["help"], gameStates["mainMenu"] = False, True
        elif gameStates["highScores"]:
            if inputHighScores(event):
                gameStates["highScores"], gameStates["mainMenu"] = False, True
        elif gameStates["gameRunning"]:
            if inputGame(event):
                gameStates["gameRunning"], gameStates["gamePaused"] = False, True
        elif gameStates["gamePaused"]:
            if inputPaused(event):
                gameStates["gamePaused"], gameStates["gameRunning"] = False, True
        elif gameStates["results"]:
            if resultsInput(event):
                gameStates["results"], gameStates["mainMenu"] = False, True
                resetMenuValues()
            
pygame.quit()