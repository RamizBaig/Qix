import random
import pygame
import math

class Qix:
    def __init__(self, board):
        self.board = board
        self.center_pos = (355,275)
        self.target_pos = self.center_pos
        self.rotation_angle = random.uniform(0, 360)
        self.target_rotation = self.rotation_angle
        self.line_length = random.randint(30, 65) 
        self.target_line_length = self.line_length
        self.movement_steps = 60 
        self.current_step = 0
        self.trail_points = []


    def choose_new_target(self):
        targetRange = 220
        degreeRange = 180
        width, height = self.board.mask.get_size()
        while True:
            min_x = max(0, self.center_pos[0] - targetRange)
            max_x = min(width - 1, self.center_pos[0] + targetRange)
            min_y = max(0, self.center_pos[1] - targetRange)
            max_y = min(height - 1, self.center_pos[1] + targetRange)

            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)

            if self.board.findMaskPixel((x, y), self.board.mask) == 1:
                self.target_pos = (x, y)
                self.target_rotation = (self.target_rotation + random.randint(-degreeRange//2, degreeRange//2))%360
                self.target_line_length = random.randint(30, 65)
                self.current_step = 0  
                return (x, y)

    def updatePosition(self):
        if self.board.findMaskPixel(self.target_pos, self.board.mask) != 1:
            self.choose_new_target()
            return
        if self.current_step < self.movement_steps:
            t = 1 / self.movement_steps
            new_x = int(self.center_pos[0] + (self.target_pos[0] - self.center_pos[0]) * t)
            new_y = int(self.center_pos[1] + (self.target_pos[1] - self.center_pos[1]) * t)
            if self.board.mask.get_at((new_x, new_y)) == 1:  
                self.center_pos = (new_x, new_y)
            self.rotation_angle += (self.target_rotation - self.rotation_angle) * (1 / self.movement_steps)
            self.rotation_angle %= 360
            self.line_length += (self.target_line_length - self.line_length) * t
            self.current_step += 1
            self.board.qixPos = self.center_pos
        else:
            self.choose_new_target()  
        
        if self.current_step % 10 == 0:
            self.trail_points.append(self.getQixLine())
            if len(self.trail_points) > 5:
                self.trail_points.pop(0)

    def getQixLine(self):
        angle_rad = math.radians(self.rotation_angle)
        x_offset = int(self.line_length * math.cos(angle_rad))
        y_offset = int(self.line_length * math.sin(angle_rad))

        start = (self.center_pos[0] - x_offset, self.center_pos[1] - y_offset)
        end = (self.center_pos[0] + x_offset, self.center_pos[1] + y_offset)

        start = self.trimPoint(start)
        end = self.trimPoint(end)

        return start, end

    def trimPoint(self, point):
        x, y = point
        max_attempts = 150  # Prevents infinite looping

        for _ in range(max_attempts):
            if self.board.findMaskPixel((x, y), self.board.mask) == 1:
                return (x, y)  # Found a valid spot
            x = (x*3 + self.center_pos[0]) // 4
            y = (y*3 + self.center_pos[1]) // 4
        return self.center_pos

    def playerHit(self):
        start, end = self.getQixLine()
        for point in self.get_line_pixels(start, end):
            if self.board.findMaskPixel(point, self.board.dynamicMask) == 0:
                return True  
        return False  

    def get_line_pixels(self, start, end):
        x1, y1 = start
        x2, y2 = end
        pixels = []

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            pixels.append((x1, y1))
            if (x1, y1) == (x2, y2):
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        return pixels

    def renderQix(self, screen):
        for i, (start, end) in enumerate(self.trail_points):
            alpha = int(255 * (i + 1) / len(self.trail_points))  # Fade effect
            color = (255, 0, 0, alpha)  
            self.draw_transparent_line(screen, color, start, end, 3)

        start, end = self.getQixLine()
        pygame.draw.line(screen, (255, 0, 0), start, end, 3)

    def draw_transparent_line(self, screen, color, start, end, width):
        surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.line(surface, color, start, end, width)
        screen.blit(surface, (0, 0))
