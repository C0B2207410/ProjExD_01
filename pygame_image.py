import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    koukaton_imgs = [pg.transform.rotozoom(koukaton_img, i, 1) for i in range(10)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-tmr, 0])
        screen.blit(koukaton_imgs[tmr%10], [300, 200])
        pg.display.update()
        tmr += 1       
        if tmr > 1600:
            tmr = 0 
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()