import pygame as pg
from func import *
pg.init()

class Block:
    def __init__(self, display, x, y, size, margin = 0):
        self.display = display
        self.x = x
        self.y = y
        self.size = size
        self.margin = margin

        self.preText = None
        self.preBlockColor = None
        self.preBorderColor = None

        self.blockColor = Grey(152)
        self.borderColor = Grey(100)

        self.Rect = pg.Rect(self.x * self.size + self.margin, 
                            self.y * self.size + self.margin, 
                            self.size - self.margin * 2, 
                            self.size - self.margin * 2)
        
        self.text = ""
        self.font = pg.font.Font(None, 35)
        self.text_surf = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (x * size + size / 2, y * size + size / 2)

        self.toMark = True

        
    def onBlock(self, x: int, y: int):
        onWidth = self.Rect.x <= x <= self.Rect.x + self.Rect.width
        onHeight = self.Rect.y <= y <= self.Rect.y + self.Rect.height
        if (onWidth and onHeight):
            return True
        return False
    
    def onClick(self, ind):
        x, y = pg.mouse.get_pos()
        isClick = pg.mouse.get_pressed()[ind]
        if (self.onBlock(x, y) and isClick):
            return True
        return False
    
    def GetPos(self):

        '''
        return position of block

        for work with numpy first cordinate is y and second cordinate is x

        return (self.y, self.x)
        
        '''

        return (self.y, self.x)
    
    def SetColor(self, blockColor, borderColor):
        self.preBlockColor = self.blockColor
        self.preBorderColor = self.borderColor

        self.blockColor = blockColor
        self.borderColor = borderColor

    def GetText(self):
        return self.text
    
    def SetSize(self, w, h):
        self.Rect = pg.Rect(self.x * w + self.margin, 
                            self.y * h + self.margin, 
                            w - self.margin * 2, 
                            h - self.margin * 2)
    
    def SetText(self, text):
        self.preText = self.text


        self.text = text

        self.text_surf = self.font.render(self.text, True, (200, 200, 200))
        self.display.blit(self.text_surf, self.text_rect)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (self.x * self.size + self.size / 2, self.y * self.size + self.size / 2)

    def Mark(self):
        if self.toMark:
            self.SetColor((250, 165, 45), (200, 130, 40))
            self.SetText("!")
        else:
            self.SetColor(self.preBlockColor, self.preBorderColor)
            self.SetText(self.preText)
        self.toMark = not self.toMark
    
    def draw(self):
        pg.draw.rect(self.display, self.blockColor, self.Rect, 0, 5)
        pg.draw.rect(self.display, self.borderColor, self.Rect, 3, 5)

        self.display.blit(self.text_surf, self.text_rect)