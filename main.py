import kivy
# from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


Window.size = (350, 580)
# Window.clearcolor = (1, 1, 1, 1)


class LoginWindow(Screen): # Login
    pass


class MainWindow(Screen): # Login
    pass


class DescargarWindow(Screen):
    pass


class AplicarWindow(Screen):
    pass


class GenerarWindow(Screen):
    pass


class CerrarWindow(Screen):
    pass


class WindowManager(ScreenManager): # Transistion btw the windows
    pass


# kv = Builder.load_file("my.kv")


class MyMainApp(MDApp):
    title = 'Encuestas Digitales'

    def build(self):
        # self.root_widget = kv
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = 'Blue'
        return Builder.load_file("my.kv")
    
    
    def navigation_draw(self):
        print("navbar")
    

if __name__ == "__main__":
    MyMainApp().run()    

# The kv file needs to be call the same way that the main class (i.g. MyApp -> My.kv)
# pos_hint: {"x", "y", "top", "botton", "left", "right"}