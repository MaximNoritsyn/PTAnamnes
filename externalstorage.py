from werkzeug.local import LocalProxy

from pymongo import MongoClient, DESCENDING, ASCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import ServerSelectionTimeoutError, DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern
import os
import configparser
import Global
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

config = configparser.ConfigParser()
config.read("config.ini")


def get_db():
    """
    Configuration method to return db instance
    """
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
        except ServerSelectionTimeoutError as err:
            # set the client and db names to 'None' and [] if exception
            db = disable_connection()

        except:
            db = disable_connection()

    return db


# Use LocalProxy to read the global db instance with just `db`
# db = LocalProxy(get_db)
def disable_connection():
    Global._database = None
    Global._internet_connection = False
    return None


def get_questions():
    list_question = []
    db = get_db()
    if db is not None:
        try:
            cursor = db.questions.find()
            for doc in cursor:
                list_question.append(question_srtingid(doc))

        except ServerSelectionTimeoutError:
            disable_connection()

        except:
            disable_connection()
    return list_question


def question_srtingid(doc):
    return {
        'text': doc.get('text'),
        'section': doc.get('section'),
        'type': doc.get('type'),
        '_id': str(doc.get('_id'))
    }
