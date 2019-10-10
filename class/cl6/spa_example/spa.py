from requests import get, post
from random import randint

# def get_account_names(name=None, limit=None):
#     dict = get('http://spa.ru.wott.iv/spa/accounts/names/', params='limit='+str(limit)).json()
#     # print(dict.items())
#     for i,j in dict.items():
#         if j == name:
#             return i
#
# def find_name(name, limit):
#     return get_account_names(name, limit)
#
# # print(find_name('jewel13_WGT11', 2))

name = randint(10000, 200000)
login = str(randint(10000, 200000))+'@test.com'
data = {
        'name': name,
        'ip': '127.0.0.1',
        'login': login,
        'password': '111111',
        'activated': 1
    }

def create_account():
    new_account = post('http://spa.ru.wott.iv/spa/accounts/create/', data=data).json()
    # return find_name(name, 10000)
    # print(find_name('name', 2))
    # print(new_account)
    for i, j in new_account.items():
        if i == 'id':
            return get_account(j)

def get_account(id):
     account = get('http://spa.ru.wott.iv/spa/accounts/'+str(id)+'/').json()
     return account

print(create_account())

# import random
# from requests import get, post
# def get_account_names(limit=10):
#     return get('http://spa.ru.wott.iv/spa/accounts/names/', params={'limit': limit}).json()
# def find_name(name='test', limit=100):
#     names = get_account_names(limit=limit)
#     return {i: j for i, j in names.items() if name in j.lower()}
# def generate_account():
#     name = 'test{}'.format(random.randint(10**4, 10**5))
#     data = {
#         'name': name,
#         'ip': '127.0.0.1',
#         'login': '{}@test.com'.format(name),
#         'password': '111111',
#         'activated': 1
#     }
#     return data
# def create_account(data):
#     return post('http://spa.ru.wott.iv/spa/accounts/create/', data=data).json()
# def check_accounts(expected, result):
#     for key, value in expected.items():
#         assert result[key] == value
# def get_account(spa_id):
#     return get('http://spa.ru.wott.iv/spa/accounts/{}/'.format(spa_id)).json()
# def check_spa_creation():
#     account = generate_account()
#     created_account = create_account(account)
#     account_id = created_account['id']
#     result_account = get_account(account_id)
#     expectd_account = {i: j for i, j in account.items() if i in ('name',)}
#     check_accounts(expectd_account, result_account)
# check_spa_creation()
