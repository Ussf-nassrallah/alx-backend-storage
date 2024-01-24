#!/usr/bin/env python3
''' 0x02. Redis basic with python '''

from typing import Union, Callable
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

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Union[str, bytes, int, float]:
        ''' get Method '''
        result = self._redis.get(key)
        if fn is not None:
            return fn(result)
        return result

    def get_str(self, key: str) -> str:
        ''' get string value '''
        result = self.get(key, lambda x: x.decode('utf-8'))
        return result

    def get_int(self, key: str) -> int:
        ''' get int value '''
        result = self.get(key, lambda x: int(x))
        return result
