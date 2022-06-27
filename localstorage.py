from kivy.storage.jsonstore import JsonStore


store_user = JsonStore('PTA_UserData.json')


def is_not_logged():
    return not store_user.exists('User')


def user_put(name):
    store_user.put('User', name=name)
