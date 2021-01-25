'''
google 에서 pypi 검색



'''

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

'''
terminal 창에서

pip list : 설치된 패키지들을 볼 수 있다.

pip 패키지명 : 해당 패키지의 정보를 보여준다.

pip install --upgrade 패키지명 : 해당 패키지를 최신 버전으로 업그레이드한다.

pip uninstall 패키지명 : 해당 패키지를 삭제한다.

'''