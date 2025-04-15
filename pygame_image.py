import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False) #左右反転
    koukaton_3 = pg.image.load("fig/3.png") #練習2
    koukaton_3 = pg.transform.flip(koukaton_3,True,False) #左右反転
    kk_rct = koukaton_3.get_rect()
    kk_rct.center = 300, 200

    tmr = 0
    
    while True:
        
        x = tmr%3200#画像がループする

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))#上に動く

        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0, +1))#下に動く

        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1, 0))#左に動く

        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((+1, 0))#右に動く
        
        screen.blit(bg_img, [-x, 0]) #左側に画像が動く
        screen.blit(bg_img2, [-x+1600, 0]) #左側に画像が動く            
        screen.blit(bg_img, [-x+3200, 0]) #左側に画像が動く
        screen.blit(koukaton_3, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()