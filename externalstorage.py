from werkzeug.local import LocalProxy

from pymongo import MongoClient, DESCENDING, ASCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern
import os
import configparser
import Global

config = configparser.ConfigParser()
config.read(".ini")


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(Global, "_database", None)
    DB_URI = config['PROD']["DB_URI"]
    DB_NAME = config['PROD']["NS"]
    if db is None:

        db = Global._database = MongoClient(
        DB_URI,
        maxPoolSize=50,
        wTimeoutMS=2500
        )[DB_NAME]
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def get_questions():
    cursor = db.questions.find()
    list_question = []
    for doc in cursor:
        list_question.append(question_srtingid(doc))
    return list_question


def question_srtingid(doc):
    return {
        'text': doc.get('text'),
        'section': doc.get('section'),
        'type': doc.get('type'),
        '_id': str(doc.get('_id'))
    }

