#!/usr/bin/env python3
""" Returns the list of schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """Returns all documents whose topics list contains the topic"""
    return list(mongo_collection.find({"topics": topic}))
