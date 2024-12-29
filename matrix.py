import pygame
from pygame.surface import Surface
import random
import copy

pygame.font.init()
font = pygame.font.SysFont("Arial", 15)

class Matrix:
    def __init__(self, screen: Surface, n: int):
        self.screen = screen
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.add_new_tile(16384)

        
        self.colours = {
            2:(172, 250, 112),
            4:(118, 236, 126),
            8:(54, 220, 141),
            16:(10, 202, 154),
            32:(10, 181, 163),
            64:(10, 161, 164),
            128:(10, 141, 161),
            256:(10, 122, 154),
            512:(10, 103, 148),
            1024:(80, 84, 131),
            2048:(133, 65, 109),
            4096:(200, 70, 156),
            8192:(230, 80, 170),
            16384:(240, 90, 180)
        }

    def transpose(self) -> None:
        self.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

    def display(self) -> None: 
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix)):
                if self.matrix[i][j] != 0:
                    val  =self.matrix[i][j]
                    pygame.draw.rect(self.screen, self.colours[val], (20 + 600/len(self.matrix)*j, 20 + 600/len(self.matrix)*i, 600/len(self.matrix) - 20, 600/len(self.matrix) - 20), border_radius=5)

                    # Render the text
                    text_surface = font.render(str(val), True, (42, 46, 84))
                    text_rect = text_surface.get_rect(center=(20 + 600/len(self.matrix)*j + (600/len(self.matrix)/2)-10, 20 + 600/len(self.matrix)*i + (600/len(self.matrix)/2)-10))
                    self.screen.blit(text_surface, text_rect)
                    
                pygame.draw.rect(self.screen, (42, 46, 84), (12 + 600/len(self.matrix)*j, 12 + 600/len(self.matrix)*i, 600/len(self.matrix) - 5, 600/len(self.matrix) - 5), 3, 5)

    def check_collisions(self, direction:str):
        
        localcopy = copy.deepcopy(self.matrix)

        if direction == 'u' or direction == 'd':
            self.transpose()

        for i in range(0, len(self.matrix)):
            row  = self.matrix[i]

            if direction == "r" or direction == 'd':
                row = row[::-1]

            #  start slide
            if row.count(0) == len(self.matrix):
                continue
            else:
                while 0 in row:
                    row.pop(row.index(0))
            
            # end slide

            # start combine
            
            for k in range(0, len(row) - 1):
                # addition occurs
                if row[k] == row[k+1]: 
                    row[k] = row[k]*2
                    row[k+1] = 0
            # end combine

            # slide 2 start

            if row.count(0) == len(self.matrix):
                continue
            else:
                while 0 in row:
                    row.pop(row.index(0))

            # slide 2 end

            while len(row) < len(self.matrix):
                row.append(0)

            if direction == "r" or direction == 'd':
                row = row[::-1]

            self.matrix[i] = row

        if direction == 'u' or direction == 'd':
            self.transpose()

        return localcopy == self.matrix

    def add_new_tile(self, n:int = 2):
            
        while True:
            x = random.randint(0,len(self.matrix)-1)
            y = random.randint(0,len(self.matrix)-1)

            if self.matrix[x][y] == 0:
                self.matrix[x][y] = n
                break

    def check_loss(self) -> bool:
        # Check for any empty spaces
        for row in self.matrix:
            # print(row)
            if 0 in row:
                return False

        # Check for any possible merges horizontally
        for row in self.matrix:
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    return False

        # Check for any possible merges vertically
        for col in range(len(self.matrix[0])):
            for row in range(len(self.matrix) - 1):
                if self.matrix[row][col] == self.matrix[row + 1][col]:
                    return False

        # If no empty spaces and no possible merges, the game is lost
        return True