import pygame as pg
import numpy as np
import random as rnd
from block import * 
from func import *
pg.init()



#* ---------| Function |---------
def BombCounter(array, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ( Control(x + j, y + i, len(array) - 1, len(array[0]) - 1) ):
                if array[y + i, x + j] == BOMB:
                    count += 1
    return count


#* ---------| World Setup |---------
world = np.ones((15, 15), dtype=int)

world *= -1

BOMB = 9

bombs = []
i = 0
while i < world.shape[0] + 5:
    x, y = rnd.randint(0, world.shape[0] - 1), rnd.randint(0, world.shape[1] - 1)
    if (world[y, x] != BOMB):
        world[y, x] = BOMB
        i += 1
        bombs.append((y, x))
    else:
        x, y = rnd.randint(0, world.shape[0]), rnd.randint(0, world.shape[1])

for ind_y, val_y in enumerate(world):
    for ind_x, val_x in enumerate(val_y):
        if world[ind_y, ind_x] != BOMB: 
            world[ind_y, ind_x] = BombCounter(world, ind_x, ind_y)


#* ---------| Function |---------
def CleanPlace(array, blocks: list[Block], x, y, i = 0, flage = False):
    if (Control(x, y, len(array) - 1, len(array[0]) - 1)) and (i < 4) and (not flage):
        if (array[y, x] < 9):
            f = flage
            d = i + 1

            for b in blocks:
                if b.GetPos() == (y, x) and b.GetText() != "!":
                    b.SetColor(Change(array[y, x])[0], Change(array[y, x])[1])
                    b.SetText(str(array[y, x]))

                    if (array[y, x] > 0):
                        f = True


            # CleanPlace(array, blocks, x - 1, y + 1, d, f)
            CleanPlace(array, blocks, x, y + 1, d, f)
            # CleanPlace(array, blocks, x + 1, y + 1, d, f)

            CleanPlace(array, blocks, x - 1, y, d, f)

            CleanPlace(array, blocks, x + 1, y, d, f)

            # CleanPlace(array, blocks, x - 1, y - 1, d, f)
            CleanPlace(array, blocks, x, y - 1, d, f)
            # CleanPlace(array, blocks, x + 1, y - 1, d, f)


#* ---------| Pygame Visual |---------

# Setup
w, h = world.shape
block_size = 50
margin = 2.5



display = pg.display.set_mode((w * block_size, h * block_size))
pg.display.set_caption("Saper =)")



blocks: list[Block] = []
for ind_y, val_y in enumerate(world):
        for ind_x, val_x in enumerate(val_y):
            blocks.append(Block(display, ind_x, ind_y, block_size, margin))

isLeftClick = False
isRightClick = False

allMarks = []

isMark = True
run = True
while run:
    display.fill((255, 255, 255))

    for ind, block in enumerate(blocks): 
        block.draw()

        if (block.onClick(0)) and (not isLeftClick):

            pos_blokc = block.GetPos()
            if (world[pos_blokc[0], pos_blokc[1]] == BOMB): # got on bomb
                block.SetColor(Change(9)[0], Change(9)[1])
                block.SetText("B")
                run = False
            if (0 < world[pos_blokc[0], pos_blokc[1]] < 9): # got on number
                blockColor, borderColor = Change(world[pos_blokc[0], pos_blokc[1]])

                block.SetColor(blockColor, borderColor)
                block.SetText(str(world[pos_blokc[0], pos_blokc[1]]))
            if (world[pos_blokc[0], pos_blokc[1]] == 0): # got on empty place
                CleanPlace(world, blocks, pos_blokc[1], pos_blokc[0])

            isLeftClick = True

        if (block.onClick(2)) and (not isRightClick):
            block.Mark()
            isRightClick = True
            allMarks.append(block.GetPos())


    if (not pg.mouse.get_pressed()[0]):
        isLeftClick = False
    if (not pg.mouse.get_pressed()[2]):
        isRightClick = False

    if (Equals(allMarks, bombs)): # detect if user marked all bombs
        print("Win")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()
    pg.time.Clock().tick(60)
pg.quit()
