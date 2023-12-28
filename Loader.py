Import flare 

class Loader:
    def __init__(self, engine_file, resource_file):
        self.engine_file = engine_file
        self.resource_file = resource_file

    def load_engine(self):
        # Load the game engine module
        try:
            engine_module = self._load_module_from_file(self.engine_file, "game_engine")
            return engine_module
        except FileNotFoundError:
            print(f"Error: Game engine file '{self.engine_file}' not found.")
        except Exception as e:
            print(f"Error loading game engine: {str(e)}")

        return None

    def extract_resources(self, target_directory):
        # Extract the necessary assets from the resource file
        try:
            with zipfile.ZipFile(self.resource_file, 'r') as zip_ref:
                zip_ref.extractall(target_directory)
            print("Resources extracted successfully.")
        except FileNotFoundError:
            print(f"Error: Resource file '{self.resource_file}' not found.")
        except zipfile.BadZipFile:
            print(f"Error: Invalid resource file '{self.resource_file}'. Please provide a valid zip archive.")
        except Exception as e:
            print(f"Error extracting resources: {str(e)}")

    def initialize_game(self):
        # Perform any additional initialization steps required for the game
        try:
            # Add your initialization code here
            print("Game initialized.")
        except Exception as e:
            print(f"Error initializing game: {str(e)}")

    @staticmethod
    def _load_module_from_file(file_path, module_name):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

import pygame
from pygame.locals import *
from scene import Scene
from scene_renderer import SceneRenderer

class DevEngine:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.scenes = {}
        self.current_scene = None
        self.running = False
        self.scene_renderer = None

    def add_scene(self, scene_name, scene):
        if isinstance(scene, Scene):
            self.scenes[scene_name] = scene
        else:
            print("Error: Scene must be an instance of the Scene class.")

    def set_scene(self, scene_name):
        if scene_name in self.scenes:
            self.current_scene = self.scenes[scene_name]
        else:
            print("Error: Scene '{}' not found in the engine.".format(scene_name))

    def create_scene_renderer(self):
        self.scene_renderer = SceneRenderer(self.current_scene)

    def render(self):
        if self.scene_renderer:
            self.scene_renderer.render(self.screen)

    def update(self, dt):
        if self.scene_renderer:
            self.scene_renderer.update(dt)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit_game()
            if self.scene_renderer:
                self.scene_renderer.handle_event(event)

    def quit_game(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            dt = self.clock.tick(60) / 1000.0
            self.update(dt)
            self.render()
            pygame.display.flip()

        pygame.quit()
        sys.exit()


