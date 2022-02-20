from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

# Declare both screens
class LoginScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class PTApp(App):
    def build(self):
        sc = ScreenManager()
        sc.add_widget(LoginScreen(name="login"))
        sc.add_widget(MainScreen(name="main"))
        return sc


if __name__ == '__main__':
    app = PTApp()
    app.run()