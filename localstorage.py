from kivy.storage.jsonstore import JsonStore
import externalstorage
import Global


store_settings = JsonStore('PTA_Settings.json')
store_questions = JsonStore('PTA_Questions.json')


def is_not_logged():
    return not store_settings.exists('User')


def user_put(name):
    store_settings.put('User', name=name)


def update_questions():
    questions = externalstorage.get_questions()
    for x in store_questions.keys():
        store_questions.delete(x)
    for doc in questions:
        store_questions[doc.get('_id')] = doc
