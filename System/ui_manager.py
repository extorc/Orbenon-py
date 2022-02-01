import pygame_gui
import pygame

class UIManager:
  @staticmethod
  def add_button(x, y, width, height, text, manager):
    return pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (width, height)),text=text,manager=manager)