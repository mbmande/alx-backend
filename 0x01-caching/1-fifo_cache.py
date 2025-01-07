#!/usr/bin/env python3

""" ================================
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key
        """
        if key is None or item is None:
            return
        # check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.cache_keys.pop(0)  # discard first item (FIFO)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")
        self.cache_keys.append(key)
        self.cache_data[key] = item  # assign item to key in cache_data

    def get(self, key):
        """ Return value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
