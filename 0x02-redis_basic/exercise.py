#!/usr/bin/env python3
""" Documentation Module """

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """Documentation init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Documentation store """
        Keyx = str(uuid.uuid4())
        self._redis.set(Keyx, data)
        return Keyx
