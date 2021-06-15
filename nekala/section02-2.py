#Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print('My anme is Goodboy!')

# 변수 선언 / 변수 선언은 (한글)도 가능
myname = 'Goodboy'

# 조건문
if myname == 'Goodboy':
    print('ok')

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print("%d * %d = " %(i,j), i*j)

# 함수 선언
def 인사():
    print('안녕하세요.')

인사()

def hello():
    print('ok!')

hello()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()
print(id(cookie))
print(dir(cookie))
