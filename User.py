from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import Login

from connected import Connected


class User(Screen):
    def add(self):
        layout = BoxLayout(padding=10)

        for i in range(5):
            btn = Button(text="Button #%s" % (i + 1))

            layout.add_widget(btn)
        return layout