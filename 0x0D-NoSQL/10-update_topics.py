#!/user/bin/env python3
""" update mongo"""


def update_topics(mongo_collection, name, topics):
    """Update doc by name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})