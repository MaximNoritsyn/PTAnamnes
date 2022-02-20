from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button

store = JsonStore('PTAnamnes_Store.json')

# Declare both screens
class LoginScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class PTApp(App):

    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(LoginScreen(name="login"))
        if store.exists('LoggedUser'):
            sm.current = 'main'
        else:
            sm.current = 'login'

        return sm


if __name__ == '__main__':
    app = PTApp()
    app.run()