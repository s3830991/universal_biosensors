import pymongo

import csv_to_json

'''
 input csv function
'''


def input_csv():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db_name = client["test"]
    mycol = db_name["test"]

    mylist = csv_to_json.trans_csv()

    x = mycol.insert_many(mylist)
