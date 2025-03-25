import pygame
from board import Board
from player import Player

board = Board()
player = Player(board)
lastPlayerMoveTime, playerMoveInterval = 0, 5

def renderGame(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix", True, (255, 255, 255))
    hint2 = font2.render("Created by: us", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 30))
    screen.blit(hint2, (400 - hint2.get_width() // 2, 570))
    
    board.renderBoard(screen)
    player.renderPlayer(screen)
    controlMovementIntervals()
    
def inputGame(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            return True
    player.inputPlayer(event)

def controlMovementIntervals():
    global lastPlayerMoveTime
    currentTime = pygame.time.get_ticks()
    if currentTime - lastPlayerMoveTime >= playerMoveInterval:
        if player.movePlayer(): 
            lastPlayerMoveTime = currentTime