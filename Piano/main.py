#!/usr/bin/python3
import os
import sys
import pygame as pg
from time import sleep

from keys import piano_notes, keyboard_keys
print(len(piano_notes))
pg.init()

WIDTH, HEIGHT = 1800, 450
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('PyPiano')
pg.display.set_icon(pg.image.load(os.path.join('Piano', 'assets', 'logo.png')))

bgColor = (255, 229, 178)
pianoSize = (1729, 185)

piano = pg.transform.scale(pg.image.load(os.path.join('Piano', 'assets', 'piano2.png')), pianoSize)
clef = pg.image.load(os.path.join('Piano', 'assets', 'clef2.png'))


def main():
    """ Main game  """
    HOTKEY = 0
    WIN.fill(bgColor)
    WIN.blit(piano, (((WIDTH - piano.get_width()) / 2), 180))
    WIN.blit(clef, ((WIDTH - clef.get_width()) + -50, 15))


    while True:
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_0:
                    HOTKEY = 0
                if event.key == pg.K_1:
                    HOTKEY = 1
                if event.key == pg.K_2:
                    HOTKEY = 2
                if event.key == pg.K_3:
                    HOTKEY = 3
                if event.key == pg.K_4:
                    HOTKEY = 4
                if event.key == pg.K_5:
                    HOTKEY = 5
                if event.key == pg.K_6:
                    HOTKEY = 6
                if event.key == pg.K_7:
                    HOTKEY = 7
                if event.key == pg.K_8:
                    HOTKEY = 8
                if event.key == pg.K_9:
                    HOTKEY = 9


        pg.display.flip()

main()