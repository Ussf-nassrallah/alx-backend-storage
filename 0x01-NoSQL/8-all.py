#!/usr/bin/env python3
'''
List all documents in Python
'''


def list_all(mongo_collection):
    ''' list_all return docs from colls '''
    docs = []

    for document in mongo_collection.find():
        docs.append(document)

    return docs
