#!/usr/bin/env python3
'''
Insert a document in Python
'''


def insert_school(mongo_collection, **kwargs):
    ''' insert_school '''
    name = kwargs['name']
    address = kwargs['address']
    new_doc = mongo_collection.insert_one({'name': name, 'address': address})
    return new_doc.inserted_id
