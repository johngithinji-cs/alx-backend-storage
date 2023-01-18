#!/usr/bin/env python3
"""function that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document in Python """
    return mongo_collection.insert(kwargs)
