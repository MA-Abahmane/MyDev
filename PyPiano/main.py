#!/usr/bin/python3
from email.policy import default
import os
import sys
import pygame
import pygame as pg

from keys import piano_notes, keyboard_keys

pg.init()
class PyPiano:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 1800, 450
        self.WIN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('PyPiano')
        pg.display.set_icon(pg.image.load(os.path.join('PyPiano', 'assets', 'logo.png')))

        self.bgColor = (255, 229, 178)
        self.pianoSize = (1729, 185)

        self.piano = pg.transform.scale(pg.image.load(os.path.join('PyPiano', 'assets', 'piano2.png')), self.pianoSize)
        self.clef = pg.image.load(os.path.join('PyPiano', 'assets', 'clef2.png'))

        pg.mixer.set_num_channels(40)  # Adjust the number of channels as needed
        self.HOTKEY = None

    def play_piano(self, N):
        print(N)
        sound_path = pg.mixer.Sound(f'PyPiano/assets/notes/{piano_notes[N][1]}.wav')
        sound_path.play()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                # Group calls
                match event.unicode:
                    case '0':
                        self.HOTKEY = 0
                    case '1':
                        self.HOTKEY = 1
                    case '2':
                        self.HOTKEY = 2
                    case '3':
                        self.HOTKEY = 3
                    case '4':
                        self.HOTKEY = 4
                    case '5':
                        self.HOTKEY = 5
                    case '6':
                        self.HOTKEY = 6
                    case '7':
                        self.HOTKEY = 7
                    case '8':
                        self.HOTKEY = 8
                    case '9':
                        self.HOTKEY = 9
                    case '10':
                        self.HOTKEY = 10
                    case '11':
                        self.HOTKEY = 11
                    case '12':
                        self.HOTKEY = 12

                if event.unicode in keyboard_keys:
                    print(True)

                if (self.HOTKEY != None):
                    self.play_piano(self.HOTKEY)

    def update_display(self):
        self.WIN.fill(self.bgColor)
        self.WIN.blit(self.piano, (((self.WIDTH - self.piano.get_width()) / 2), 180))
        self.WIN.blit(self.clef, ((self.WIDTH - self.clef.get_width()) - 50, 15))
        pg.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update_display()

if __name__ == "__main__":
    piano_app = PyPiano()
    piano_app.run()
