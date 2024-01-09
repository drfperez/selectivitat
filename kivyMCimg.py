from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.uix.popup import Popup

class PreguntaApp(App):
    preguntes = [
        ("Qüestió 1: La tensió de ruptura d’un llautó és 550 MPa. Quina força axial cal per a provocar el trencament d’un eix massís de 6 mm de diàmetre?",
         ["10,37 kN", "15,55 kN", "19,80 kN", "62,20 kN"],
         "A"),
        # Altres preguntes van aquí...
        ("Pregunta 5: Què és una imatge?",
         [
             {"text": "Un conjunt de píxels", "img_path": "ruta_imatge_resposta1.jpg"},
             {"text": "Un bloc de text", "img_path": "ruta_imatge_resposta2.jpg"},
             # ... altres respostes
         ],
         "A")
    ]

    def build(self):
        root = ScrollView()

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        root.add_widget(layout)

        self.respostes_correctes = []

        for pregunta, respostes, resposta_correcta in self.preguntes:
            label_pregunta = Label(text=pregunta, size_hint_y=None, height=40)
            layout.add_widget(label_pregunta)

            toggle_buttons = []
            for resposta in respostes:
                text = resposta["text"]
                img_path = resposta["img_path"]

                toggle_button = ToggleButton(text=text, group=pregunta, size_hint_y=None, height=40)
                layout.add_widget(toggle_button)
                toggle_buttons.append(toggle_button)

            self.respostes_correctes.append(resposta_correcta)

        btn_comprovar = Button(text="Comprovar respostes", size_hint_y=None, height=40)
        btn_comprovar.bind(on_release=self.comprovar_respostes)
        layout.add_widget(btn_comprovar)

        return root

    def comprovar_respostes(self, instance):
        respostes_seleccionades = [btn.state == 'down' for btn in instance.parent.children[:-1]]
        num_correctes = sum([1 for seleccionada, correcta in zip(respostes_seleccionades, self.respostes_correctes) if seleccionada == (correcta == "A")])

        popup_content = Label(text=f'Has encertat {num_correctes} de {len(self.respostes_correctes)} preguntes.')
        popup = Popup(title='Resultat', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    PreguntaApp().run()
