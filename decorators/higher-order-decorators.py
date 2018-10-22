"""
Demonstrates a sample usage of Higher Order Decorators
"""

import json


def response_type(type='json'):
    def handle_response(fn):
        def wrapper(*args, **kwargs):
            response = fn(*args, **kwargs)
            if type is 'json':
                return json.loads(response).get('data')
            elif type is 'string':
                return response.split(':')[1]
            else:
                return None
        return wrapper
    return handle_response


@response_type('json')
def on_success_1(data):
    return data


@response_type('string')
def on_success_2(data):
    return data


print(on_success_1('{ "data": "Response 200" }'))
print(on_success_2('data:Response 200'))
