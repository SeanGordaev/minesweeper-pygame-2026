import numpy as np
import random as rnd

class Game:
    def __init__(self):
        self.world = np.ones((12, 12), dtype=int)
        self.world *= -1

        self.BOMB = 9
        self.bombs = []

        self.SafeBlockSet = False

        self.MakeBombs()
        self.SetCount()
        self.FoundSafeBlock()

    def MakeBombs(self):
        i = 0
        while i < self.world.shape[0] * 1.75:
            y, x = rnd.randint(0, self.world.shape[0] - 1), rnd.randint(0, self.world.shape[1] - 1)
            if (self.world[y, x] != self.BOMB):
                self.world[y, x] = self.BOMB
                self.bombs.append((y, x))
                i += 1

    def SetCount(self):
        for ind_y, val_y in enumerate(self.world):
            for ind_x, _ in enumerate(val_y):
                if self.world[ind_y, ind_x] != self.BOMB: 
                    self.world[ind_y, ind_x] = self.BombCounter(ind_x, ind_y)

    def BombCounter(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.Control(x + j, y + i)):
                    if self.world[y + i, x + j] == self.BOMB:
                        count += 1
        return count
    
    def FoundSafeBlock(self):
        for ind_y, val_y in enumerate(self.world):
            for ind_x, _ in enumerate(val_y):
                if (not self.SafeBlockSet and self.world[ind_y, ind_x] == 0):
                    # self.SafeBlockSet = True
                    self.world[ind_y, ind_x] == 1

    def Control(self, x, y, min_X = 0, min_Y = 0):
        max_X = len(self.world) - 1
        max_Y = len(self.world[0]) - 1
        if ((min_X <= x <= max_X) and (min_Y <= y <= max_Y)):
            return True
        return False

    
    def Equals(self, A1, A2):
        if (len(A1) != len(A2)):
            return False
        
        for b in A1:
            if not (b in A2):
                return False
            
        return True
