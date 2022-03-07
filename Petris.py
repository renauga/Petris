

import sys
import pygame as pg
import state_machine
from states.gameplay import Gameplay

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800,900))
    states = {#"SPLASH": SplashScreen(),
                   "GAMEPLAY": Gameplay()}
    game = state_machine.Game(screen, states, "GAMEPLAY")
    game.run()
    pg.quit()
    sys.exit()