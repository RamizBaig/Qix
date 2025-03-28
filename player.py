import pygame
#from Board import getBoard
movement_vectors = {
        pygame.K_LEFT:  (-3,  0),  pygame.K_a:  (-3,  0),
        pygame.K_RIGHT: ( 3,  0),  pygame.K_d:  ( 3,  0),
        pygame.K_UP:    ( 0, -3),  pygame.K_w:  ( 0, -3),
        pygame.K_DOWN:  ( 0,  3),  pygame.K_s:  ( 0,  3)
    }
class Player:
    
    def __init__(self, board):
        self.board = board
        self.pos = (399, 549)
        self.lastBorderPos = self.pos
        self.keyHolds = []  
        self.push = False
        self.board.incursion = False
        self.lives = 3
        self.slowIncursionMoves = 0
        self.fastIncursionMoves = 0

    def movePlayer(self):       
        if self.keyHolds == []: return
        if self.keyHolds[0] not in movement_vectors: return
        
        mask = self.board.getMask()   
        newPos = self.newPos(self.pos, movement_vectors[self.keyHolds[0]])
        wantedPosition = self.board.findMaskPixel(newPos, mask)
        if wantedPosition == None:
            return
        if self.board.incursion:   
            pathMaskPixel = self.board.findMaskPixel(newPos, self.board.dynamicMask)
            if pathMaskPixel == 0:
                return
            if wantedPosition == 1:
                self.addPathToMask(self.pos, movement_vectors[self.keyHolds[0]])
                self.pos = newPos
                return True       
            else: 
                self.board.incursionPoint=self.pos
                self.addPathToMask(self.pos, movement_vectors[self.keyHolds[0]])
                self.pos = newPos
                self.completeIncursion()
                self.lastBorderPos = self.pos 
                self.board.newIncursionMask()
                return True 
        
        elif self.push and wantedPosition == 1:
            if wantedPosition == 1:
                self.addPathToMask(self.pos, movement_vectors[self.keyHolds[0]])
                self.lastBorderPos = self.pos 
                self.pos = newPos
                self.board.incursion = True
                self.slowIncursionMoves = 0
                self.fastIncursionMoves = 0
                return True 
           
        else: # not self.push:
            if wantedPosition == 0 and self.board.ensureOnBorder(newPos):
                self.lastBorderPos = self.pos 
                self.pos = newPos
                return True
       
        return False

    def completeIncursion(self):
        self.board.incursion=False 
        mask = self.board.getMask()
        width, height = mask.get_size()
        tempMask = pygame.Mask((619, 490))
        for x in range(width):
            for y in range(height):
                if self.board.dynamicMask.get_at((x, y)) == 0:
                    mask.set_at((x, y), 0)
                    self.board.regionBorders.set_at((x, y), 0)
        
        vecs = ((0,1),(1,0),(-1,0),(0,-1))
        for vec in vecs:
            startingFloodPoint = self.newPos(self.board.incursionPoint, vec)
            
            if self.board.findMaskPixel(startingFloodPoint, mask) == None: 
                continue
            startingFloodPoint = (startingFloodPoint[0]-90, startingFloodPoint[1]-60)
            if mask.get_at(startingFloodPoint) == 0:
                continue
            tempMask = mask.connected_component(startingFloodPoint)
            qixPos = self.board.getQixPos()
            qixPosOnMask = self.newPos(qixPos, (-90, -60))
            if tempMask.get_at(qixPosOnMask):
                self.board.mask = tempMask
                return      

    def newPos(self, pos, vec):
        return (pos[0] + vec[0], pos[1] + vec[1])
    
    def addPathToMask(self, pos, vec):
        offset_x, offset_y = 90, 60
        x, y = pos 
        mask_x, mask_y = x - offset_x, y - offset_y
        for i in range(1, 4):  
            new_x = mask_x + vec[0]/3 * i
            new_y = mask_y + vec[1]/3 * i
            self.board.dynamicMask.set_at((new_x, new_y), 0)
    
    def inputPlayer(self, event):  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.push = True
            elif event.key not in self.keyHolds:
                self.keyHolds.append(event.key)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.push = False
            elif event.key in self.keyHolds:
                self.keyHolds.remove(event.key)
    
    def renderPlayer(self, screen):
        # Create a transparent surface
        ring_surface = pygame.Surface((20, 20), pygame.SRCALPHA)  
        ring_surface.fill((0, 0, 0, 0))  # Fully transparent background

        # Draw the outer circle (red)
        pygame.draw.circle(ring_surface, (255, 0, 0, 255), (10, 10), 8, width=3)

        # Blit onto the main screen
        screen.blit(ring_surface, (self.pos[0] - 10, self.pos[1] - 10))
