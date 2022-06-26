from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window

store_user = JsonStore('PTA_UserData.json')

def is_not_logged():
    return not store_user.exists('User')


class MainScreen(Screen):
    def on_touch_move(self, touch):
        if (touch.ox - touch.x) > 100:
            print(touch.ox - touch.x)
            PTApp.get_running_app().change_screen('setting', 'left')


class SettingScreen(Screen):
    def on_touch_move(self, touch):
        if (touch.x - touch.ox) > 100:
            PTApp.get_running_app().change_screen('main', 'right')

    def shutdown(self):
        PTApp.get_running_app().stop()


class SubmitScreen(Screen):
    coutionLabel = Label(text='You need to fill name of user')

    def pt_login(self):
        if self.ids['login'].text != '':
            store_user.put('User', name=self.ids['login'].text)
            PTApp.get_running_app().change_screen('main', 'left')
        else:
            if self.coutionLabel.parent is None:
                self.ids['placeforcoution'].add_widget(self.coutionLabel)


Builder.load_file("PT.kv")

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SettingScreen(name='setting'))
sm.add_widget(SubmitScreen(name='submit'))


class PTApp(App):
    def build(self):
        if is_not_logged():
            sm.current = 'submit'
        return sm

    def change_screen(self, screen_name, screen_direction):
        sm.transition.direction = screen_direction
        sm.current = screen_name


if __name__ == '__main__':
    app = PTApp()
    app.run()
