import os
import pymongo
from fastapi import FastAPI

# create a MongoClient to connect to the DDBMS (Distributed Database Management System):

MONGO_URL = os.environ["DATABASE_URL"]
client = pymongo.MongoClient(MONGO_URL)

dbname = os.environ['DATABASE_NAME']
db = client[dbname]  # connect to a specific database name

class Queries:
    @property
    def collection(self):
        db = client[self.DB_NAME]
        return db[self.COLLECTION]
