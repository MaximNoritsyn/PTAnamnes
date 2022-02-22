from kivy.app import App
from kivy.lang import Builder
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
        # Retornar com função Builder.load_string evita erros em acentuação.
        return Builder.load_string(open('PT.kv', encoding='UTF-8').read())


if __name__ == '__main__':
    app = PTApp()
    app.run()
