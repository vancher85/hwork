# 1. Создать класс для сериализации данных Serializer. Объект класса принимает на вход сложный объект(list, dict, etc), и обладает методами loads и dumps. Эти методы работают так же как и json.loads и json.dumps.
# 2. dumps принимает на вход один параметр - contetnt_type(это может быть json или pickle) и на выходе возвращает строку в нужном формате(json или pickle).
# 3. Метод loads принимает два параметра - data и content_type, и возвращает новый объект типа Serializer со сложным объектом внутри

import json
import pickle

class Serializer:
    def __init__(self, obj=None):
        self.obj = obj

    def dumps(self, content_type=None):
        if content_type == 'json':
            print(json.dumps(self.obj))
        elif content_type == 'pickle':
            print(pickle.dumps(self.obj))
        else:
            return

    def loads(self, data=None, content_type=None):
        if content_type == 'json':
            print(json.loads(data))
        elif content_type == 'pickle':
            print(pickle.loads(data))
        else:
            return
d = Serializer()
c = Serializer(obj={1:2})

print('-pickle example-')
c.dumps(content_type='pickle')
d.loads(data=b'\x80\x03}q\x00K\x01K\x02s.', content_type='pickle')
print('-json example-')
c.dumps(content_type='json')
d.loads(data='{"1": 2}', content_type='json')


# d.loads(data='[1,2]', content_type='json')