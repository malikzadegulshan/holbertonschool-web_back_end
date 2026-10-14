#!/usr/bin/env python3
""" Changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """Sets the topics list on every document matching the name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
