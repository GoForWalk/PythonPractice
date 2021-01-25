'''
package : module 들의 집합

신규여행사 프로젝트
파이썬 패키지로 생성해서 사용

패키지의 폴더명 : travel

'''

# import travel.thailand # 모듈이나 패키지만 가능하다. (함수 or 메소드는 불가능)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 
# trip_to2 = ThailandPackage()
# trip_to2.detail()

# from travel import vietnam
# trip_vi = vietnam.VietnamPackage()
# trip_vi.detail()


from travel import *
# 패키지내에서 공개 비공개 여부를 지정을 해야한다. 
# (그 전에는 from travel import * 을 사용했을때 import가 활성화 되지 않는다.)
# 패키지 내 __init__.py 파일에서 설정할 수 있다.
# __all__ 에서  패키지내에서 공개할 모듈을 지정할 수 있다.

trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to1 = thailand.ThailandPackage()
trip_to1.detail()

# __all__ 에서 vietnam 만 공개 설정을 했기 때문에 thailand에 대한 모듈은 현재 파일에서 사용할 수 없다.

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

