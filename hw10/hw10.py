# 1. Выбрать свой сервис/роект(rest), с которым вы дальше будете работать. Выбрать staging на котором вы будете работать со своим сервисом.
# 2. Выбрать 2 rest метода(желательно json), которые вы будете тестировать.
# 3. Написать код, который умеет работать с вашими rest методами. Т.е. он должен уметь:
# • Генерировать дефолтные данные
# • Сериализовать данные в/из json
# • Создавать данные на строне сервера(POST)
# • Получать данные с сервера(GET(by id), GET(list objects))


import json
import random
from requests import post, get

class HttpMixin():
    HOST = 'http://spa.ru.wott.iv/'
    def create_account(self):
        return post(url=self.HOST + '/spa/accounts/create/', data=self.wrap_data())
    def get_by_id(self, id):
        return get(url=self.HOST + '/spa/accounts/' + str(id) + '/').json()


class SpaAccount(HttpMixin):
    serializers = {'json': json}
    def __init__(self, id=None, name=None, ip='127.0.0.1', login=None, password='111111', activated=1):
        self.id = id
        self.name = name
        self.ip = ip
        self.login = login
        self.password = password
        self.activated = activated

    def generate_unique(self):
        self.id = random.randint(10**7, 10**8)
        self.name = 'test{}'.format(self.id)
        self.login = '{}@test.com'.format(self.name)

    def wrap_data(self):
        return self.__dict__

    def dumps(self, content_type='json'):
        return self.serializers[content_type].dumps(self.wrap_data())

    def loads(self, data, content_type='json'):
        return self.serializers[content_type].loads((data))

account = SpaAccount()
account.generate_unique()
print(account.wrap_data())
##Генерировать дефолтные данные
# print(account.generate_unique())

##Сериализовать данные в/из json
# print(account.dumps())
# print(account.loads(data='{"1": 2}'))

##Создавать данные на строне сервера(POST)
print(account.create_account())

##Получать данные на строне сервера(GET id)
print(account.get_by_id(id=54613))

##Получать данные на строне сервера(GET id)














# name = random.randint(10000, 200000)
# login = str(random.randint(10000, 200000)) + '@test.com'
# data = {
#     'name': name,
#     'ip': '127.0.0.1',
#     'login': login,
#     'password': '111111',
#     'activated': 1
# }
# def create_account():
#     new_account = post('http://spa.ru.wott.iv/spa/accounts/create/', data=data)
#     return new_account
# print(data)
# print(create_account())
# ========
# def unwrap_data(self, data):
#     return data

# class SerializerMixin():
#     serializers = {'json': json}
#     def dumps(self, content_type='json'):
#         return self.serializers[content_type].dumps(self.wrap_data())
#
#     def loads(self, data, content_type='json'):
#         return self.serializers[content_type].loads(self.unwrap_data(data))