import pygame
from pygame.locals import *
from gui import GUI, Button, Label, Panel
from asset_manager import AssetManager

class IDE:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.gui = GUI()
        self.asset_manager = AssetManager()
        self.running = False

        # Create Panels
        self.workzone_panel = Panel((0, 0, screen_width, screen_height), (200, 200, 200))
        self.assets_panel = Panel((0, 0, screen_width, screen_height), (220, 220, 220))
        self.property_inspector_panel = Panel((0, 0, screen_width, screen_height), (240, 240, 240))
        self.cli_panel = Panel((0, 0, screen_width, screen_height), (230, 230, 230))
        self.toolbox_panel = Panel((0, 0, screen_width, screen_height), (210, 210, 210))
        self.status_bar_panel = Panel((0, 0, screen_width, screen_height), (220, 220, 220))

        # Add Elements to Panels
        self.workzone_panel.add_element(WorkZone())
        self.assets_panel.add_element(AssetsPanel())
        self.property_inspector_panel.add_element(PropertyInspector())
        self.cli_panel.add_element(CLI())
        self.toolbox_panel.add_element(Toolbox())
        self.status_bar_panel.add_element(Label((0, 0, screen_width, screen_height), "Ready"))

        # Arrange Panels in the IDE Window
        self.gui.add_element(self.workzone_panel)
        self.gui.add_element(self.assets_panel)
        self.gui.add_element(self.property_inspector_panel)
        self.gui.add_element(self.cli_panel)
        self.gui.add_element(self.toolbox_panel)
        self.gui.add_element(self.status_bar_panel)

    def add_button(self, rect, text, callback):
        button = Button(rect, text, callback)
        self.gui.add_element(button)

    def add_label(self, rect, text):
        label = Label(rect, text)
        self.gui.add_element(label)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_ide()
            self.gui.handle_event(event)

    def update(self, dt):
        self.gui.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.gui.draw(self.screen)
        pygame.display.flip()

    def quit_ide(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()
        sys.exit()


class IDE:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.gui = GUI()
        self.asset_manager = AssetManager()
        self.running = False
        
        # Create menus
        self.file_menu = Menu("File")
        self.edit_menu = Menu("Edit")
        self.view_menu = Menu("View")
        
        # Add menu items
        self.file_menu.add_item(MenuItem("New", self.new_file))
        self.file_menu.add_item(MenuItem("Open", self.open_file))
        self.file_menu.add_item(MenuItem("Save", self.save_file))
        self.file_menu.add_item(MenuItem("Exit", self.quit_ide))
        
        self.edit_menu.add_item(MenuItem("Cut", self.cut))
        self.edit_menu.add_item(MenuItem("Copy", self.copy))
        self.edit_menu.add_item(MenuItem("Paste", self.paste))
        
        self.view_menu.add_item(MenuItem("Toggle Grid", self.toggle_grid))
        self.view_menu.add_item(MenuItem("Zoom In", self.zoom_in))
        self.view_menu.add_item(MenuItem("Zoom Out", self.zoom_out))
        
        # Create menu bar
        self.menu_bar = MenuBar()
        self.menu_bar.add_menu(self.file_menu)
        self.menu_bar.add_menu(self.edit_menu)
        self.menu_bar.add_menu(self.view_menu)
        
        # Add menu bar to GUI
        self.gui.add_element(self.menu_bar)

    # Rest of the IDE class implementation...
# Import necessary modules
import pygame
from pygame.locals import *
from uielements import *
from layoutbuilder import *

# Create the IDE window
window = Window()
window.set_size(800, 600)
window.set_title("Game Development IDE")

# Layout Configuration
layout_configuration = {
    "menu_layout": layouts["menu_horizontal"],
    "workzone_layout": layouts["panel_horizontal"],
    "assets_panel_layout": layouts["panel_vertical"],
    "property_inspector_layout": layouts["panel_vertical"],
    "cli_layout": layouts["panel_horizontal"],
    "toolbox_layout": layouts["panel_vertical"],
    "status_bar_layout": layouts["menu_horizontal"],
}

# Create Panels
menu_panel = Panel(layout_configuration["menu_layout"])
workzone_panel = Panel(layout_configuration["workzone_layout"])
assets_panel = Panel(layout_configuration["assets_panel_layout"])
property_inspector_panel = Panel(layout_configuration["property_inspector_layout"])
cli_panel = Panel(layout_configuration["cli_layout"])
toolbox_panel = Panel(layout_configuration["toolbox_layout"])
status_bar_panel = Panel(layout_configuration["status_bar_layout"])

# Add Elements to Panels
menu_panel.add_element(Menu())
workzone_panel.add_element(WorkZone())
assets_panel.add_element(AssetsPanel())
property_inspector_panel.add_element(PropertyInspector())
cli_panel.add_element(CLI())
toolbox_panel.add_element(Toolbox())
status_bar_panel.add_element(StatusBar())

# Arrange Panels in the IDE Window
window.add_control(menu_panel)
window.add_control(workzone_panel)
window.add_control(assets_panel)
window.add_control(property_inspector_panel)
window.add_control(cli_panel)
window.add_control(toolbox_panel)
window.add_control(status_bar_panel)

# Run the IDE
window.run()
def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_ide()
            self.gui.handle_event(event)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.gui.draw(self.screen)
        pygame.display.flip()

class IDE:
    def __init__(self, screen_width, screen_height):
        # ...
        self.tabs = []

    def add_tab(self, tab_name):
        # Create a new tab and add it to the GUI
        tab = Tab(tab_name)
        self.gui.add_element(tab)
        self.tabs.append(tab)

    def switch_tab(self, tab_index):
        # Switch to the specified tab index
        self.gui.switch_tab(tab_index)

class IDE:
    def __init__(self, screen_width, screen_height):
        # ...
        self.tabs = []

    def add_tab(self, tab_name):
        # Create a new tab and add it to the GUI
        tab = Tab(tab_name)
        self.gui.add_element(tab)
        self.tabs.append(tab)

    def switch_tab(self, tab_index):
        # Switch to the specified tab index
        self.gui.switch_tab(tab_index)



    def run(self):
        self.running = True
        while self.running:
            dt = self.clock.tick(60) / 1000.0
            self.handle_events()
            self.update(dt)
            self.render()

        pygame.quit()
        sys.exit()
