#!/usr/bin/python3
from pymongo import MongoClient
import config
import json
import os

client = MongoClient(config.exch_name_host, config.exch_host)

db = client[config.exch_name_bd]
users = db[config.exch_name_collections[0]]

def user_update_coin():
    all_users = users.find()
    for i in range(users.count()):
        users.update_one({'id':all_users[i]['id']},{'$inc':{'oil_1':(16*all_users[i]['tower_1']),'oil_2':(184*all_users[i]['tower_2']),'oil_3':(1249*all_users[i]['tower_3'])}})

if __name__ == "__main__":
    user_update_coin()