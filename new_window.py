from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Define print screens


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# .kv design file
kv = Builder.load_file('new_window.kv')


class MyLayout(Widget):
    pass


class SlideApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    SlideApp().run()
