import pygame

class Sparc:
    def __init__(self, board, playerPos, direction):
        self.board = board
        self.pos = self.findSpawnLocation(playerPos)
        self.directionVec = direction
        self.trapped = False
        
    def renderSparc(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.pos), 7) 
    
    def moveSparc(self):
        wantedPos = self.newPos(self.pos, self.directionVec)
        if self.board.findMaskPixel(wantedPos, self.board.regionBorders) == 0 and self.board.ensureOnBorder(wantedPos):
            self.pos = wantedPos

        else: 
            self.directionVec = self.chooseNewDir()
            self.pos = self.newPos(self.pos, self.directionVec)

    def playerHit(self):
        return abs(self.pos[0] - self.board.playerPos[0]) + abs(self.pos[1] - self.board.playerPos[1]) <= 5

    def chooseNewDir(self):
        directions = [(0,-3), (3,0), (0,3),(-3,0)]
        directions.remove(self.directionVec)
        directions.remove((self.directionVec[0]*-1, self.directionVec[1]*-1))
        for vec in directions:
            wantedPos = self.newPos(self.pos, vec)
            if self.board.findMaskPixel(wantedPos, self.board.regionBorders) == 0 and self.board.ensureOnBorder(wantedPos):
                self.trapped = False
                return vec
        
        # only reaches here if cant find a good direction
        self.trapped = True
        playerPos = self.board.playerPos
        directions = [(0,-3), (3,0), (0,3),(-3,0)]
        dist = []
        for vec in directions:
            wantedPos = self.newPos(self.pos, vec)
            if (vec != (self.directionVec[0]*-1, self.directionVec[1]*-1)) and self.board.findMaskPixel(wantedPos, self.board.regionBorders) == 0:
                dist.append((playerPos[0] - (self.pos[0] + vec[0]))**2 + (playerPos[1] - (self.pos[1] + vec[1]))**2)
            else: 
                dist.append(999999999)

        return directions[dist.index(min(dist))]
    
    def newPos(self, pos, vec):
        return (pos[0] + vec[0], pos[1] + vec[1])
    
    def findSpawnLocation(self, playerPos):
        x = 618 - playerPos[0] + 90 + 90
        if playerPos[1] < 275:
            y = 549
        else: 
            y = 60
        return (x, y)
        
    
        