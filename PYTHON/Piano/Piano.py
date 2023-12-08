from threading import Thread as Thr
import pygame as pg
from time import sleep

pg.init()
pg.mixer.init()


notes = ['C-1', 'C-2', 'C-3', 'C-4']

pg.mixer.set_num_channels(len(notes))


def piano(np, time):
    sleep(time)
    pg.mixer.Sound(np).play()
    sleep(time)

    

