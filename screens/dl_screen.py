from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

# KVファイル読み込み
Builder.load_file(os.path.join(os.path.dirname(__file__), "dl_screen.kv"))

class DlScreen(Screen):
    def on_pre_enter(self, *args):
        """画面が表示される直前（アニメーション前）に呼ばれる"""
        print("DlScreen: on_pre_enter")
        self.init_data()  # ← 初期処理を呼び出す

    def on_enter(self, *args):
        """画面が完全に表示されたあとに呼ばれる"""
        print("DlScreen: on_enter")

    def init_data(self):
        """初期データの設定など"""
        # ここに画面初期化処理を書く

