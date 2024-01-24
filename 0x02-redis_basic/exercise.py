#!/usr/bin/env python3
''' 0x02. Redis basic with python '''

from typing import Union, Callable, Any
import uuid
import redis
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' count_calls '''
    @wraps(method)
    def fn(self, *arguments, **kwargs) -> Any:
        ''' inc '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *arguments, **kwargs)

    return fn


def call_history(method: Callable) -> Callable:
    ''' call_history '''
    @wraps(method)
    def fn(self, *arguments, **kwargs) -> Any:
        ''' storing list '''
        inputs = f'{method.__qualname__}:inputs'
        outputs = f'{method.__qualname__}:outputs'

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(inputs, str(arguments))

        result = method(self, *arguments, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(outputs, result)
        return result

    return fn


class Cache:
    ''' Cash '''
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
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
