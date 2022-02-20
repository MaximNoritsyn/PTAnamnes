from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore

store = JsonStore('PTAnamnes_Store.json')


# Declare both screens
class LoginScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class PTApp(App):

    def build(self):

        sm = ScreenManager()
        if store.exists('LoggedUser'):
            sm.add_widget(MainScreen(name="main"))
            sm.add_widget(SettingsScreen(name="settings"))
            sm.switch_to(sm.screens[0])
        else:
            sm.add_widget(LoginScreen(name="login"))

        return sm


if __name__ == '__main__':
    app = PTApp()
    app.run()
