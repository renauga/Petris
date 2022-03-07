

import sys
import pygame as pg
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import state_machine
from states.gameplay import Gameplay
from states.splash_screen import SplashScreen

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    states = {"SPLASH": SplashScreen(),
                   "GAMEPLAY": Gameplay()}
    game = state_machine.Game(screen, states, "SPLASH")
    game.run()
    pg.quit()
    sys.exit()