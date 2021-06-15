#1018 체스판
# n,m = map(int,input().split())
#
# total = []
# answers = []
#
# def turnOne(total,i,j,mode):
#     a = [['B','W'],['W','B']]
#     answer = 0
#     for k in range(8):
#         for u in range(8):
#             if (k+u)%2 == 1 and total[i+k][j+u] != a[mode][0]:
#                 answer += 1
#             elif (k+u)%2 == 0 and total[i+k][j+u] != a[mode][1]:
#                 answer += 1
#
#     return answer
#
# for i in range(n):
#     total.append(list(input()))
#
# for i in range(n-7):
#     for j in range(m-7):
#         answers.append(turnOne(total,i,j,0))
#         answers.append(turnOne(total,i,j,1))
#
# print(min(answers))

# 1085 직사각형에서 탈출

# x,y,w,h = map(int,input().split())
# print(min(x,y,w-x,h-y))

# 1181번 정렬

# n = int(input())
# total = []
# for i in range(n):
#     word = input()
#     total.append((len(word),word))
# total = sorted(list(set(total)))
#
# for i in total:
#     print(i[1])

# 1259 팰린드롬수

# answer = []
#
# while True:
#     n = input()
#     if not int(n): break
#     if len(n)%2 == 1 and list(n)[:len(n)//2][::-1] == list(n)[len(n)//2+1:]:
#         print('yes')
#         continue
#     if len(n)%2 == 0 and list(str(n))[:len(n)//2][::-1] == list(str(n))[len(n)//2:]:
#         print('yes')
#         continue
#     print('no')

# 1436 영화감독 숌
# n = int(input())
# answer = []
# start = 666
#
# while len(answer) != n:
#     if '666' in str(start):
#         answer.append(start)
#     start += 1
#
# print(answer[-1])

# 1463 1로 만들기

# n = int(input())
#
# total = [0,0,1,1]
# if n <= 3:
#     print(total[n])
# else:
#     for i in range(4,n+1):
#         mini = []
#         if i%3 == 0:
#             mini.append(i//3)
#         if i%2 == 0:
#             mini.append(i//2)
#         mini.append(i-1)
#
#         total.append(min([total[i] for i in mini]) + 1)
#     print(total[-1])

# 2108번 통계학
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# total = []
# rlrl = {}
# for i in range(n):
#     a = int(input())
#     total.append(a)
#     if a in rlrl.keys():
#         rlrl[a] += 1
#     else:
#         rlrl[a] = 1
#
# total = sorted(total)
# new = sorted(rlrl.items(),key=(lambda x:x[1]),reverse=True)
# king = []
#
# for i in rlrl.keys():
#     if rlrl[i] == new[0][1]:
#         king.append(i)
#
# print(round(sum(total)/len(total)))
# print(total[len(total)//2])
# if len(king) == 1:
#     print(king[0])
# else:
#     print(sorted(king)[1])
# print(total[-1]-total[0])

# 2609번 최대공약수 최소공배수
# import math
# a,b = map(int,input().split())
# gcd = math.gcd(a,b)
# ggd = gcd * a//gcd * b//gcd
#
# print(gcd, ggd)

# 2292번 벌집
# n = int(input())
# answer = 1
# count = 1
# while answer < n:
#     answer += count * 6
#     count += 1
#
# print(count)

# 2231번 분해합
# n = int(input())
# for i in range(n):
#     if i + sum(list(map(int,(list(str(i)))))) == n:
#         print(i)
#         break
# else:
#     print(0)

# 2164번 카드2
# from collections import deque
#
# asd = int(input())
#
# total = deque([str(i+1) for i in range(asd)])
#
# while len(total) != 1:
#     total.popleft()
#     total.append(total.popleft())
#
# print(total[0])

# 2164번 카드2
# import math
#
# total = [True] * 1001
# total[1] = False
#
# for i in range(2,math.floor(math.sqrt(1000))+1):
#     j = 2
#     while i*j <= 1000:
#         total[i*j] = False
#         j += 1
#
# a = int(input())
# lis=list(map(int,input().split()))
# answer = 0
# for i in lis:
#     if total[i]:
#         answer += 1
#
# print(answer)

