#!/user/bin/env python3
""" insert mongodb """


def insert_school(mongo_collection, **kwargs):
    """inserts in school collection"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)