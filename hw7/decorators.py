import random
from requests import post
import json

spa_version = 1

def generate_account():
    name = 'test{}'.format(random.randint(10**4, 10**5))
    data = {
        'name': name,
        'ip': '127.0.0.1',
        'login': '{}@test.com'.format(name),
        'password': '111111',
        'activated': 1
    }
    return data

def serializator(version):
    def func_decor(func):
        def decorator(data, *args, **kwargs):
            # print(*args)
            # print(json.dumps(*args))
            return func(json.dumps(data), *args, **kwargs)
        if spa_version == 1:
            return decorator
        return func
    return func_decor


@serializator(version=spa_version)
def create_account(data):
    return post('http://spa.ru.wott.iv/spa/accounts/create/', data=data).json()

account = generate_account()
print(create_account(account))