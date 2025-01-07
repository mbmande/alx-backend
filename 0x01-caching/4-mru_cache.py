#!/usr/bin/env python3

""" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        # Initialize the access order list to
        # track the order of access to cache items
        self.access_order = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
        """
        if key is None or item is None:
            return
        # check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # discard most recently used item (MRU)
            # remove the most recently used key from access order
            mru_key = self.access_order.pop()
            # remove the corresponding item from cache data
            del self.cache_data[mru_key]
            # print the discarded key for debugging purposes
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item  # assign item to key in cache data
        self.access_order.append(key)  # add key to access order

    def get(self, key):
        """ Return value in self.cache_data linked to key
        """
        # if key is None or key not in self.cache_data:
        #     return None
        # return self.cache_data.get(key)
        if key is not None:  # check if key is not None
            if key in self.cache_data:  # if key exists in cache_data
                # update access order
                self.access_order.remove(key)
                self.access_order.append(key)
                return self.cache_data[key]  # return value associated with key
        return None  # return None if key is None or key not in cache_data
