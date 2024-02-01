#!/usr/bin/env python3
''' Last In First Out Cache module'''
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Implements LIFO in caching'''
    def __init__(self):
        ''' Initializes attributes from parent class'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Implements LIFO method in caching'''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''Return the value linked to the key popped'''
        if key is None or key != self.cache_data.keys():
            return self.cache_data.get(key, None)
        return self.cache_data.get(key)
