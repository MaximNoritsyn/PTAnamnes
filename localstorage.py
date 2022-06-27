from kivy.storage.jsonstore import JsonStore
import externalstorage


store_user = JsonStore('PTA_UserData.json')
store_quest = JsonStore('PTA_Questions.json')


def is_not_logged():
    return not store_user.exists('User')


def user_put(name):
    store_user.put('User', name=name)


def update_questions():
    questions = externalstorage.update_questions()
    a=1
    #store_quest