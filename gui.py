import pygame
from pygame.locals import *

class Menu:
    def __init__(self):
        self.options = []
        self.selected_option = None

    def add_option(self, option):
        self.options.append(option)

    def select_option(self, option):
        if option in self.options:
            self.selected_option = option

    def handle_input(self, key):
        if key == "up":
            self._select_previous_option()
        elif key == "down":
            self._select_next_option()
        elif key == "enter":
            self._execute_selected_option()

    def _select_previous_option(self):
        if not self.options:
            return

        if self.selected_option is None:
            self.selected_option = self.options[-1]
        else:
            index = self.options.index(self.selected_option)
            if index == 0:
                self.selected_option = self.options[-1]
            else:
                self.selected_option = self.options[index - 1]

    def _select_next_option(self):
        if not self.options:
            return

        if self.selected_option is None:
            self.selected_option = self.options[0]
        else:
            index = self.options.index(self.selected_option)
            if index == len(self.options) - 1:
                self.selected_option = self.options[0]
            else:
                self.selected_option = self.options[index + 1]

    def _execute_selected_option(self):
        if self.selected_option is not None:
            self.selected_option.execute()

class Window:
    def __init__(self):
        pygame.init()
        self.open = True
        self.size = (800, 600)
        self.title = "Window"
        self.controls = []
        self.menu = Menu()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)

    def add_control(self, control):
        self.controls.append(control)

    def set_size(self, width, height):
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)

    def set_title(self, title):
        self.title = title
        pygame.display.set_caption(self.title)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        for control in self.controls:
            control.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.open:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.open = False
                # Handle other events here as needed
            self.draw()


class GUI:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element)

    def handle_event(self, event):
        for element in self.elements:
            element.handle_event(event)

    def update(self):
        for element in self.elements:
            element.update()

    def draw(self, surface):
        for element in self.elements:
            element.draw(surface)


import pygame
from pygame.locals import *


# Base GUI element class
class GUIElement:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.visible = True

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass


# Button class
class Button(GUIElement):
    def __init__(self, rect, text, callback, color=(255, 255, 255)):
        super().__init__(rect)
        self.text = text
        self.callback = callback
        self.color = color
        self.hovered = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
        elif event.type == MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

    def draw(self, surface):
        color = (255, 0, 0) if self.hovered else self.color
        pygame.draw.rect(surface, color, self.rect, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, color)
        surface.blit(text, self.rect.move(10, 10))


# Label class
class Label(GUIElement):
    def __init__(self, rect, text, color=(255, 255, 255)):
        super().__init__(rect)
        self.text = text
        self.color = color

    def draw(self, surface):
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, self.color)
        surface.blit(text, self.rect)


# TextInput class
class TextInput(GUIElement):
    def __init__(self, rect, text=''):
        super().__init__(rect)
        self.text = text
        self.active = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == KEYDOWN and self.active:
            if event.key == K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2 if self.active else 1)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, (255, 255, 255))
        surface.blit(text, self.rect.move(10, 10))


# Image class
class Image(GUIElement):
    def __init__(self, rect, image):
        super().__init__(rect)
        self.image = pygame.image.load(image)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# Panel class
class Panel(GUIElement):
    def __init__(self, rect, color=(200, 200, 200)):
        super().__init__(rect)
        self.color = color
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def remove_element(self, element):
        self.elements.remove(element)

    def handle_event(self, event):
        for element in self.elements:
            element.handle_event(event)

    def update(self):
        for element in self.elements:
            element.update()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        for element in self.elements:
            element.draw(surface)


# Slider class
class Slider(GUIElement):
    def __init__(self, rect, callback, value=0.5):
        super().__init__(rect)
        self.callback = callback
        self.value = value
        self.dragging = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == MOUSEMOTION and self.dragging:
            self.value = (event.pos[0] - self.rect.x) / self.rect.width
            self.value = min(max(self.value, 0), 1)
            self.callback(self.value)

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, (255, 255, 255), (self.rect.x, self.rect.y, self.rect.width * self.value, self.rect.height))


# DropDown class
class DropDown(GUIElement):
    def __init__(self, rect, options, callback):
        super().__init__(rect)
        self.options = options
        self.callback = callback
        self.selected_option = options[0]
        self.expanded = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
            elif self.expanded:
                for i, option in enumerate(self.options, start=1):
                    if pygame.Rect(self.rect.x, self.rect.y + 30 * i, self.rect.width, 30).collidepoint(event.pos):
                        self.selected_option = option
                        self.callback(option)
                        self.expanded = False

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(self.selected_option, True, (0, 0, 0))
        surface.blit(text, self.rect.move(10, 10))
        if self.expanded:
            for i, option in enumerate(self.options, start=1):
                pygame.draw.rect(surface, (150, 150, 150), (self.rect.x, self.rect.y + 30 * i, self.rect.width, 30))
                text = font.render(option, True, (0, 0, 0))
                surface.blit(text, (self.rect.x + 10, self.rect.y + 30 * i + 10))


# ProgressBar class
class ProgressBar(GUIElement):
    def __init__(self, rect, color=(255, 255, 255)):
        super().__init__(rect)
        self.color = color
        self.value = 0

    def set_value(self, value):
        self.value = min(max(value, 0), 1)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (0, 255, 0), (self.rect.x, self.rect.y, self.rect.width * self.value, self.rect.height))


# CheckBox class
class CheckBox(GUIElement):
    def __init__(self, rect, callback, checked=False):
        super().__init__(rect)
        self.callback = callback
        self.checked = checked

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
                self.callback(self.checked)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)
        if self.checked:
            pygame.draw.rect(surface, (255, 255, 255), self.rect.inflate(-10, -10))


# RadioButton class
class RadioButton(GUIElement):
    def __init__(self, rect, group, callback, checked=False):
        super().__init__(rect)
        self.group = group
        self.callback = callback
        self.checked = checked
        group.append(self)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                for button in self.group:
                    button.checked = False
                self.checked = True
                self.callback(self)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.rect.center, self.rect.width // 2, 2)
        if self.checked:
            pygame.draw.circle(surface, (255, 255, 255), self.rect.center, self.rect.width // 2 - 5)
 