# 2164번 카드2
# from collections import deque
#
# c = int(input())
# answer = []
#
# for i in range(c):
#     n,m = map(int,input().split())
#     total = list(map(int,input().split()))
#     newTotal = deque()
#     for i,v in enumerate(total):
#         newTotal.append((v,i))
#     who = -1
#     count = 0
#     while who != m:
#         if newTotal[0][0] == max([i[0] for i in newTotal]):
#             count += 1
#             who = newTotal.popleft()[1]
#         else:
#             newTotal.append(newTotal.popleft())
#     answer.append(count)
#
# for i in answer:
#     print(i)

# 1920번 수 찾기
# n = int(input())
# a = list(set(list(map(int,input().split()))))
# m = int(input())
# target = list(map(int,input().split()))
#
# for i in target:
#     if i in a:
#         print(1)
#     else:
#         print(0)

#2751번 수 정렬하기
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# answer = []
# for i in range(n):
#     answer.append(int(input()))
#
# for i in sorted(answer):
#     print(i)

#2751번 수 정렬하기
# number = int(input())
# for i in range(number):
#     k = int(input())
#     n = int(input())
#     total = [[i+1 for i in range(n)]]
#     for i in range(1,k+1):
#         mini = [1]
#         for j in range(2,n+1):
#             mini.append(sum(total[i-1][:j]))
#         total.append(mini)
#     print(total[-1][-1])

#2798번 블랙잭
# from itertools import combinations
# import heapq
#
# n,m = map(int,input().split())
# total = list(map(int,input().split()))
# a = []
# for i in combinations(total,3):
#     if sum(i) > m:
#         continue
#     else:
#         heapq.heappush(a,m-sum(i))
# an = heapq.heappop(a)
# print(m-an)

#2839번 설탕배달
# n = int(input())
# INF = 1e9
# total = [INF] * 5001
#
# total[3] = 1
# total[5] = 1
#
# for i in range(6,n+1):
#     total[i] = min(total[i-3],total[i-5]) + 1
# if total[n] >= INF:
#     print(-1)
# else:
#     print(total[n])

#2869번 달팽이는 올라가고 싶다.
# a,b,v = map(int,input().split())
#
# oneDay = a-b
#
# if (v-a)%oneDay != 0:
#     print((v-a)//oneDay+2)
# else:
#     print((v-a)//oneDay+1)

#1453번 직각삼각형
# while True:
#     total = sorted(list(map(int,input().split())))
#     if sum(total) == 0:
#         break
#
#     if total[-1]**2 == total[0]**2 + total[1]**2:
#         print("right")
#     else:
#         print("wrong")

#4949번 균형잡힌 세상
# from collections import deque
#
# open = ['(', '[']
# close = [')',']']
#
# while True:
#     word = list(input())
#     if len(word) == 1 and word[0] == '.':
#         break
#     a = deque()
#     for i,v in enumerate(word):
#         if v in open:
#             a.append(v)
#         elif v in close:
#             if len(a) != 0 and a[-1] == open[close.index(v)]:
#                 a.pop()
#             else:
#                 a.append(v)
#     if len(a) > 0:
#         print('no')
#     else:
#         print('yes')

#7568번 덩치
# n = int(input())
# total = []
# for i in range(n):
#     total.append(tuple(map(int,input().split())))
#
# answer = []
# for i in total:
#     count = 0
#     for j in total:
#         if j[0] > i[0] and j[1] > i[1]:
#             count += 1
#     answer.append(count+1)
#
# print(' '.join(map(str,answer)))

#9012번 괄호
# from collections import deque
#
# n = int(input())
#
# for i in range(n):
#     a = deque()
#     target = list(input())
#     for k in target:
#         if k == ')':
#             if len(a) != 0 and a[-1] =='(':
#                 a.pop()
#             else:
#                 a.append(k)
#         else:
#             a.append(k)
#     if len(a) != 0 :
#         print('NO')
#     else:
#         print('YES')

#10250번 ACM호텔
# n = int(input())
#
# for i in range(n):
#     h,w,number = map(int,input().split())
#     if number%h == 0:
#         if number//h >= 10:
#             print(str(h)+str(number//h))
#         else:
#             print(str(h) + '0' + str(number//h))
#     else:
#         if 1+number//h >= 10:
#             print(str(number%h) + str(1+number//h))
#         else:
#             print(str(number % h) + '0' + str(1+number // h))

