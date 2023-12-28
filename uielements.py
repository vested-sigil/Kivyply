import pygame
from pygame.locals import *


class UIElement:
    def __init__(self, rect, visible=True, resizable=False):
        self.rect = pygame.Rect(rect)
        self.visible = visible
        self.resizable = resizable

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass

    def contains(self, point):
        return self.rect.collidepoint(point)

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def resize(self, width, height):
        if self.resizable:
            self.rect.width = width
            self.rect.height = height


class Button(UIElement):
    def __init__(self, rect, text, callback, color=(255, 255, 255), resizable=False):
        super().__init__(rect, resizable=resizable)
        self.text = text
        self.callback = callback
        self.color = color
        self.hovered = False

    def handle_event(self, event):
        if event.type == FINGERDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
        elif event.type == FINGERMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

    def draw(self, surface):
        color = (255, 0, 0) if self.hovered else self.color
        pygame.draw.rect(surface, color, self.rect, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, color)
        surface.blit(text, self.rect.move(10, 10))


class InspectButton(Button):
    def __init__(self, rect, target_element, color=(255, 255, 255), resizable=False):
        super().__init__(rect, "Inspect", self.inspect_element, color=color, resizable=resizable)
        self.target_element = target_element

    def inspect_element(self):
        element_props = vars(self.target_element)
        for prop, value in element_props.items():
            print(f"{prop}: {value}")


class Window:
    def __init__(self):
        pygame.init()
        self.open = True
        self.size = (800, 600)
        self.title = "Window"
        self.controls = []
        self.ui_manager = UIManager()
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
        self.screen.fill((0, 0,
