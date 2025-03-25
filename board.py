import pygame

WIDTH, HEIGHT = 619, 490
class Board:
    updated = False

    def __init__(self):
        self.updated = False
        mask = pygame.Mask((WIDTH, HEIGHT))
        regionBorders = pygame.Mask((WIDTH, HEIGHT))
        mask.fill()  
        regionBorders.fill()
        for x in range(WIDTH):
            mask.set_at((x, 0), 0)        
            mask.set_at((x, HEIGHT - 1), 0) 
            regionBorders.set_at((x, 0), 0)        
            regionBorders.set_at((x, HEIGHT - 1), 0) 

        for y in range(HEIGHT):
            mask.set_at((0, y), 0)     
            mask.set_at((WIDTH - 1, y), 0)
            regionBorders.set_at((0, y), 0)     
            regionBorders.set_at((WIDTH - 1, y), 0)
        self.mask = mask
        self.regionBorders = regionBorders
        self.qixPos = (400, 300)
            
    def getQixPos(self):
        return self.qixPos

    def renderBoard(self, screen):
        mask_surface = self.mask.to_surface(setcolor=(50,50,50), unsetcolor=(0, 255, 0))
        region_surface = self.regionBorders.to_surface(setcolor=(0,0,0,0), unsetcolor=(0,0,255))
        screen.blit(mask_surface, (80, 60))
        screen.blit(region_surface, (80, 60))

    def getMask(self):
        return self.mask

