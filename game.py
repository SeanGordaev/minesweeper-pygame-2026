import pygame as pg
import block
pg.init()

class Game:
    def __init__(self):
        self.w, self.h = 500, 500

        self.root = pg.display.set_mode((self.w, self.h))
        pg.display.set_caption("Menu")

        self.text = ""
        self.font = pg.font.Font(None, 80)



        self.Game()


    def SetSizeDisplay(self, w, h):
        self.root = pg.display.set_mode((w, h))

    def Menu(self):

        text = "Minesweeper"
        text_surf = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.center = (self.w / 2, self.h / 4 + self.font.get_height() / 2)

        run = True
        while run:
            self.root.fill((255, 255, 255))

            self.root.blit(text_surf, text_rect)
 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            pg.display.flip()
            pg.time.Clock().tick(60)
        pg.quit()


    def Game(self):
        self.Menu()

        self.SetSizeDisplay(1000, 700)

        self.Menu()

if __name__ == "__main__":
    t = Game()
    