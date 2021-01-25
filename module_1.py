'''
모듈 : 필요한 것들 끼리 잘 만들어진 파일

theater_module.py 사용

1. 모듈은 지금 사용하는 같은 파일에 위치하거나,
2. 파이썬 라이브러리들이 모여있는 파일에 위치해 있을 경우 사용 가능

'''
'''
# import theater_module

# theater_module.price(3)
# theater_module.price_morning(2)
# theater_module.price_solider(4)

# import theater_module as mv # 별명 사용 가능

# mv.price(3)
# mv.price_solider(4)
# mv.price_morning(1)

from theater_module import *
# from random import *
# 모듈명이나 모듈 별병을 입력하지 않고 바로 모듈 내 함수를 사용할 수 있다.

price(3)
price_solider(5)
price_morning(2)
'''

from theater_module import price_morning, price

price(4)
price_morning(1)

from theater_module import price_solider as solp

solp(5)