from cgitb import text
from turtle import textinput
from constants import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE
from state_machine import GameState
import pygame as pg
import pygame_textinput
import utils.score_storage as storage

class SplashScreen(GameState):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.font = pg.font.SysFont('Calibri', 25, True, False)
        self.text1 = self.font.render("Welcome to Petris!",True,WHITE)
        self.text2 = self.font.render("Fill your username and press enter to start playing",True,WHITE)
        self.text3 = pg.font.SysFont('Calibri', 30, True, False).render("Scoreboard", True, WHITE)
        self.user_name = pygame_textinput.TextInputVisualizer(font_color=WHITE, cursor_color=WHITE)
        self.next_state = "GAMEPLAY"
        self.scoreboard = storage.read_scores()

    def startup(self, persistent):
        self.scoreboard = storage.read_scores()

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

        height = 50
        surface.blit(self.text1,(self.screen_rect.centerx-(self.text1.get_width()/2),height))

        height+= (self.text1.get_height()+5)
        surface.blit(self.text2,(self.screen_rect.centerx-(self.text2.get_width()/2),height))

        height+= (self.text2.get_height()+5)
        width = self.user_name.surface.get_width()
        pg.draw.rect(surface,WHITE,[SCREEN_WIDTH/2-width/2-10, height,width+20,self.user_name.surface.get_height()+20], 1, 4)

        height+=10
        surface.blit(self.user_name.surface,(SCREEN_WIDTH/2-width/2,height))
        
        height+=(self.user_name.surface.get_height()+30)
        surface.blit(self.text3,(self.screen_rect.centerx-(self.text3.get_width()/2),height))
        
        height+=(10+self.text3.get_height())
        for name,score in self.scoreboard:
            name_text = self.font.render(name, True, WHITE)
            score_text = self.font.render(str(score), True, WHITE)
            surface.blit(name_text,(SCREEN_WIDTH/2-200,height))
            surface.blit(score_text,(SCREEN_WIDTH/2+200,height))
            height+=name_text.get_height()
            if height>SCREEN_HEIGHT-50:
                break

        