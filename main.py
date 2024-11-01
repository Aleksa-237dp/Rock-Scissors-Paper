# https://waksoft.susu.ru/2019/04/24/pygame-shpargalka-dlja-ispolzovanija/

import pygame as pg
from pygame.locals import (K_ESCAPE, KEYDOWN)
from settings import sc, uc, ft, nr, scores, colors, sg
from sound_game import sound_game
from player import player
from computer import computer
from draw_text import dt
from button import btn_start, btn_paper, btn_scissors, btn_stone

pg.init()

pg.display.set_caption('Камень - Ножницы - Бумага')
pg.display.set_icon(pg.image.load('images/l_scissors.png'))

clock = pg.time.Clock()
counter_rotation = 0
nr.change_rounds(5)

sound_game.play_background('music/background_music.mp3')

running = True

while running:
    clock.tick(sc.tick)
    sc.win.fill((sc.color))

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pg.QUIT:
            running = False

        btn_start.handle_event(event)
        btn_stone.handle_event(event)
        btn_scissors.handle_event(event)
        btn_paper.handle_event(event)

    dt.create_text(player_name=player.name,
                   computer_name=computer.name,
                   computer_score=scores.comp_score,
                   player_score=scores.pl_score,
                   number_rounds=nr.number_rounds)
    dt.blits()

    if not sg.start_game and not uc.users_choice:

        btn_start.draw(sc.win)
        player.blit_image(player.start, player.start_rect)
        computer.blit_image(computer.start, computer.start_rect)

        if btn_start.is_clicked:
            btn_start.is_clicked = False
            sg.change_start_game()

    elif sg.start_game and not uc.users_choice:

        selected_text = ft.arial.render('Сделай свой выбор', True, (colors.yellow))
        sc.win.blit(selected_text,
                    ((sc.width / 2) - 130, (sc.height / 2) - 100))

        btn_stone.draw(sc.win)
        btn_scissors.draw(sc.win)
        btn_paper.draw(sc.win)
        player.blit_image(player.start, player.start_rect)
        computer.blit_image(computer.start, computer.start_rect)

        if btn_stone.is_clicked:
            player.set_choice(1)

        if btn_scissors.is_clicked:
            player.set_choice(2)

        if btn_paper.is_clicked:
            player.set_choice(3)

        if btn_stone.is_clicked or btn_scissors.is_clicked or btn_paper.is_clicked:
            btn_paper.is_clicked = False
            btn_scissors.is_clicked = False
            btn_stone.is_clicked = False
            computer.random_choice()
            uc.change_users_choice()
            counter_rotation = 6
            sound_game.play_start('music/counting_down.mp3')

    elif sg.start_game and uc.users_choice:
        if counter_rotation > 0:
            counter_rotation -= 1
            player.change_rotation(45)
            computer.change_rotation(45)
            player.blit_image(player.start_rotate, player.start_rect)
            computer.blit_image(computer.start_rotate, computer.start_rect)

            pg.display.update()
            pg.time.delay(520)
        else:
            if player.choice == computer.choice:
                scores.change_scores(0, 0)
            elif player.choice == 1 and computer.choice == 2:
                scores.change_scores(1, 0)
            elif player.choice == 2 and computer.choice == 3:
                scores.change_scores(1, 0)
            elif player.choice == 3 and computer.choice == 1:
                scores.change_scores(1, 0)
            else:
                scores.change_scores(0, 1)

            
            sound_game.play_choice('music/choice.mp3')
            sc.win.fill((sc.color))
            player.view_choice()
            computer.view_choice()
            sg.change_start_game()
            uc.change_users_choice()
            nr.decrease_rounds()
            dt.create_text(player_name=player.name,
                           computer_name=computer.name,
                           computer_score=scores.comp_score,
                           player_score=scores.pl_score,
                           number_rounds=nr.number_rounds)
            dt.blits()
            pg.display.update()
            pg.time.delay(3000)

    if nr.number_rounds == 0:
        nr.change_rounds(5)
        scores.pl_score = 0
        scores.comp_score = 0

    pg.display.update()


pg.quit()
