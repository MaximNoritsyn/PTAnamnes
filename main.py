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
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(MainScreen(name="main"))
        sm.current = 'login'
        return sm


if __name__ == '__main__':
    app = PTApp()
    app.run()