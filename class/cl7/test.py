# #ex1
# def func_decor(func):
#     def decorator(*args, **kwargs):
#         raw_response = func(*args, **kwargs)
#         return '***{}***'.format(raw_response)
#
#     return decorator
#
#
# @func_decor
# def expected_func(string):
#     return 'Hello {}'.format(string)
#
#
# @func_decor
# def expected_func_2(number):
#     return number ** 2
#
#
# print(expected_func('world'))
# print(expected_func_2(2))


# # ex2
# is_staging = True
#
# def create_real_user(use):
#     def func_decor(func):
#         def decorator(**kwargs):
#             raw_response = func(**kwargs)
#             return '***{}***'.format(raw_response)
#         if use:
#             return decorator
#         return func
#     return func_decor
#
# @create_real_user(use=is_staging)
# def expected_func(string):
#     return 'Hello {}'.format(string)
# @create_real_user(use=is_staging)
# def expected_func_2(number):
#     return number**2
#
# print(expected_func_2(4))