import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        return FloatLayout()
    

if __name__ == "__main__":
    MyApp().run()    

# The kv file needs to be call the same way that the main class (i.g. MyApp -> My.kv)
# pos_hint: {"x", "y", "top", "botton", "left", "right"}