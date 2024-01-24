#!/usr/bin/env python3
''' Implementing an expiring web cache and tracker '''

from functools import wraps
from typing import Callable

import redis
import requests

store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    ''' data_cacher '''
    @wraps(method)
    def fn(url) -> str:
        ''' fn: function thats caching output '''
        store.incr('count:{}'.format(url))
        output = store.get('result:{}'.format(url))

        if output:
            return output.decode('utf-8')

        output = method(url)
        store.set(f'count:{url}', 0)
        store.setex(f'result:{url}', 10, output)
        return output

    return fn


@data_cacher
def get_page(url: str) -> str:
    ''' get page '''
    return requests.get(url).text
