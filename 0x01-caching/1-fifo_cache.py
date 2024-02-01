#!/usr/bin/env python3
"""Task 1 module """
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class that inherits from BaseCaching'''
    def __init__(self):
        '''Initialize the attributes from parent class'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Using FIFO to pop the first item to cache '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print('DISCARD:', first_key)

    def get(self, key):
        '''Return the value linked to the key popped'''
        if key is None or key != self.cache_data.keys():
            return self.cache_data.get(key, None)
        return self.cache_data.get(key)
