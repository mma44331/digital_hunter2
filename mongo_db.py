import os

from pymongo import MongoClient

my_client = MongoClient(os.getenv('MONGO_URI'))
my_db = my_client['target_bank']
my_col = my_db['targets']




def get_data(query):
    try:
        res = my_col.find(query)
        return res
    except Exception as e:
        raise Exception(e)
