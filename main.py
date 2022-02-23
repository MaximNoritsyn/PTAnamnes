from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore

store_user = JsonStore('PTA_UserData.json')


class LoginPopup(Popup):

    def pt_login(self):
        if self.ids['login'].text != '':
            store_user.put('User', name=self.ids['login'].text)
            self.dismiss()
        else:
            # we need say to user
            pass


def show_login_window():
    content = LoginPopup()

    window = Popup(title="Log in first", content=content, auto_dismiss=False)
    window.open()


def is_not_logged():
    return not store_user.exists('User')


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        if is_not_logged():
            show_login_window()


class SettingsScreen(Screen):
    pass


class PTApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    app = PTApp()
    app.run()
