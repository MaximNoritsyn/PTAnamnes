from kivy.storage.jsonstore import JsonStore
import externalstorage
import Global


store_user = JsonStore('PTA_UserData.json')
store_quest = JsonStore('PTA_Questions.json')


def is_not_logged():
    return not store_user.exists('User')


def user_put(name):
    store_user.put('User', name=name)


def update_questions():
    questions = externalstorage.get_questions()
    for doc in questions:
        store_quest[doc.get('_id')] = doc
