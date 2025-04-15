import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton_3 = pg.image.load("fig/3.png") #練習2
    koukaton_3 = pg.transform.flip(koukaton_3,True,False) #左右反転
    tmr = 0
    
    while True:
        x = tmr 
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0]) #左側に画像が動く
        screen.blit(koukaton_3, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()