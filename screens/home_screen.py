from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "home_screen.kv"))

class HomeScreen(Screen):
    pass
