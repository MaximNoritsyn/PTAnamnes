from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore

store_user = JsonStore('PTA_UserData.json')


class LoginPopup(Popup):

    def __init__(self):
        super().__init__()
        self.pop = Popup(title="Log in first", content=self, auto_dismiss=False)

    def open_login(self):
        self.pop.open()

    def pt_login(self):
        if self.ids['login'].text != '':
            store_user.put('User', name=self.ids['login'].text)
            self.pop.dismiss()
        else:
            # we need say to user
            pass


def is_not_logged():
    return not store_user.exists('User')


def show_login_window():
    content = LoginPopup()
    content.open_login()


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
