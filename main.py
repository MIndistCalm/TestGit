from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from DataBase import *
from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'width', '320')

from kivy.core.window import Window
from User import *

class LoginPage(Screen):
    def verify_credentials(self):
        if self.ids["login"].text == "" and self.ids["passw"].text == "":
            Window.size = (Window.width, Window.height)
            # Window.fullscreen = 'auto'
            Window.borderless = '0'
            self.manager.current = "user"
            c = User()
            c.add()
        else:
            self.manager.current = "error"


class ErrorPage(Screen):
    pass


class UserPage(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


kv_file = Builder.load_file('login.kv')


class LoginApp(App):
    def builder(self):
        return kv_file


if __name__ == '__main__':
    # LoginApp().run()
    run()
