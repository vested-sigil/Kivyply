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


