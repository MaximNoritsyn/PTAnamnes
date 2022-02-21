from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore

storeUser = JsonStore('PTA_UserData.json')


class LoginScreen(Screen):

    def pt_login(self):
        if self.ids['txt_input'].text != '':
            storeUser.put('User', name=self.ids['txt_input'].text)
        else:
            # we need say to user
            pass


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class PTApp(App):

    def build(self):

        sm = ScreenManager()
        if storeUser.exists('User'):
            sm.add_widget(MainScreen(name="main"))
            sm.add_widget(SettingsScreen(name="settings"))
            sm.switch_to(sm.screens[0])
        else:
            sm.add_widget(LoginScreen(name="login"))

        return sm


if __name__ == '__main__':
    app = PTApp()
    app.run()
