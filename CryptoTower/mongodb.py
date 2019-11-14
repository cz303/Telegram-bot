from pymongo import MongoClient
import config
import json

client = MongoClient(config.exch_name_host, config.exch_host)

db = client[config.exch_name_bd]
users = db[config.exch_name_collections[0]]

def insert_user(data):
    users.insert_one(data).inserted_id

def search_in_db(message):
    chat_id = message.chat.id

    user = users.find_one({'id':chat_id})
    return user

def update_user_info_1(message):
    chat_id = message.chat.id
    user = users.find_one({'id':chat_id})

    if user['byb_coin'] < 100:
        return False
    else:
        users.update_one({'id':chat_id},{'$inc':{'tower_1':1,'byb_coin':-100}})
        return True

def update_user_info_2(message):
    chat_id = message.chat.id
    user = users.find_one({'id':chat_id})

    if user['byb_coin'] < 1000:
        return False
    else:
        users.update_one({'id':chat_id},{'$inc':{'tower_2':1,'byb_coin':-1000}})
        return True

def update_user_info_3(message):
    chat_id = message.chat.id
    user = users.find_one({'id':chat_id})

    if user['byb_coin'] < 6000:
        return False
    else:
        users.update_one({'id':chat_id},{'$inc':{'tower_3':1,'byb_coin':-6000}})
        return True

def update_state(message,menu):
    chat_id = message.chat.id
    users.update_one({'id':chat_id},{'$set':{'state_controller':menu}})

def update_comp_name(message,name):
    chat_id = message.chat.id
    users.update_one({'id':chat_id},{'$set':{'name_comp':name}})

def collect_update_coin(message):
    chat_id = message.chat.id
    user_temp = users.find_one({'id':chat_id})

    user = users.update_one({'id':chat_id},{'$inc':{'byb_coin':user_temp['oil_1']}})
    user = users.update_one({'id':chat_id},{'$inc':{'byb_coin':user_temp['oil_2']}})
    user = users.update_one({'id':chat_id},{'$inc':{'byb_coin':user_temp['oil_3']}})

    user = users.update_one({'id':chat_id},{'$set':{'oil_1':0,'oil_2':0,'oil_3':0}})

def top_5_in_db():
    users_5 = users.find({}).sort('byb_coin',-1)
    return users_5