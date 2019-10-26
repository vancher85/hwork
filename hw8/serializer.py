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