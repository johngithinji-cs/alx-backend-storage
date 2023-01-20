#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


def cache(expiration: int):
    '''Caches the output of fetched data.
    '''
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            '''The wrapper function for caching the output.
            '''
            key = f"count:{args[0]}"
            _redis.incr(key)
            count = _redis.get(key)
            page_key = f"page:{args[0]}"
            page = _redis.get(page_key)
            if page:
                return page.decode()
            else:
                page = fn(*args, **kwargs)
                _redis.setex(page_key, expiration, page)
                return page
        return wrapper
    return decorator

@cache(10)
def get_page(url: str) -> str:
     '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text
