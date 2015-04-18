import json
from flask import request

from .hooks import before_request


def route(bp, rule, **kwargs):
    def decorator(f):
        endpoint = kwargs.pop('endpoint', None)
        if isinstance(rule, list):
            for url in rule:
                bp.add_url_rule(url, endpoint, f, **kwargs)
        elif isinstance(rule, str):
            bp.add_url_rule(rule, endpoint, f, **kwargs)

        bp.before_request(before_request)
        return f
    return decorator


def get_post_data():
    data = request.form or request.data
    try:
        return json.loads(data)
    except (TypeError, ValueError):
        return data
