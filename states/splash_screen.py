from cgitb import text
from turtle import textinput
from constants import BLACK, SCREEN_WIDTH, WHITE
from state_machine import GameState
import pygame as pg
import pygame_textinput

class SplashScreen(GameState):
    def __init__(self):
        super(SplashScreen, self).__init__()
        font = pg.font.SysFont('Calibri', 25, True, False)
        self.text1 = font.render("Welcome to Petris!",True,WHITE)
        self.text2 = font.render("Fill your username and press enter to start playing",True,WHITE)
        self.user_name = pygame_textinput.TextInputVisualizer(font_color=WHITE, cursor_color=WHITE)
        self.next_state = "GAMEPLAY"


    def get_events(self, events):
        self.user_name.update(events)
        for event in events:
            if event.type == pg.QUIT:
                self.quit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.persist["username"] = self.user_name.value
                    self.done = True

    def draw(self, surface):
        surface.fill(BLACK)
        surface.blit(self.text1,(self.screen_rect.centerx-(self.text1.get_width()/2),50))
        surface.blit(self.text2,(self.screen_rect.centerx-(self.text2.get_width()/2),55+self.text1.get_height()))
        width = self.user_name.surface.get_width()
        height = self.user_name.surface.get_height()
        pg.draw.rect(surface,WHITE,[SCREEN_WIDTH/2-width/2-10, 60+self.text1.get_height()+self.text2.get_height(),width+20,height+20], 1, 4)
        surface.blit(self.user_name.surface,(SCREEN_WIDTH/2-width/2,70+self.text1.get_height()+self.text2.get_height()))
        