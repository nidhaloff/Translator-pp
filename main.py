
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from deep_translator import GoogleTranslator
from bidi.algorithm import get_display
import arabic_reshaper


class MainLayout(BoxLayout):

    @staticmethod
    def get_supported_languages(auto_included=False, *args):
        supported_languages = GoogleTranslator.supported_languages
        if auto_included:
            supported_languages.insert(0, 'auto')
        return supported_languages

    @staticmethod
    def translate(source, target, text, *args):
        if not text:
            return 'provide a text to translate'

        res = GoogleTranslator(source=source, target=target).translate(payload=text)
        if target == 'arabic':
            res = get_display(arabic_reshaper.reshape(res))
        return res


class MainApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        Window.size = (500, 500)
        Window.minimum_width, Window.minimum_height = Window.size
        return MainLayout()


if __name__ == '__main__':
    MainApp().run()