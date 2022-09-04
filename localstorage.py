from kivy.storage.jsonstore import JsonStore
import externalstorage


store_settings = JsonStore('PTA_Settings.json')
store_questions = JsonStore('PTA_Questions.json')


def is_not_logged():
    return not store_settings.exists('User')


def user_put(name):
    store_settings.put('User', name=name)


def update_questions():
    questions = externalstorage.get_questions()
    if questions is not None:
        for x in store_questions.keys():
            store_questions.delete(x)
        for doc in questions:
            store_questions[doc.get('_id')] = doc


def get_questions():
    update_questions()
    return list(store_questions.find())
