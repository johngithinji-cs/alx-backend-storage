#!/usr/bin/env python3
""" function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ Where can I learn Python? """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
