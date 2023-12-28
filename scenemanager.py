 import pygame

class InputManager:
    def __init__(self):
        self.keys_pressed = set()

    def handle_input(self):
        self.keys_pressed.clear()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keys_pressed.add(event.key)

    def is_key_pressed(self, key):
        return key in self.keys_pressed


class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def present(self):
        pygame.display.flip()


class SceneManager:
    def __init__(self):
        self.current_scene = None

    def set_scene(self, scene):
        self.current_scene = scene
        self.current_scene.on_enter()

    def switch_scene(self, scene):
        if self.current_scene:
            self.current_scene.on_exit()
        self.set_scene(scene)

    def handle_input(self):
        if self.current_scene:
            self.current_scene.handle_input()

    def update(self, dt):
        if self.current_scene:
            self.current_scene.update(dt)

    def render(self, renderer):
        if self.current_scene:
            self.current_scene.render(renderer)
```

**game_objects.py**
```python
import pygame

class Game:
    def __init__(self):
        pygame.init()

class Scene:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def handle_input(self):
        pass

    def update(self, dt):
        pass

    def render(self, renderer):
        pass

class MainMenuScene(Scene):
    def on_enter(self):
        print("Entered Main Menu Scene")

    def on_exit(self):
        print("Exited Main Menu Scene")

    def handle_input(self):
        pass

    def update(self, dt):
        pass

    def render(self, renderer):
        pass

if __name__ == '__main__':
    # Create game systems
    input_manager = InputManager()
    renderer = Renderer()
    scene_manager = SceneManager()

    # Set up the initial scene
    main_menu_scene = MainMenuScene(scene_manager)
    scene_manager.set_scene(main_menu_scene)

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        # Handle input
        scene_manager.handle_input()

        # Update current scene
        scene_manager.update(dt)

        # Render current scene
        renderer.clear()
        scene_manager.render(renderer)
        renderer.present()

        # Check for quit event
        for event in pygame
