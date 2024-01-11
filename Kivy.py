from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.core.window import Window

class QuizApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # ScrollView for questions
        scroll_view = ScrollView()

        # GridLayout for questions and options
        grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Sample questions and answers
        sample_questions = [
            ("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], "a"),
            ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "b"),
            ("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], "b"),
        ]

        # Adding questions and options
        for i, (question, options, correct_answer) in enumerate(sample_questions):
            question_label = Label(text=question, size_hint_y=None, height=dp(60))
            grid_layout.add_widget(question_label)

            for j, option in enumerate(options):
                option_button = ToggleButton(text=option, group=f'question_{i}')
                grid_layout.add_widget(option_button)

            grid_layout.add_widget(Label(text=f"Resposta {i + 1}", size_hint_y=None, height=dp(30)))

        scroll_view.add_widget(grid_layout)

        # Button to check answers
        btn_comprovar = Button(text="Comprovar respostes", on_press=self.check_answers)
        grid_layout.add_widget(btn_comprovar)

        # Popup to display the result
        self.result_popup = Popup(title='Resultat', size_hint=(None, None), size=(400, 200))

        scroll_view.size_hint_y = None
        scroll_view.height = Window.height - btn_comprovar.height
        root.add_widget(scroll_view)

        return root

    def check_answers(self, instance):
        # Sample logic to check answers
        correct_answers = ["a", "b", "b"]  # Replace with the correct answers from your questions

        # Get selected answers
        selected_answers = []
        for i in range(len(sample_questions)):
            question_group = f'question_{i}'
            selected_answer = [button.text for button in ToggleButton.get_widgets(group=question_group) if button.state == 'down']
            selected_answers.append(selected_answer[0] if selected_answer else None)

        # Compare selected answers with correct answers
        for i, (selected, correct) in enumerate(zip(selected_answers, correct_answers)):
            question_group = f'question_{i}'
            if selected == correct:
                color = 'green'
            else:
                color = 'red'

            # Update button color
            for button in ToggleButton.get_widgets(group=question_group):
                button.background_color = (0, 1, 0, 0) if color == 'green' else (1, 0, 0, 1)

        # Display result in the popup
        num_correct = sum([1 for selected, correct in zip(selected_answers, correct_answers) if selected == correct])
        result_text = f"You got {num_correct} out of {len(sample_questions)} questions correct."
        self.result_popup.content = Label(text=result_text)
        self.result_popup.open()

if __name__ == '__main__':
    QuizApp().run()
