from block import * 
from game import *
import time

class Display(Game):
    def __init__(self):
        super().__init__()

        w, h = self.world.shape
        block_size = 50
        margin = 2.5

        self.display = pg.display.set_mode((w * block_size, h * block_size))
        pg.display.set_caption("Saper =)")

        self.Blocks: list[Block] = []
        for ind_y, val_y in enumerate(self.world):
            for ind_x, _ in enumerate(val_y):
                self.Blocks.append(Block(self.display, ind_x, ind_y, block_size, margin))

        self.isLeftClick = False
        self.isRightClick = False

        self.allMarks = []

        self.isMark = True
        self.run = True

        print(self.world)

        self.Run()

    def CleanPlace(self, blocks: list[Block], x, y, i = 0, flage = False):
        if ((i < 4) and (not flage)):
            num = self.world[y, x]
            if (num == 0):
                f = flage
                d = i + 1

                for b in blocks:
                    if b.GetPos() == (y, x):
                        b.SetColor(self.Change(self.world[y, x])[0], self.Change(self.world[y, x])[1])
                        b.SetText(str(self.world[y, x]))

                        if (self.world[y, x] > 0 and d > 1):
                            f = True


                self.CleanPlace(blocks, x - 1, y + 1, d, f)
                self.CleanPlace(blocks, x, y + 1, d, f)
                self.CleanPlace(blocks, x + 1, y + 1, d, f)

                self.CleanPlace(blocks, x - 1, y, d, f)

                self.CleanPlace(blocks, x + 1, y, d, f)

                self.CleanPlace(blocks, x - 1, y - 1, d, f)
                self.CleanPlace(blocks, x, y - 1, d, f)
                self.CleanPlace(blocks, x + 1, y - 1, d, f)

    def Change(self, num: int):
        match num:
            case 9:
                return ((230, 70, 70), (170, 10, 10))
            case 10:
                return ((50, 230, 20), (20, 200, 0))
            case 0:
                return ((230, 230, 230), (170, 170, 170))
            case _:
                return (((255 / 8) * num, 0, 0), (30 * num + 10 - 20, 0, 0))

    def Run(self):
        while self.run:
            self.display.fill((255, 255, 255))
            
            if (not pg.mouse.get_pressed()[0]):
                isLeftClick = False
            if (not pg.mouse.get_pressed()[2]):
                isRightClick = False

            for block in self.Blocks: 
                block.draw()
                BlocksPos = block.GetPos()
                if (self.world[BlocksPos[0], BlocksPos[1]] == 10):
                    blockColor, borderColor = self.Change(self.world[BlocksPos[0], BlocksPos[1]])

                    block.SetColor(blockColor, borderColor)
                    block.SetText("S")

                if (block.onClick(0)) and (not isLeftClick):
                    if (self.world[BlocksPos[0], BlocksPos[1]] == self.BOMB): # got on bomb
                        block.SetColor(self.Change(9)[0], self.Change(9)[1])
                        block.SetText("B")
                        self.run = False
                    if (0 < self.world[BlocksPos[0], BlocksPos[1]] < 9): # got on number
                        blockColor, borderColor = self.Change(self.world[BlocksPos[0], BlocksPos[1]])

                        block.SetColor(blockColor, borderColor)
                        block.SetText(str(self.world[BlocksPos[0], BlocksPos[1]]))
                    self.CleanPlace(self.Blocks, BlocksPos[1], BlocksPos[0])

                    isLeftClick = True

                if (block.onClick(2)) and (not isRightClick):
                    block.Mark()
                    isRightClick = True
                    self.allMarks.append(block.GetPos())

            if (self.Equals(self.allMarks, self.bombs)): # detect if user marked all bombs
                print("Win")

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

            pg.display.flip()
            pg.time.Clock().tick(60)
        pg.quit()

if __name__ == "__main__":
    G = Display()