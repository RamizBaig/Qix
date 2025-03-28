import pygame
from board import Board
from player import Player
from sparc import Sparc
from qix import Qix


def renderGame(screen):
    screen.fill((30,30,30))
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 22)
    title = font1.render("Qix", True, (255, 255, 255))
    livesText = font2.render("Lives: " + (str)(lives+1), True, (255, 255, 255))
    scorestext = font2.render("Score: " + (str)(score), True, (255, 255, 255))
    levelText = font2.render("Level: " + (str)(level+1), True, (255, 255, 255))
    hint = font2.render("Press \'p\' or \'esc\' to pause or for help", True, (255,255,255))
    screen.blit(title, (400 - title.get_width() // 2, 30))
    screen.blit(hint, (400 - hint.get_width() // 2, 570))
    screen.blit(livesText, (725, 35))
    screen.blit(scorestext, (25, 35))
    screen.blit(levelText, (25, 55))
    board.renderBoard(screen)
    player.renderPlayer(screen)
    for sparc in sparxList:
        sparc.renderSparc(screen)
    qix.renderQix(screen)
    summonSparxIntervals()
    gameLogic()
    if pygame.time.get_ticks() - timeAtFreeze < frozenLength:
        timerUntilUnfreeze = (frozenLength)//1000 - (pygame.time.get_ticks() - timeAtFreeze)// 1000
        font3 = pygame.font.Font(None, 100)
        unfreezeText = font3.render((str)(timerUntilUnfreeze), True, (255, 255, 255))
        screen.blit(unfreezeText, (400 - unfreezeText.get_width() // 2, 300 - unfreezeText.get_height()))
        if showBonus:
            bonusText = "Bonus: " + str(bonusPercentage) + "% * 1000 points = " + str(bonusPercentage*1000)
            bonusRender = font1.render(bonusText, True, (255, 255, 255))
            screen.blit(bonusRender, (400 - bonusRender.get_width() // 2, 375 - bonusRender.get_height()))
    
def gameLogic():
    global lives, level
    if pygame.time.get_ticks() - timeAtFreeze < frozenLength: return
    controlMovementIntervals()
    board.playerPos = player.pos
    if playerHit(): 
        lives -= 1
        resetBoard()
    updatePoints()
    if board.currentPercentage() > requiredPercent/100:
        level+=1
        newLevel()
        
    
def inputGame(event): 
    global timeWhenPaused, lastSparxSummon
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
            timeWhenPaused = pygame.time.get_ticks()
            if pygame.time.get_ticks() - timeAtFreeze < frozenLength:
                timeUntilUnfreeze = (frozenLength) - (pygame.time.get_ticks() - timeAtFreeze)
                if timeUntilUnfreeze > 0:
                    lastSparxSummon -= timeUntilUnfreeze
            return True
    player.inputPlayer(event)

def isGameOver():
        return lives < 0

def summonSparxIntervals():
    currentTime = pygame.time.get_ticks()
    global lastSparxMoveTime, lastSparxSummon
    if currentSparxLeft > 0:
        if currentTime - lastSparxSummon >= SparxSummonConstant/currentSparxLeft:
            summonSparcPair()
            lastSparxSummon = currentTime

def controlMovementIntervals():
    global lastPlayerMoveTime, lastSparxMoveTime, lastSparxSummon
    currentTime = pygame.time.get_ticks()
    if player.push and board.incursion:
        if currentTime - lastPlayerMoveTime >= playerMoveInterval*2:
            if player.movePlayer(): 
                lastPlayerMoveTime = currentTime
                player.slowIncursionMoves += 1
    else: 
        if currentTime - lastPlayerMoveTime >= playerMoveInterval:
            if player.movePlayer(): 
                lastPlayerMoveTime = currentTime
                player.fastIncursionMoves += 1
                
    if currentTime - lastSparxMoveTime >= sparxMoveInterval:
        moveAllSparx()
        lastSparxMoveTime = currentTime
  
    if currentTime - lastQixMoveTime >= qixMoveInterval:
        qix.updatePosition()
    
def moveAllSparx():
    for sparc in sparxList:
        sparc.moveSparc()

def summonSparcPair():
    global currentSparxLeft
    currentSparxLeft -= 2
    sparc1 = Sparc(board, player.pos, ( 3, 0))
    sparc2 = Sparc(board, player.pos, (-3, 0))
    sparxList.append(sparc1)
    sparxList.append(sparc2)
    
def playerHit():
    for sparc in sparxList:
        if sparc.playerHit():
            return True
    if qix.playerHit():
        return True

def resetBoard():
    global sparxList, currentSparxLeft, lastSparxSummon, frozenLength, timeAtFreeze, showBonus
    player.pos = player.lastBorderPos
    sparxList = []    
    numSparx = [4,6,8,10,12]
    currentSparxLeft = numSparx[min(level, len(numSparx)-1)]
    lastSparxSummon = -999999
    board.newIncursionMask()
    board.incursion = False
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))  
    triggerFreeze(2000)
    showBonus = False

def newLevel():
    global board, player, qix, lastPercentageUpdate, timeAtFreeze, frozenLength, showBonus
    resetBoard()
    showBonus = True
    board = Board()
    player = Player(board)
    qix = Qix(board)
    lastPercentageUpdate = 0
    timeAtFreeze = pygame.time.get_ticks()
    frozenLength = 3000
    triggerFreeze(3000)
    

def resetGame(boardRequiredPercent):
    global lives, score, requiredPercent, level, lastPercentageUpdate
    global board, player, qix, lastPlayerMoveTime,playerMoveInterval, lastSparxSummon,sparxMoveInterval
    global lastSparxMoveTime, SparxSummonConstant, currentSparxLeft, sparxList, qixMoveInterval, lastQixMoveTime
    global showBonus, timeWhenPaused
    lives = 2
    level = 0
    score = 0
    timeWhenPaused = pygame.time.get_ticks()
    showBonus = False
    requiredPercent = boardRequiredPercent
    lastPercentageUpdate = 0
    board = Board()
    player = Player(board)
    qix = Qix(board)
    lastPlayerMoveTime, playerMoveInterval = 0, 20
    lastSparxMoveTime , sparxMoveInterval  = 0, 20
    lastSparxSummon , SparxSummonConstant  = -999999, 5000*2
    lastQixMoveTime , qixMoveInterval = 0, 10
    numSparx = [4,6,8,10,12]
    currentSparxLeft = numSparx[min(level, len(numSparx)-1)]
    sparxList = []
    triggerFreeze(3000)
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1))   
    
def getScore():
    return score

def getDifficulty():
    return {65: "Easy", 75: "Medium", 85: "Hard"}[requiredPercent]

def updatePoints():
    global lastPercentageUpdate, score, bonusPercentage
    newPercent = int(board.currentPercentage()*100) - int(lastPercentageUpdate)
    if not newPercent: return
    lastPercentageUpdate = int(board.currentPercentage()*100)
    bonus = 1.5 if (player.slowIncursionMoves / player.fastIncursionMoves) >= 1.5 else 1
    score += (int)((2*newPercent*100 + 5*newPercent**0.5) * bonus)
    bonusPercentage = lastPercentageUpdate - requiredPercent
    if lastPercentageUpdate > requiredPercent:
        score += bonusPercentage * 1000
        
def triggerFreeze(length):
    global frozenLength, timeAtFreeze, lastSparxSummon
    frozenLength = length
    pauseDuration = pygame.time.get_ticks() - timeWhenPaused
    lastSparxSummon = lastSparxSummon + pauseDuration + length
    timeAtFreeze = pygame.time.get_ticks()