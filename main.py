from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.storage.jsonstore import JsonStore
from kivy.core.window import Window

store_user = JsonStore('PTA_UserData.json')


def is_not_logged():
    return not store_user.exists('User')


class MainScreen(Screen):
    pass


class SubmitScreen(Screen):
    def pt_login(self):
        if self.ids['login'].text != '':
            store_user.put('User', name=self.ids['login'].text)
            sm.current = 'main'
        else:
            # we need say to user
            pass


Builder.load_file("PT.kv")


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SubmitScreen(name='submit'))


class PTApp(App):
    def build(self):
        if is_not_logged():
            sm.current = 'submit'
        return sm

if __name__ == '__main__':
    app = PTApp()
    app.run()