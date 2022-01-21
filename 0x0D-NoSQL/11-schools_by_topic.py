#!/usr/bin/env python3
"""docs and notes"""


def schools_by_topic(mongo_collection, topic):
    """returns list of school with specific topic"""
    return [item for item in mongo_collection.find({"topics": topic})]