from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import localstorage
import Global

if platform == "android":
     from android.permissions import request_permissions, Permission
     request_permissions([Permission.INTERNET])


class MainScreen(Screen):
    def on_touch_move(self, touch):
        if (touch.ox - touch.x) > 100:
            PTApp.get_running_app().change_screen('setting', 'left')

    def fill_patient(self):
        layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        self.ids['questions'].clear_widgets()
        layout.add_widget(TextInputFirstNamePatient())
        layout.add_widget(TextInputLastNamePatient())
        for i in localstorage.get_questions():
            layout_question = LayoutQuestion()
            layout_question.ids['text'].text = i[1].get('text')
            if i[1].get('type') == 'num':
                answer = TextInputAnswerNum()
                layout_question.add_widget(answer)
            elif i[1].get('type') == 'string':
                answer = TextInputAnswerString()
                layout_question.add_widget(answer)
            layout.add_widget(layout_question)
        self.ids['questions'].add_widget(layout)
        self.ids['internet_connection'].size_hint_y = 0
        self.ids['internet_connection'].height = '0dp'
        self.ids['internet_connection'].text = ''
        if not Global.internet():
            self.ids['internet_connection'].size_hint_y = 1
            self.ids['internet_connection'].height = '10dp'
            self.ids['internet_connection'].text = Global.text_error()

    def on_enter(self, *args):
        self.fill_patient()


class SettingScreen(Screen):
    def on_touch_move(self, touch):
        if (touch.x - touch.ox) > 100:
            PTApp.get_running_app().change_screen('main', 'right')

    def shutdown(self):
        PTApp.get_running_app().stop()


class SubmitScreen(Screen):
    caution_label = Label(text='You need to fill name of user')

    def pt_login(self):
        if self.ids['login'].text != '':
            localstorage.user_put(self.ids['login'].text)
            PTApp.get_running_app().change_screen('main', 'left')
        else:
            if self.caution_label.parent is None:
                self.ids['place_for_caution'].add_widget(self.caution_label)


class LayoutQuestion(GridLayout):
    pass


class TextInputFirstNamePatient(TextInput):
    pass


class TextInputLastNamePatient(TextInput):
    pass


class TextInputAnswerNum(TextInput):
    pass


class TextInputAnswerString(TextInput):
    pass


Builder.load_file("PT.kv")

sm = ScreenManager()


class PTApp(App):
    def build(self):
        localstorage.update_questions()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingScreen(name='setting'))
        sm.add_widget(SubmitScreen(name='submit'))
        if localstorage.is_not_logged():
            sm.current = 'submit'
        return sm

    def change_screen(self, screen_name, screen_direction):
        sm.transition.direction = screen_direction
        sm.current = screen_name


if __name__ == '__main__':
    app = PTApp()
    app.run()
