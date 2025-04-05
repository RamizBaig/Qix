import pygame

WIDTH, HEIGHT = 619, 490
class Board:
    def __init__(self, newLevel):
        self.level = newLevel
        self.mask = pygame.Mask((WIDTH, HEIGHT))
        self.regionBorders = pygame.Mask((WIDTH, HEIGHT))
        self.newIncursionMask()
        
        self.mask.fill()  
        self.regionBorders.fill()
        for x in range(WIDTH):
            self.mask.set_at((x, 0), 0)        
            self.mask.set_at((x, HEIGHT - 1), 0) 
            self.regionBorders.set_at((x, 0), 0)        
            self.regionBorders.set_at((x, HEIGHT - 1), 0) 

        for y in range(HEIGHT):
            self.mask.set_at((0, y), 0)     
            self.mask.set_at((WIDTH - 1, y), 0)
            self.regionBorders.set_at((0, y), 0)     
            self.regionBorders.set_at((WIDTH - 1, y), 0)

        self.qixPos = (400, 300)
        self.playerPos = None
        
            
    def getQixPos(self):
        return self.qixPos

    def renderBoard(self, screen):
        mask_surface = self.mask.to_surface(setcolor=(50,50,50), unsetcolor=(0, 255, 0))
        region_surface = self.regionBorders.to_surface(setcolor=(0,0,0,0), unsetcolor=(0,0,255))
        
        screen.blit(mask_surface, (90, 60))
        
        offsets = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in offsets:
            screen.blit(region_surface, (90 + dx, 60 + dy))
        
        if self.incursion:
            path_surface = self.dynamicMask.to_surface(setcolor=(0,0,0,0), unsetcolor=(255,0,0))
            for dx, dy in offsets:
                screen.blit(path_surface, (90 + dx, 60 + dy))
    

    def getMask(self):
        return self.mask
    
    def newIncursionMask(self):
        self.dynamicMask = pygame.Mask((619, 490)) 
        self.dynamicMask.fill()
        
    def findMaskPixel(self, pos, mask):
        x, y = pos
        mask_x = x - 90
        mask_y = y - 60
        if 0 <= mask_x < mask.get_size()[0] and 0 <= mask_y < mask.get_size()[1]:
            return mask.get_at((mask_x, mask_y))
        return None
    
    def ensureOnBorder(self, pos):
        vecs = ((0, 3), (3, 0), (-3, 0), (0, -3),
                (3, 3), (-3, 3), (3, -3), (-3, -3))
        for dx, dy in vecs:
            maskPos = (pos[0] + dx, pos[1] + dy)
            pixel = self.findMaskPixel(maskPos, self.mask)
            if pixel == 1:
                return True
        return False

    def currentPercentage(self):
        num_zeros = self.mask.get_size()[0] * self.mask.get_size()[1] - self.mask.count()
        return num_zeros / (self.mask.get_size()[0] * self.mask.get_size()[1])