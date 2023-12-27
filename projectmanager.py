import json
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView

# Project Manager Class
class ProjectManager:
    def __init__(self, project_dir='projects/'):
        self.project_dir = project_dir
        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)

    def create_project(self, project_name, content):
        project_path = os.path.join(self.project_dir, project_name + '.json')
        with open(project_path, 'w') as file:
            json.dump(content, file)

    def save_project(self, project_name, content):
        project_path = os.path.join(self.project_dir, project_name + '.json')
        with open(project_path, 'w') as file:
            json.dump(content, file)

    def load_project(self, project_name):
        project_path = os.path.join(self.project_dir, project_name + '.json')
        if os.path.exists(project_path):
            with open(project_path, 'r') as file:
                return json.load(file)
        else:
            return None

# Project Manager UI Class
class ProjectManagerUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.project_manager = ProjectManager()
        self.project_content_input = TextInput()

        self.file_chooser = FileChooserListView(path=self.project_manager.project_dir, filters=['*.json'])
        self.add_widget(self.file_chooser)
        self.add_widget(self.project_content_input)

        button_layout = BoxLayout(size_hint_y=None, height=50)
        load_button = Button(text='Load Project', on_press=self.load_project)
        save_button = Button(text='Save Project', on_press=self.save_project)
        new_button = Button(text='New Project', on_press=self.new_project)
        delete_button = Button(text='Delete Project', on_press=self.delete_project)
        duplicate_button = Button(text='Duplicate Project', on_press=self.duplicate_project)

        button_layout.add_widget(load_button)
        button_layout.add_widget(save_button)
        button_layout.add_widget(new_button)
        button_layout.add_widget(delete_button)
        button_layout.add_widget(duplicate_button)

        self.add_widget(button_layout)

    def load_project(self, instance):
        selected = self.file_chooser.selection
        if selected:
            project_path = selected[0]
            with open(project_path, 'r') as file:
                content = json.load(file)
                self.project_content_input.text = json.dumps(content, indent=4)

    def save_project(self, instance):
        selected = self.file_chooser.selection
        if selected:
            project_path = selected[0]
            content = json.loads(self.project_content_input.text)
            with open(project_path, 'w') as file:
                json.dump(content, file)

    def new_project(self, instance):
        new_project_name = "new_project.json"
        project_path = os.path.join(self.project_manager.project_dir, new_project_name)
        with open(project_path, 'w') as file:
            json.dump({}, file)

    def delete_project(self, instance):
        selected = self.file_chooser.selection
        if selected:
            project_path = selected[0]
            os.remove(project_path)
            self.file_chooser._update_files()

    def duplicate_project(self, instance):
        selected = self.file_chooser.selection
        if selected:
            original_project_path = selected[0]
            duplicate_project_path = original_project_path.replace('.json', '_copy.json')
            with open(original_project_path, 'r') as original_file:
                content = json.load(original_file)
            with open(duplicate_project_path, 'w') as duplicate_file:
                json.dump(content, duplicate_file)
