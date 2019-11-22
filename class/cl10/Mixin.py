# import json
# import random
# from requests import post, get
# class HttpMixin(object):
#     HOST = 'http://spa.ru.wott.iv'
#     def post(self):
#         return self.loads(post(url=self.HOST + '/spa/accounts/create/', data=self.dumps()).text)
#     def get(self):
#         pass
# class Serializer(object):
#     serializers = {'json': json}
#     def dumps(self, content_type='json'):
#         dumper = self.serializers[content_type]
#         return dumper.dumps(self.wrap_data())
#     def loads(self, data, content_type='json'):
#         loader = self.serializers[content_type]
#         return loader.loads(self.unwrap_data(data))
# class SpaAccount(HttpMixin, Serializer):
#     def __init__(self, id=None, name=None, ip='127.0.0.1', login=None, password='111111', activated=1):
#         self.id = id
#         self.name = name
#         self.ip = ip
#         self.login = login
#         self.password = password
#         self.activated = activated
#     def generate_unique(self):
#         self.id = random.randint(10**5, 10**6)
#         self.name = 'test{}'.format(self.id)
#         self.login = '{}@test.com'.format(self.name)
#     def wrap_data(self):
#         return self.__dict__
#     def unwrap_data(self, data):
#         return data
#     def __str__(self):
#         return str(self.wrap_data())
# account = SpaAccount()
# account.generate_unique()
# print(account.post())