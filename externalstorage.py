from werkzeug.local import LocalProxy

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from bson.objectid import ObjectId
import configparser
import Global
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

config = configparser.ConfigParser()
config.read("config.ini")


def get_db():
    db = getattr(Global, "_database", None)
    DB_URI = config['PROD']["DB_URI"]
    DB_NAME = config['PROD']["NS"]
    if db is None:

        try:
            db = Global._database = MongoClient(
                DB_URI,
                maxPoolSize=50,
                wTimeoutMS=250,
                serverSelectionTimeoutMS=300
            )[DB_NAME]

            Global._internet_connection = True
            Global._text_error = ''
        except ServerSelectionTimeoutError as err:
            db = disable_connection()

        except BaseException as error:
            db = disable_connection('An exception occurred: {}'.format(error))

    return db


# Use LocalProxy to read the global db instance with just `db`
# db = LocalProxy(get_db)
def disable_connection(text_error='No internet connection'):
    Global._database = None
    Global._internet_connection = False
    Global._text_error = text_error
    return None


def get_questions():
    list_question = []
    db = get_db()
    if db is not None:
        try:
            cursor = db.questions.find()
            for doc in cursor:
                list_question.append(question_string_id(doc))

        except ServerSelectionTimeoutError:
            disable_connection()

        except:
            disable_connection()
    return list_question


def question_string_id(doc):
    return {
        'text': doc.get('text'),
        'section': doc.get('section'),
        'type': doc.get('type'),
        '_id': str(doc.get('_id'))
    }
