#!/usr/bin/env python3
'''
11. Where can I learn Python?
'''


def schools_by_topic(mongo_collection, topic):
    ''' schools_by_topic '''
    docs = []

    result = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }

    for document in mongo_collection.find(result):
        docs.append(document)

    return docs
