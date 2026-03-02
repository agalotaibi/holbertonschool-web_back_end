#!/usr/bin/env python3


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    If no document in the collection, returns an empty list.
    """
    return list(mongo_collection.find())
