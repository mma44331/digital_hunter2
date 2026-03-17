import os
from shards.logger import log_event
from pymongo import MongoClient

my_client = MongoClient(os.getenv('MONGO_URI'))
my_db = my_client['target_bank']
my_col = my_db['targets']




def get_data(query):
    try:
        res = my_col.find(query)
        log_event('info','information was successfully extracted from the game')
        return res
    except ConnectionError as e:
        log_event('error',f'database connection failed: {str(e)}')
