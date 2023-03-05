# main.py

__version__ = '0.1'

# ...ваш код

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World!')

TestApp().run()
