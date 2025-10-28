from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

# KVファイル読み込み
Builder.load_file(os.path.join(os.path.dirname(__file__), "dl_screen.kv"))

class DlScreen(Screen):
    pass
