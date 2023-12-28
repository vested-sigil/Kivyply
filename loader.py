
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

