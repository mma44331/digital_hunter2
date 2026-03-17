import os
from pymongo import MongoClient
from shards.logger import log_event

my_client = MongoClient(os.getenv('MONGO_URI'))
my_db = my_client['target_bank']
my_col = my_db['targets']




def get_data_find(parms):
    try:
        query, projection = parms
        res = list(my_col.find(query, projection = None).to_list())
        log_event('info','information was successfully extracted from the game')
        return res
    except ConnectionError as e:
        log_event('error',f'database connection failed: {str(e)}')
        return []

def get_data_aggr(parms):
    try:
        query = parms
        res = list(my_col.aggregate(query).to_list())
        log_event('info','information was successfully extracted from the game')
        return res
    except ConnectionError as e:
        log_event('error',f'database connection failed: {str(e)}')
        return []