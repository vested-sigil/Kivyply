from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.properties import ObjectProperty
from functools import partial
from kivy.graphics import Color, Rectangle
from projectmanager import ProjectManagerUI
from kivy.core.window import Window

# Ensure the right imports for custom widgets
# from customwidgets import CustomWidget1, CustomWidget2

class DrawingCanvas(BoxLayout):
    selected_widget = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(DrawingCanvas, self).__init__(**kwargs)
        self.current_widget = None
        self.widgets = []
        self.widget_classes = {
            'Label': Label,
            'Button': Button,
            'TextInput': TextInput,
            'CheckBox': CheckBox,
            'Slider': Slider,
            'Switch': Switch,
            'Image': Image,
            'VideoPlayer': VideoPlayer,
            'ModalView': ModalView,
            'Popup': Popup,
            'Spinner': Spinner,
            'ProgressBar': ProgressBar,
            'FileChooserListView': FileChooserListView,
            'Scatter': Scatter,
            'FloatLayout': FloatLayout,
            'AnchorLayout': AnchorLayout,
            'GridLayout': GridLayout,
            'StackLayout': StackLayout,
            'ScrollView': ScrollView,
            # 'CustomWidget1': CustomWidget1,
            # 'CustomWidget2': CustomWidget2,
        }

    def set_current_widget(self, widget_name):
        self.current_widget = self.widget_classes.get(widget_name)

    def on_touch_down(self, touch):
        if self.current_widget:
            widget = self.current_widget(size_hint=(None, None), size=(100, 100), pos=touch.pos)
            self.add_widget(widget)
            self.widgets.append(widget)
        return super(DrawingCanvas, self).on_touch_down(touch)

class ToolboxTabbedPanel(TabbedPanel):
    def __init__(self, drawing_canvas, **kwargs):
        super(ToolboxTabbedPanel, self).__init__(**kwargs)
        self.do_default_tab = False
        self.drawing_canvas = drawing_canvas
        self.add_widget(self.create_tab('Widgets', [
            'Label', 'Button', 'TextInput', 'CheckBox', 'Slider', 'Switch',
            'Image', 'VideoPlayer', 'ModalView', 'Popup', 'Spinner',
            'ProgressBar', 'FileChooserListView', 'Scatter', 'FloatLayout',
            'AnchorLayout', 'GridLayout', 'StackLayout', 'ScrollView',
            # 'CustomWidget1', 'CustomWidget2',
        ]))

    def create_tab(self, title, widgets):
        tab = TabbedPanelItem(text=title)
        layout = BoxLayout(orientation='vertical', size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for widget_name in widgets:
            button = Button(text=widget_name, size_hint_y=None, height=40)
            button.bind(on_release=partial(self.on_widget_select, widget_name))
            layout.add_widget(button)
        return tab

    def on_widget_select(self, widget_name, *args):
        self.drawing_canvas.set_current_widget(widget_name)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Define the drawing canvas first
        self.drawing_canvas = DrawingCanvas(size_hint=(1, 0.7))
        
        # Now define the toolbox, passing in the drawing canvas
        self.toolbox = ToolboxTabbedPanel(drawing_canvas=self.drawing_canvas, size_hint=(1, None), height=Window.height * 0.1)
        
        # Define the project manager UI at the bottom
        self.project_manager_ui = ProjectManagerUI(size_hint=(1, 0.2))

        # Add the widgets to the screen in the correct order
        self.add_widget(self.toolbox)
        self.add_widget(self.drawing_canvas)
        self.add_widget(self.project_manager_ui)

class LayoutDesignerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    LayoutDesignerApp().run()
