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
config.read(".ini")


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
            wTimeoutMS=2500,
            serverSelectionTimeoutMS=3000
            )[DB_NAME]

            print("server version:", db.client.server_info()["version"])

        except ServerSelectionTimeoutError as err:
            # set the client and db names to 'None' and [] if exception
            db = Global._database = None

            # catch pymongo.errors.ServerSelectionTimeoutError
            print("pymongo ERROR:", err)

    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


def get_questions():
    list_question = []
    if db is not None:
        try:
            cursor = db.questions.find()
            for doc in cursor:
                list_question.append(question_srtingid(doc))
        finally:
            return []
    return list_question


def question_srtingid(doc):
    return {
        'text': doc.get('text'),
        'section': doc.get('section'),
        'type': doc.get('type'),
        '_id': str(doc.get('_id'))
    }

