'''Класс  Button  принимает следующие параметры: 
-  x ,  y  - координаты верхнего левого угла кнопки 
-  width ,  height  - ширина и высота кнопки 
-  text  - текст, отображаемый на кнопке (необязательный параметр) 
-  image  - изображение, отображаемое на кнопке (необязательный параметр) 
-  font  - путь к файлу шрифта (необязательный параметр) 
-  font_size  - размер шрифта (необязательный параметр) 
-  bg_color  - цвет фона кнопки (необязательный параметр) 
-  text_color  - цвет текста кнопки (необязательный параметр) 
-  hover_color  - цвет кнопки при наведении на нее (необязательный параметр) 
 
Вы можете создать экземпляр класса  Button , указав необходимые параметры, и затем вызвать метод  draw  для отображения кнопки на экране. Метод  handle_event  обрабатывает события мыши, чтобы отслеживать наведение и клики на кнопку.'''

import pygame as pg
from pygame.locals import *
pg.init()

from settings import sc


class Button:

    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 text='',
                 image=None,
                 font=None,
                 font_size=26,
                 bg_color=(255, 0, 0),
                 text_color=(255, 255, 255),
                 hover_color=(255, 128, 0),
                 click_color=(0, 204, 0)):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.image = image
        self.font = pg.font.Font(
            font, font_size) if font else pg.font.SysFont(
                'Arial', font_size)
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.click_color = click_color
        self.is_hovered = False
        self.is_clicked = False

    def draw(self, surface):
        if self.is_clicked:
            color = self.click_color
        elif self.is_hovered:
            color = self.hover_color
        else:
            color = self.bg_color

        pg.draw.rect(surface, color, self.rect, border_radius=20)

        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

        if self.image:
            image_rect = self.image.get_rect(center=self.rect.center)
            surface.blit(self.image, image_rect)

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.is_clicked = True

        # elif event.type == MOUSEBUTTONUP:
        #     self.is_clicked = False



btn_start = Button(sc.width / 2 - 100, sc.height / 2, 200, 50, text='Старт')
btn_stone = Button(sc.width / 2 - 175, sc.height / 2 + 100, 100, 50, text='Камень')
btn_scissors = Button(sc.width / 2 -50, sc.height / 2 + 100, 100, 50, text='Ножницы')
btn_paper = Button(sc.width / 2 + 75, sc.height / 2 + 100, 100, 50, text='Бумага')

'''Cвойство  click_color , определяет цвет кнопки при нажатии. В методе  draw  проверяется состояние кнопки ( is_clicked ), и если кнопка нажата, то используется цвет  click_color . В методе  handle_event  обрабатывается событие  MOUSEBUTTONDOWN , чтобы установить флаг  is_clicked  в значение  True , а событие  MOUSEBUTTONUP  сбрасывает флаг  is_clicked  в значение  False . 
 
При нажатии на кнопку она будет менять цвет на  click_color .'''
