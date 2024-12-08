'''The Button class accepts the following parameters: 
- x , y - coordinates of the upper left corner of the button 
- width , height - width and height of the button 
- text - text displayed on the button (optional parameter) 
- image - image displayed on the button (optional parameter) 
- font - font file path (optional parameter) 
- font_size - font size (optional parameter) 
- bg_color - button background color (optional parameter) 
- text_color - button text color (optional parameter) 
- hover_color - button color when hovering over it (optional parameter) 
 
You can create an instance of Button class by specifying the required parameters and then call the draw method to display the button on the screen. The handle_event method handles mouse events to keep track of button hovering and clicks.'''

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

'''The click_color property , defines the color of the button when it is clicked. The draw method checks the state of the button ( is_clicked ), and if the button is clicked, the click_color is used . The handle_event method handles the MOUSEBUTTONDOWN event to set the is_clicked flag to True , and the MOUSEBUTTONUP event resets the is_clicked flag to False . 
 
When the button is clicked, it will change its color to click_color .'''
