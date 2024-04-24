import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen): # Login
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager): # Transistion btw the windows
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv
    

if __name__ == "__main__":
    MyMainApp().run()    

# The kv file needs to be call the same way that the main class (i.g. MyApp -> My.kv)
# pos_hint: {"x", "y", "top", "botton", "left", "right"}