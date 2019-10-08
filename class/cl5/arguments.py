# позиционные
# def func(arg1, arg2):
#     print(arg1/arg2)
#
# func(1,2)
# func(3,4)

# именнованные
# def func(arg, arg1=None, arg2=2):
#     if arg2 is None:
#         raise Exception(arg1)
#     print(arg/arg2)
#
# func(1)
# func(3,4)

# динамические (позиционные неизвестной длинны)
# def func(*args):
#     print(args)
#     i = args[0]
#     for arg in args[1:]:
#         i = i/arg
#     return i
#
# print(func(1,1,1))
# print(func(10,2,5,6))


# def func(*urls):
#     result_url = ""
#     for i in urls:
#         result_url += i
#     return result_url
# print(func('/users', '/posts'))


# def func(host, *path):
#     result_url = ""
#     for i in path:
#         result_url += i
#     return host + result_url
# print(func('localhost', '/users', '/posts'))

# **queries
# def func(host, *path, **queries):
#     print(queries)
#     result_url = ""
#     for i in path:
#         result_url += i
#     if queries:
#         result_url += '?'
#         for i, j in queries.items():
#             result_url += (i + '=' + j)
#             result_url += '&'
#     return host + result_url
# print(func('localhost', '/users', '/posts',  a='1', b='2'))


#split arguments
# from urllib.parse import quote, urlencode
# from urllib.request import urlopen as base_urlopen
# def urlopen(url='http://google.com', query_params=None):
#     if query_params:
#         query_params = urlencode(query_params)
#         url = url + '?' + query_params
#         print(url)
#     return base_urlopen(url).read().decode('utf-8')
#
# def parse_elements(element='<img', **url_arguments):
#     print(element, url_arguments)
#     page = urlopen(**url_arguments)
#     return page.count(element)
# print(parse_elements(element='href', url='https://ru.wargaming.net/', query_params={'a': 'b'}))
#
# # print(parse_elements())
# # print(parse_elements(element='href', url='https://ru.wargaming.net/'))


#TODO
from urllib.parse import quote, urlencode
# from urllib.request import urlopen as base_urlopen
# def urlopen(url='http://google.com'):
#     print(url)
#     return base_urlopen(url).read().decode('utf-8')
#
# def parse_elements(element='<img', *url_arguments):
#     print(element, url_arguments)
#     page = urlopen(*url_arguments)
#     return page.count(element)
# print(parse_elements(element='href', url='https://ru.wargaming.net/'))

# print(parse_elements())
# print(parse_elements(element='href', url='https://ru.wargaming.net/'))

#фабричный метод
# def linux(dct):
#     return 'linux: {}'.format(dct)
#
# def windows(dct):
#     return 'windows: {}'.format(dct)
#
# def mac(dct):
#     return 'mac: {}'.format(dct)
#
# def fabric_method(dct, os='linux'):
#     if os == 'linux':
#         return linux(dct)
#     if os == 'windows':
#         return windows(dct)
#     if os == 'mac':
#         return mac(dct)
#     return 'Unsupported os type'
# print(fabric_method({'a':'b'}))


# абстрактная фабрика
# def linux(dct):
#     return 'linux: {}'.format(dct)
#
# def windows(dct):
#     return 'windows: {}'.format(dct)
#
# def mac(dct):
#     return 'mac: {}'.format(dct)
#
# def absract_fabric(func, arg):
#     return func(arg)
# print(absract_fabric(linux, {'a':'b'}))
# print(absract_fabric(windows, {'a':'b'}))




import json
import pickle

user = {'id': 1234, 'username': 'test'}

def dumps(library, data):
    return library.dumps(data)


def load(library, data):
    return library.loads(data)

pickle_user = dumps(pickle, user)
json_user = dumps(json, user)

print(pickle_user)
print(json_user)


print(load(pickle, pickle_user))
print(load(json, json_user))