# 팩토리얼 0의 개수

# n = int(input())
# answer = 1
# for i in range(1,n+1):
#     answer *= i
# a = 0
# for i in str(answer)[::-1]:
#     if i == '0':
#         a += 1
#     else:
#         break
# print(a)

# 1003번 피보나치 함수
# n = int(input())
# arr = [[1,0],[0,1],[1,1]]
# for i in range(38):
#     arr.append([arr[-1][0]+arr[-2][0],arr[-1][1]+arr[-2][1]])
#
# for i in range(n):
#     k = int(input())
#     print(' '.join(map(str,arr[k])))

# 1012번 유기농 배추
# n = int(input())
# answer = []
#
# for i in range(n):
#     m,l,k = map(int,input().split())
#     total = [[0 for _ in range(m)] for _ in range(l)]
#     count = [0]
#
#     def dfs(z, j):
#         if total[z][j] != 1:
#             return
#         total[z][j] = 9
#         dm = [1,0,-1,0]
#         dl = [0,1,0,-1]
#         for one,two in zip(dm,dl):
#             if l > z+two >= 0 and m > j+one >= 0 and total[z+two][j+one] == 1:
#                 dfs(z+two,j+one)
#
#     for j in range(k):
#         a,b = map(int,input().split())
#         total[b][a] = 1
#
#     for j in range(m):
#         for z in range(l):
#             if total[z][j] == 1:
#                 count[0] += 1
#                 dfs(z,j)
#
#     answer.append(count[0])
# for i in answer:
#     print(i)

# 1764번 듣보잡
# n,m = map(int,input().split())
# N = set()
# M = set()
#
# for i in range(n):
#     N.add(input())
#
# for i in range(m):
#     M.add(input())
#
# total = sorted(list(N.intersection(M)))
# print(len(total))
#
# for i in total:
#     print(i)

# 9095번 1,2,3 더하기
# n = int(input())
#
# for i in range(n):
#     arr = [0, 1, 2, 4]
#     target = int(input())
#
#     if target <= 3:
#         print(arr[target])
#     else:
#         for i in range(4,target+1):
#             arr.append(sum([arr[i-3],arr[i-2],arr[i-1]]))
#         print(arr[-1])

# 1697번 숨바꼭질
# from collections import deque
#
# total = [1e8] * 100001
# n,k = map(int,input().split())
#
# total[n] = 0
#
# def check(n):
#     q = deque()
#     q.append((n,0))
#
#     while q:
#         i,v = q.popleft()
#         if i < 100000 and total[i+1] == 1e8:
#             q.append((i+1,v+1))
#             total[i+1] = v+1
#         if i <= 50000 and total[i*2] == 1e8:
#             q.append((i*2,v+1))
#             total[i*2] = v+1
#         if i > 0 and total[i-1] == 1e8:
#             q.append((i-1,v+1))
#             total[i-1] = v+1
#
# check(n)
#
# print(total[k])

#1541번 잃어버린 괄호
# from collections import deque
#
# arr = deque(list(input()))
# a = ''
# b = ''
#
# while arr:
#     if arr[0] == '-':
#         break
#     a += arr.popleft()
#
# b = ''.join(arr)[1:]
# answer1 = sum(map(int,a.split('+')))
# if b:
#     answer2 = sum([sum(map(int,i.split('-'))) for i in b.split('+')])
#     print(answer1 - answer2)
# else:
#     print(answer1)

# 1074번 Z
# N,r,c = map(int,input().split())
# total = (2**N)**2
# count = 0
#
# def counting(N,m,l):
#     global count
#     if l == r and m == c:
#         return count
#     ## 왼쪽위에 있을 떄
#     if l+(2**N)//2-1 >= r >= l and m+(2**N)//2-1 >= c >= m:
#         return counting(N-1,m,l)
#     ## 오른쪽위에 있을 떄
#     if l+(2**N)//2-1 >= r >= l and m+(2**N)-1 >= c >= m+(2**N)//2:
#         count += ((2**N)**2)//4
#         return counting(N-1,m+(2**N)//2,l)
#     ## 왼아래에 있을 떄
#     if m + (2**N)//2-1 >= c >= m and l+(2**N)-1 >= r >= l+(2**N)//2:
#         count += ((2**N)**2)//2
#         return counting(N-1,m,l+(2**N)//2)
#     ## 오른쪽아래에 있을 떄
#     if m + (2**N)-1 >= c >= m+(2**N)//2 and l+(2**N)-1 >= r >= l+(2**N)//2:
#         count += (((2**N)**2)//4)*3
#         return counting(N-1,m+2**N//2,l+2**N//2)
#
# print(counting(N,0,0))

#패션왕 신해빈

# n = int(input())
# answer = []
# for i in range(n):
#     number = int(input())
#     total = {}
#     ultra = 1
#     for j in range(number):
#         name,kind = input().split()
#         if kind in total.keys():
#             total[kind] += 1
#         else:
#             total[kind] = 1
#     values = total.values()
#     for i in values:
#         ultra *= (i+1)
#     answer.append(ultra-1)
#
# for i in answer:
#     print(i)

#11723번 집합
# import sys
# input = sys.stdin.readline
# n = int(input())
# king = set()
#
# for i in range(n):
#     info = input().split()
#     if info[0] == 'add':
#         king.add(int(info[1]))
#     elif info[0] == 'remove':
#         if int(info[1]) in king:
#             king.remove(int(info[1]))
#     elif info[0] == 'check':
#         if int(info[1]) in king:
#             print(1)
#         else:
#             print(0)
#     elif info[0] == 'toggle':
#         if int(info[1]) in king:
#             king.remove(int(info[1]))
#         else:
#             king.add(int(info[1]))
#     elif info[0] == 'all':
#         king = set([i for i in range(1,21)])
#     else:
#         king = set()

# 11726번 타일링
arr = [0,1,2]
n = int(input())
for i in range(3,n+1):
    arr.append()