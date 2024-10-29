from kaki.app import App
# from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager

from kivy.factory import Factory

import os

Window.size = (500, 900)
# Window.clearcolor = (1, 1, 1, 1)

# kv = Builder.load_file("my.kv")


class Live(App, MDApp):

    # CLASSES = {
    #     "ScreenUI": "live.screen_ui"
    # }

    # AUTORELOADER_PATHS = [
    #     (".", {"recursive": True}),
    # ]

    KV_FILES = [
        os.path.join(os.getcwd(), 'layout.kv'),
        # os.path.join(os.getcwd(), 'screen_manager.kv'),
        # os.path.join(os.getcwd(), 'login_screen.kv'),
        # os.path.join(os.getcwd(), 'user_screen.kv'),
        # os.path.join(os.getcwd(), 'third.kv'),
    ]

    CLASSES = {
        "UI": "main",
        # "nombre_clase": "nombre_archivo_kivy"
        # "Manager": "screen_manager",
        # "LoginScreen": "login_screen",
        # "UserScreen": "login_screen",
        # "ThirdScreen": "third",
    }

    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]


    def build_app(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = 'Blue'
        return Factory.UI()
    
    
    # def navigation_draw(self):
    #     print("navbar")
    
Live().run()    

# The kv file needs to be call the same way that the main class (i.g. MyApp -> My.kv)
# pos_hint: {"x", "y", "top", "botton", "left", "right"}