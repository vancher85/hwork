import random


class SpaAccount(object):
    def __init__(self, name='Iv', ip='127.0.0.1', login='login1', password='pass', activated=1, id=None):
        self.name = name,
        self.ip = ip,
        self.login = login
        self.password = password
        self.activated = activated
        # self.id = self.generate_id()
        self.id = id

    def generate_id(self):
        # return random.randint(10**5, 10**6)
        self.id = random.randint(10**5, 10**6)

    def __str__(self):
        return str(self.__dict__)

    # def create(self):
    #     return post(url=self.url + /sp/ac/crea, data=self._dict_).json

account = SpaAccount()
account.generate_id()
print(account)