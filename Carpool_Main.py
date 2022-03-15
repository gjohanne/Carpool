from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class Login(Screen):
    def logger(self):
        self.root.ids.login_label.text = f'Hi'


class Home(Screen):
    pass


class CardPage(Screen):
    pass


class WindowManager(ScreenManager):
    def rail_open(self):
        if self.root.ids.rail.rail_state == "open":
            self.root.ids.rail.rail_state = "close"
        else:
            self.root.ids.rail.rail_state = "open"

    def on_start(self):
        for i in range(9):
            tile = Factory.MyTile(source="Carpool_Logo.png")
            self.root.ids.box.add_widget(tile)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('Carpool_Design.kv')

    def clear(self):
        self.root.app.ids.welcome_label.text = "Welcome"
        self.root.app.ids.user.text = ""
        self.root.app.ids.password.text = ""


MainApp().run()
