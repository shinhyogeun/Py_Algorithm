# #Section02-1
# #파이썬 기초 코딩
# #Print 구문의 이해
#
# # 기본출력
# print('Hello!')
# print("asdasd")
# print("""hello!""")
# print('''hello!''')
#
# print()
#
#
# # Separator 옵션 사용
# print('T','P',sep='')
# print('2019','02','19',sep='-')
# print('niceman','google.com',sep='@')
#
#
# #end 옵션 사용
# print('Welcome To',end='')
# print("HILDI")
# print('testnoew')
# print()
#
#
# #format 사용
# print('{} and {}'.format('You','Me'))
# print('{0} and {1} and {0}'.format('You','Me'))
# print('{a} are {b}'.format(a='You',b='Me'))
#
#
# # %s: 문자, %d: 정수, f: 실수
# print("%s's favorite number is %d" % ('Eunki',7))
# print("Test1: %5d, Price: %4.2f" % (776,6543.123))
print("Test1: {0: 5d}, Price: {1:4.2f}".format(776,6543.123))
# print("Test1: {a: 5d}, Price: {b:4.2f}".format(a=776,b=6543.123))

a = '%02d'
b = '%04d'
c = (a+b) % (5,505)
print(c)
# c = a+b % (776,6543.123)
# print(c % (5,505))
# """
# 참고 : Escape 코드
#
# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \r : 캐리지 리턴
# \f : 폼 피드
# \a : 벨 소리
# \b : 백 스페이스
# \000 : 널 문자
# ...
#
# """
# \관련
# print("'you'")
# print('\'you\'')
# print('"You"')
# print("""'You""")
# print('\\You\\\n')
# print('me')
# print('\tYou\t\n')