#10773번 제로
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# n = int(input())
# q = deque()
#
# for i in range(n):
#     a = int(input())
#
#     if a != 0:
#         q.append(a)
#     else:
#         q.pop()
#
# print(sum(q))

#10814번 나이순 정렬
# import sys
#
# input = sys.stdin.readline
# n = int(input())
# a = {}
# for i in range(n):
#     one = list(input().split())
#     one[0] = int(one[0])
#     if one[0] in a.keys():
#         a[one[0]].append(one[1])
#     else:
#         a[one[0]] = [one[1]]
#
# for i in sorted(a.keys()):
#     for j in a[i]:
#         print(i, j)

#10816번 숫자카드2
# n = int(input())
# total = list(map(int,input().split()))
# dic = {}
# for i in total:
#     if i in dic.keys():
#         dic[i] += 1
#     else:
#         dic[i] = 1
# m = int(input())
#
# answer = []
# target = list(map(int,input().split()))
#
# for i in target:
#     if i in dic.keys():
#         answer.append(dic[i])
#     else:
#         answer.append(0)
#
# print(' '.join(list(map(str,answer))))

# 10828번 스택
# from collections import deque
# import sys
# input = sys.stdin.readline
# mother = deque()
# n = int(input())
#
# for i in range(n):
#     n = list(input().split())
#     if n[0] == 'push':
#         mother.append(n[1])
#     elif n[0] =='pop':
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother.pop())
#     elif n[0] == 'size':
#         print(len(mother))
#     elif n[0] == 'empty':
#         if len(mother) == 0:
#             print(1)
#         else:
#             print(0)
#     elif n[0] == 'top':
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother[-1])

# 10989번 수정렬하기3
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr= [0] * 10001
#
# for i in range(n):
#     arr[int(input())] += 1
#
# for i in range(10001):
#     if arr[i] != 0:
#         for j in range(arr[i]):
#             print(i)

# 1874번 스택수열

# from collections import deque
#
# n = int(input())
# arr = deque()
# answer = []
# bucket = []
# making = []
# total = []
# base = deque([i+1 for i in range(n)])
# exit = False
# for i in range(1,n+1):
#     arr.append(int(input()))
#
# while arr:
#     if arr[0] in bucket:
#         exit = True
#         break
#     if making == [] or making[-1] < arr[0]:
#         making.append(base.popleft())
#         answer.append('+')
#     elif making[-1] > arr[0]:
#         bucket.append(making.pop())
#         answer.append('-')
#     elif making[-1] == arr[0]:
#         total.append(making.pop())
#         answer.append('-')
#         arr.popleft()
#
# if exit:
#     print('NO')
# else:
#     for i in answer:
#         print(i)

# 11050 이항계수
# n,k = map(int,input().split())
# a = 1
# for i in range(2,n+1):
#     a *= i
# b = 1
# for i in range(2,k+1):
#     b *= i
# c = 1
# for i in range(2,n-k+1):
#     c *= i
#
# print(int(a/(c*b)))

# 11650 좌표정렬하기
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for i in range(n):
#     inp = tuple(map(int,input().split()))
#     arr.append(inp)
#
# for i in sorted(arr):
#     print(' '.join(list(map(str,i))))

# 11651 좌표정렬하기2
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for i in range(n):
#     a,b = map(int,input().split())
#     arr.append((b,a))
#
# for i in sorted(arr):
#     print(' '.join(list(map(str,reversed(i)))))


# 요세푸스 문제0
# from collections import deque
#
# n,k = map(int,input().split())
# answer = []
# total = deque([i for i in range(1,n+1)])
#
# while len(answer) != n:
#     mini = deque()
#     if k % len(total) == 0:
#         answer.append(total.pop())
#     else:
#         for i in range(k % len(total) - 1):
#             total.append(total.popleft())
#         answer.append(total.popleft())
#
# ans = '<'
# ans += ', '.join(map(str,answer))
# ans += '>'
# print(ans)

#18111 마인크래프트

n,m,b = map(int,input().split())
total = []
answerArr = []

for i in range(n):
    total.append(list(map(int,input().split())))

dic = {i:0 for i in set(total)}

for i in range(len(total)):
    dic[i] += 1
    
for i in set(total):
    an = 99
    time = 0
    for j in dic.keys():
        if j >= i:
            time += (j-i)*2
            an += (j-i)
        else:
            time += (i-j)
            an -= (i-j)
    if an >= 0:

