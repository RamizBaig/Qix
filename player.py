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
        self.pos = (80, 60)
        self.keyHolds = []  
        self.push = False
        self.incursion = False

    def movePlayer(self):        
        if self.keyHolds == []: return
        if self.keyHolds[0] not in movement_vectors: return
        
        mask = self.board.getMask()   
        newPos = self.newPos(self.pos, movement_vectors[self.keyHolds[0]])
        wantedPosition = self.findMaskPixel(newPos, mask)
        if wantedPosition == None:
            return
        if not self.incursion and not self.push:
            if wantedPosition == 0 and self.ensureOnBorder(newPos):
                self.pos = newPos
                return True
        elif not self.incursion and self.push:
            if wantedPosition == 1:
                self.newIncursionMask()
                self.addPathToMask(self.pos, movement_vectors[self.keyHolds[0]])
                self.pos = newPos
                return True 
        else:   
            pathMaskPixel = self.findMaskPixel(newPos, self.dynamic_mask)
            if pathMaskPixel == 0:
                return
            if wantedPosition == 1:
                self.addPathToMask(self.pos, movement_vectors[self.keyHolds[0]])
                self.pos = newPos
                return True       
            else: 
                self.incursionPoint=self.pos
                self.addPathToMask(self.pos, movement_vectors[self.keyHolds[0]])
                self.pos = newPos
                self.completeIncursion()
                self.incursion=False 
                return True 
        return False

    def ensureOnBorder(self, pos):
        vecs = ((0, 3), (3, 0), (-3, 0), (0, -3),
                (3, 3), (-3, 3), (3, -3), (-3, -3))
        for dx, dy in vecs:
            maskPos = (pos[0] + dx, pos[1] + dy)
            pixel = self.findMaskPixel(maskPos, self.board.mask)
            if pixel == 1:
                return True
        print(pos)
        return False

    def completeIncursion(self):
        self.incursion=False 
        mask = self.board.getMask()
        width, height = mask.get_size()
        tempMask = pygame.Mask((619, 490))
        for x in range(width):
            for y in range(height):
                if self.dynamic_mask.get_at((x, y)) == 0:
                    mask.set_at((x, y), 0)
        
        vecs = ((0,1),(1,0),(-1,0),(0,-1))
        for vec in vecs:
            startingFloodPoint = self.newPos(self.incursionPoint, vec)
            
            if self.findMaskPixel(startingFloodPoint, mask) == None: 
                continue
            startingFloodPoint = (startingFloodPoint[0]-80, startingFloodPoint[1]-60)
            if mask.get_at(startingFloodPoint) == 0:
                continue
            
            tempMask = mask.connected_component(startingFloodPoint)
            if tempMask.get_at(self.board.getQixPos()):
                self.board.mask = tempMask
                print(startingFloodPoint)
                return  
        
    def checkNonQixSide(self):
        BFSlist = []
        visited = []
        vecs = ((0,1),(1,0),(-1,0),(0,-1))
        mask = self.board.getMask()
        for vec in vecs:
            startingFloodPoint = self.newPos(self.incursionPoint, vec)
            if self.findMaskPixel(startingFloodPoint, mask) == None: 
                continue
            startingFloodPoint = (startingFloodPoint[0]-80, startingFloodPoint[1]-60)
            if self.dynamic_mask.get_at(startingFloodPoint) == 0:
                continue
            BFSlist.append(startingFloodPoint)
            visited.append(startingFloodPoint)
            while BFSlist:
                x, y = BFSlist.pop()
                qixX, qixY = self.board.getQixPos()
                if x==qixX and y==qixY:
                    continue
                for dx, dy in vecs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < mask.get_size()[0] and 0 <= ny < mask.get_size()[1]:
                        if mask.get_at((nx, ny)) == 1 and self.dynamic_mask.get_at((nx, ny)) == 1:
                            if (nx,ny) not in visited:
                                BFSlist.append((nx, ny))
                                visited.append((nx, ny))
            print(startingFloodPoint)
    

    def newPos(self, pos, vec):
        return (pos[0] + vec[0], pos[1] + vec[1])
    
    def newIncursionMask(self):
        self.incursion=True
        self.dynamic_mask = pygame.Mask((619, 490)) #self.board.getMask().copy()
        self.dynamic_mask.fill()
    
    def addPathToMask(self, pos, vec):
        offset_x, offset_y = 80, 60
        x, y = pos 
        mask_x, mask_y = x - offset_x, y - offset_y
        for i in range(1, 4):  
            new_x = mask_x + vec[0]/3 * i
            new_y = mask_y + vec[1]/3 * i
            self.dynamic_mask.set_at((new_x, new_y), 0)
            self.board.regionBorders.set_at((new_x, new_y), 0)
    
    def findMaskPixel(self, pos, mask):
        x, y = pos
        mask_x = x - 80
        mask_y = y - 60
        if 0 <= mask_x < mask.get_size()[0] and 0 <= mask_y < mask.get_size()[1]:
            return mask.get_at((mask_x, mask_y))
        return None
        
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
        if self.incursion:
            mask_surface = self.dynamic_mask.to_surface(setcolor=(0,0,0,0), unsetcolor=(255, 0, 0))
            screen.blit(mask_surface, (80, 60))
        
        pygame.draw.circle(screen, (255, 0, 0), (self.pos), 10) 
