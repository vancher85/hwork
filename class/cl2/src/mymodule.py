import random  # целый модуль
import datetime

# from random import (
#     random,
#     randint as randint_system,
#     randrange
# )
#
# from random import *  # все имена импортируются в глобальную область видимости (когда работаем с конфигами)

# print(random.random())
# print(random.randint(1, 100))

########
# from urllib.parse import urlparse
# wargaming_url = urlparse('http://wargaming.net')
# if __name__ == "__main__":
#     print('I\'m from modeule1', wargaming_url)



#######
from urllib.parse import urlparse
# from mymodule2 import SET
wargaming_url = urlparse('http://wargaming.net')
ivanimport = "it's import from mymodule"

if __name__ == "__main__":
    print('I\'m from modeule1', wargaming_url)
# print('I\'m from modeule1', wargaming_url)