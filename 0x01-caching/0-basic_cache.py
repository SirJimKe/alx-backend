#!/usr/bin/env pyhton3
""" Create a class BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Returns data from parent class attribute cache-data"""
    def put(self, key, item):
        """Assigns the item value to the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Returns the value linked to key"""
        if key is None or key != self.cache_data.keys():
            return self.cache_data.get(key, None)
        return self.cache_data.get(key)
