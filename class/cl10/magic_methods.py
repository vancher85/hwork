class MagicExample(object):
    def __init__(self):
        self.id = 12
        self.name = 'admin'

    def __call__(self, *args, **kwargs):
        return self.__dict__.update(kwargs)

    # def __str__(self):
    #     return 'Str id:{0}, name:{1}'.format(self.id, self.name)
    #
    # def __repr__(self):
    #     return 'Repr: id:{}'.format(self.id)
    #
    # def __bytes__(self):
    #     return bytes('Bytes id:{0}, name:{1}'.format(self.id, self.name), encoding='utf-8')

magic = MagicExample()
##str
# print(magic)
##bytes
# print(bytes(magic))
## repr
# print([magic, magic])
##call
magic(ip='1.1.1.1')
print(magic.ip)