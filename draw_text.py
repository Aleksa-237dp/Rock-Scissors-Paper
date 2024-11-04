from settings import colors, ft, sc
from player import player
from computer import computer

# отрисовка текста
class WinText:

    def __init__(self):

        self.number_rounds = 0
        self.player_score = 0
        self.computer_score = 0
        self.score_text_heading = None
        self.player_name = None
        self.computer_name = None

    def create_text(self, player_name, computer_name, player_score,
                    computer_score, number_rounds):

        self.player_name = player_name
        self.computer_name = computer_name
        self.player_score = player_score
        self.computer_score = computer_score
        self.number_rounds = number_rounds

        self.number_rounds_heading = ft.arial.render('Осталось раундов', True,
                                                     (colors.yellow))
        self.player_name = ft.roboto.render(player.name, True, (colors.white))
        self.computer_name = ft.roboto.render(computer.name, True,
                                              (colors.white))
        self.score_text_heading = ft.roboto.render('Очки', True,
                                                   (colors.white))
            
    def blits(self):
        
        sc.win.blit(self.player_name, (30, 50))
        sc.win.blit(self.score_text_heading,
                    ((sc.width - 80) / 2, sc.height - 100))
        sc.win.blit(self.computer_name, (sc.width - 210, 50))
        sc.win.blit(self.number_rounds_heading, (sc.width / 2 - 140, 50))
        sc.win.blit(
            ft.arial.render(str(self.number_rounds), True, (colors.yellow)),
            ((sc.width / 2) - 20, sc.height - 500))
        sc.win.blit(
            ft.arial.render(str(self.player_score), True, (colors.yellow)),
            (80, sc.height - 50))
        sc.win.blit(
            ft.arial.render(str(self.computer_score), True, (colors.yellow)),
            (sc.width - 100, sc.height - 50))
        
        
dt = WinText()
