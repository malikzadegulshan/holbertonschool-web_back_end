#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """Returns a list of all documents in the collection,
    or an empty list if there are none"""
    return list(mongo_collection.find())
