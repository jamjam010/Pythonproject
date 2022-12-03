'''
모듈 사용법
from 모듈명 import 함수
from 모듈명 import 함수1, 함수2
from 모듈명 import *
'''
from converter import killometer_to_miles

miles = killometer_to_miles(150)
print('150km={}miles'.format(miles))