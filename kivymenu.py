import subprocess
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

class SelectivitatApp(App):
    def execute_problem_1(self, *args):
        subprocess.Popen(['python', 'problema_1.py'])

    def execute_problem_2(self, *args):
        subprocess.Popen(['python', 'problema_2.py'])

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Càrrega del logo i redimensionament
        logo_image = Image(source="logo.png")  # Reemplaça "logo.png" amb la ruta real del teu logo
        logo_image.size_hint = (None, None)
        logo_image.size = (75, 75)
        layout.add_widget(logo_image)

        # Text justificat amb mida de font 18
        text = "Tria els problemes de Tecnologia i Enginyeria corresponents a les proves d'accés \na la Universitat de les convocatòries de Juny i Setembre de 2009"
        text_label = Label(text=text, font_size=18, halign='left', valign='top', size_hint=(1, None))
        layout.add_widget(text_label)

        # Crea el menú desplegable
        problem_menu = DropDown()

        btn_problem = Button(text='Escull un problema', size_hint=(None, None), size=(200, 50))
        btn_problem.bind(on_release=problem_menu.open)
        layout.add_widget(btn_problem)

        problem_menu.add_widget(Button(text='Problema 1', size_hint_y=None, height=44))
        problem_menu.add_widget(Button(text='Problema 2', size_hint_y=None, height=44))
        # Afegeix opcions per als altres problemes aquí

        return layout

if __name__ == '__main__':
    SelectivitatApp().run()
