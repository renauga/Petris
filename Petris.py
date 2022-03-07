

import sys
import pygame as pg
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import state_machine
from states.gameplay import Gameplay

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    states = {#"SPLASH": SplashScreen(),
                   "GAMEPLAY": Gameplay()}
    game = state_machine.Game(screen, states, "GAMEPLAY")
    game.run()
    pg.quit()
    sys.exit()