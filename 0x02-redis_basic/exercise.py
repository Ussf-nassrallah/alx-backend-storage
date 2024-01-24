#!/usr/bin/env python3
''' 0x02. Redis basic with python '''

from typing import Union
import uuid
import redis


class Cache:
    ''' Cash '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store method '''
        ran_key = str(uuid.uuid4())
        self._redis.set(ran_key, data)
        return ran_key
