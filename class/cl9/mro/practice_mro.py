import random
from requests import post, get

class SpaCommon():
    HOST = 'http://spa.ru.wott.iv'

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def create_url(self):
        return self.HOST + '/spa/accounts/'

class SpaAccount(object):
    # HOST = 'http://spa.ru.wott.iv'

    def __init__(self, ip='127.0.0.1', login=None, password='111111', activated=1):
        self.ip = ip
        self.login = login
        self.password = password
        self.activated = activated
        super(SpaAccount, self).__init__()

    def generate_unique(self):
        self.id = random.randint(10 ** 5, 10 ** 6)
        self.name = 'test{}'.format(self.id)
        self.login = '{}@test.com'.format(self.name)

    def create(self):
        return post(SpaCommon().create_url() + 'create/', data=self.__dict__).json()

    def __str__(self):
        return str(self.__dict__)


class SpaAccountNames(SpaCommon):
    # HOST = 'http://spa.ru.wott.iv'

    def __init__(self):
        super(SpaAccountNames, self).__init__()

    def get(self):
        super(SpaAccountNames, self).__init__()
        return get(SpaCommon().create_url() + 'names/').json()


# print(SpaAccountNames().get())
a = SpaAccount()
a.generate_unique()
print(a.id)