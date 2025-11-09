from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
import mylib
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
#fonts
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles
import os 
from kivy.resources import resource_add_path
# 別ファイルの画面をインポート
from screens import DlScreen, HomeScreen
#デバッグ用
debugFlg = 1
class TestApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # インスタンス変数の初期化
        self.dialog = None

        
    def build(self):
        self.setFont()
        return self.commonBuild()
        #return Builder.load_string('BoxLayout:')

    def on_start(self):
        if debugFlg == 1:
            self.changeScreen("home_screen")
        else:
            self.show_login_dialog(callback=self.after_login)
        
    def show_login_dialog(self,callback):
        """ログインダイアログを表示"""
        if not self.dialog:
            self.username_field = MDTextField(
                hint_text="ID",
                required=True,
            )
            self.password_field = MDTextField(
                hint_text="PASSWORD",
                password=True,
                required=True,
            )

            self.dialog = MDDialog(
                title="LOGIN",
                type="custom",
                content_cls=Builder.load_string('''
BoxLayout:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: self.minimum_height

    MDTextField:
        id: username
        hint_text: "ID"
    MDTextField:
        id: password
        hint_text: "PASSWORD"
        password: True
'''),
                buttons=[
                    MDFlatButton(
                        text="LOGIN",
                        on_release=lambda x: self._login_pressed
                        (self.dialog.content_cls.ids.username.text,
                        self.dialog.content_cls.ids.password.text,
                        callback)
                    ),
                    MDFlatButton(
                        text="CANCEL",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()
        
    def _login_pressed(self, username, password, callback):
        """ログイン押下時に呼ばれる"""
        status = mylib.login_action(username, password)
        
        # 呼び出し元の関数に結果を返す
        callback(status)
    
    def after_login(self, response):
        """ログイン結果を受け取る"""
        status = response["status_code"]
        if status == 200:
            self.dialog.dismiss()
            self.changeScreen("home_screen")
        else:
            from kivymd.toast import toast
            toast("failed")
            
    def changeScreen(self, screen_name):
        self.sm.current = screen_name
        self.nav_drawer.set_state("close")
        
    # def changeScreen(self,screen_name):
    #     self.root.current = screen_name
    def show_datepicker(self, field):
        """開始日/終了日用の日付ピッカーを開く"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=lambda instance, value, date_range: self.set_date(field, value))
        date_dialog.open()

    def set_date(self, field, date_value):
        """選択された日付を格納"""
        if field == "start":
            self.start_date = date_value
        elif field == "end":
            self.end_date = date_value
        print(f"{field}日: {date_value}")  # デバッグ用

    def download_data(self):
        """開始日・終了日を使ったダウンロード処理"""
        print(f"ダウンロード期間: {self.start_date} ～ {self.end_date}")
        # ここで実際のダウンロード処理を呼ぶ
        
    def commonBuild(self):
        # Navigation Layout
        self.nav_layout = MDNavigationLayout()
        
         # ScreenManagerの設定
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home_screen"))
        self.sm.add_widget(DlScreen(name="dl_screen"))
        
         # Navigation Drawerの設定
        self.nav_drawer = MDNavigationDrawer()
        drawer_box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        
          # Homeボタン
        home_item = OneLineIconListItem(text="Home", on_release=lambda x: self.changeScreen("home_screen"))
        home_item.add_widget(IconLeftWidget(icon="home"))
        drawer_box.add_widget(home_item)
        
          # DLボタン
        dl_item = OneLineIconListItem(text="DL", on_release=lambda x: self.changeScreen("dl_screen"))
        dl_item.add_widget(IconLeftWidget(icon="download"))
        drawer_box.add_widget(dl_item)
        
        self.nav_drawer.add_widget(drawer_box)

        # Layout構成
        self.nav_layout.add_widget(self.sm)
        self.nav_layout.add_widget(self.nav_drawer)

        return self.nav_layout
    
    def setFont(self):
        fontPath = os.path.join(os.path.dirname(__file__),"assets","fonts","BIZUDGothic-Regular.ttf")
        print(fontPath)
        print("Font path:", fontPath)
        print("File exists:", os.path.exists(fontPath))

        # フォントパスをKivyに登録
        #resource_add_path(os.path.dirname(fontPath))

        LabelBase.register(name="Roboto",fn_regular=fontPath)
        # theme_font_styles.append("BIZUDGothic")
        # self.theme_cls.font_styles["BIZUDGothic"] = [
        #     "BIZUDGothic",
        #     "BIZUDGothic",
        #     16,
        #     None
        # ]
        #self.theme_cls.font_style = "BIZUDGothic"

TestApp().run()
