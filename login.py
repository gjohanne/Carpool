from kivy.lang import Builder
from kivymd.app import MDApp
#from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    class SlidApp(MDApp):
        def build(self):
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "BlueGray"
            return Builder.load_file('login.kv')


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class SlideApp(MDApp):
    def build(self):
        return Builder.load_file('login.kv')
        #return sm

    def logger(self):
        self.root.ids.welcome_label.text = f'Hi {self.root.ids.user.text}!'

    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    # def preview(self):

#kv = Builder.load_file('login.kv')
#sm = WindowManager()

if __name__ == '__main__':
    SlideApp().run()
