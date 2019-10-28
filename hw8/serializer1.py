# 1. Создать класс для сериализации данных Serializer. Объект класса принимает на вход сложный объект(list, dict, etc), и обладает методами loads и dumps. Эти методы работают так же как и json.loads и json.dumps.
# 2. dumps принимает на вход один параметр - contetnt_type(это может быть json или pickle) и на выходе возвращает строку в нужном формате(json или pickle).
# 3. Метод loads принимает два параметра - data и content_type, и возвращает новый объект типа Serializer со сложным объектом внутри

import json
import pickle

serializers = {'json': json, 'pickle': pickle}
class Serializer:
    def __init__(self, obj=None):
        self.obj = obj

    def get_method(self, content_type):
        return serializers.get(content_type)

    def dumps(self, content_type=None):
        print(self.get_method(content_type).dumps(self.obj))

    def loads(self, data=None, content_type=None):
        print(self.get_method(content_type).loads(data))

d = Serializer()
c = Serializer(obj={1: 2})

print('-pickle example-')
c.dumps(content_type='pickle')
d.loads(data=b'\x80\x03}q\x00K\x01K\x02s.', content_type='pickle')

print('-json example-')
c.dumps(content_type='json')
d.loads(data='{"1": 2}', content_type='json')