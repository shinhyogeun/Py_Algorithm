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
# arr = [0] * 1001
# arr[1] = 1
# arr[2] = 2
# n = int(input())
# for i in range(3,1001):
#     arr[i] = arr[i-1] + arr[i-2]
# print(arr[n]%10007)

# 11727번 타일링2
# arr = [0] * 1001
# arr[1] = 1
# arr[2] = 3
# n = int(input())
# for i in range(3,1001):
#     arr[i] = arr[i-1] + 2*arr[i-2]
# print(arr[n]%10007)

# 11047번 동전0
# from collections import deque
#
# n,k = map(int,input().split())
# q = deque()
# answer = 0
# for i in range(n):
#     q.append(int(input()))
#
# while k != 0:
#     one = q.pop()
#     answer += k//one
#     k %= one
#
# print(answer)

# 10026번 적록색약
# import sys
# limit_number = 15000
# sys.setrecursionlimit(limit_number)
#
# n = int(input())
# answer = [0,0]
# arr = []
# for i in range(n):
#     arr.append(list(input()))
# arr2 = [[i if i != 'G' else 'R' for i in j] for j in arr]
#
# def dfs(arr,i,j):
#     target = arr[i][j]
#     arr[i][j] = 'X'
#     dm = [1,0,-1,0]
#     dl = [0,1,0,-1]
#     for a,b in zip(dm,dl):
#         if n > i+b >= 0 and n > j+a >= 0 and arr[i+b][j+a] == target:
#             dfs(arr,i+b,j+a)
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] in ['R','G','B']:
#             answer[0] += 1
#             dfs(arr,i,j)
#         if arr2[i][j] in ['R','B']:
#             answer[1] += 1
#             dfs(arr2, i, j)
#
# print(' '.join(map(str,answer)))

#9461번 파도반 수열
# n = int(input())
# arr = [0] * 101
# arr[1] = 1
# arr[2] = 1
# arr[3] = 1
# arr[4] = 2
# arr[5] = 2
#
# for i in range(6,101):
#     arr[i] = arr[i-1] + arr[i-5]
#
# answer = []
#
# for i in range(n):
#     answer.append(arr[int(input())])
#
# for i in answer:
#     print(i)

#11279번 최대힙
# import sys
# import heapq
#
# input = sys.stdin.readline
# n = int(input())
# arr = []
#
# for i in range(n):
#     inp = int(input())
#     if not inp:
#         if len(arr) != 0:
#             print(-heapq.heappop(arr))
#         else:
#             print(0)
#     else:
#         heapq.heappush(arr,-inp)

#11286번 절댓값 힙
# import sys
# import heapq
#
# input = sys.stdin.readline
# n = int(input())
# arr = []
#
# for i in range(n):
#     inp = int(input())
#     if not inp:
#         if len(arr) != 0:
#             print(heapq.heappop(arr)[1])
#         else:
#             print(0)
#     else:
#         heapq.heappush(arr,(abs(inp),inp))

#11399번 ATM
# n = int(input())
# arr = list(map(int,input().split()))
# arr = sorted(arr)
# answer = 0
#
# for i in range(n):
#     answer += (n-i)*arr[i]
#
# print(answer)

# 1927번 최소 힙
# import sys
# import heapq
#
# input = sys.stdin.readline
# n = int(input())
# arr = []
#
# for i in range(n):
#     inp = int(input())
#     if not inp:
#         if len(arr) != 0:
#             print(heapq.heappop(arr))
#         else:
#             print(0)
#     else:
#         heapq.heappush(arr,inp)

# 1927번 회의실 배정
# import heapq
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# answer = 0
# min = 0
# arr = []
#
# for i in range(n):
#     start,end = map(int,input().split())
#     heapq.heappush(arr,(end,start))
#
# while arr:
#     end,start = heapq.heappop(arr)
#     if min <= start:
#         answer += 1
#         min = end
# print(answer)

# 1620번 나는야 포켓몬 마스터 이다솜
# import sys
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
# arr = []
# dic = {}
# for i in range(n):
#     inp = input()[:-1]
#     arr.append(inp)
#     dic[inp] = i+1
#
# for i in range(m):
#     inp = input()[:-1]
#     if inp.isalpha():
#         print(dic[inp])
#     else:
#         print(arr[int(inp)-1])

# 11403번 경로 찾기
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 0 and arr[i][k] + arr[k][j] == 2:
#                 arr[i][j] = 1
#
# for i in arr:
#     print(' '.join(map(str,i)))

# 1992번 쿼드트리
# n = int(input())
# total = []
# answer = ''
#
# for i in range(n):
#     total.append(list(map(int,list(input()))))
#
# def dfs(l,m,n):
#     global answer
#     arr = []
#     if n == 0:
#         return
#     for i in total[l:l+n]:
#         for j in i[m:m+n]:
#             arr.append(j)
#     if len(set(arr)) == 1:
#         answer += str(arr[0])
#         return
#
#     answer += '('
#     dfs(l,m,n//2)
#     dfs(l,m+n//2,n//2)
#     dfs(l+n//2,m,n//2)
#     dfs(l+n//2,m+n//2,n//2)
#     answer += ')'
#
# dfs(0,0,n)
# print(answer)

# 2178번 미로탐색
# from collections import deque
#
# n,k = map(int,input().split())
# q = deque()
# q.append((0,0))
# total = []
#
# for i in range(n):
#     total.append(list(map(int,list(input()))))
# while q:
#     l,m = q.popleft()
#     dm = [1,0,-1,0]
#     dl = [0,1,0,-1]
#     for a,b in zip(dl,dm):
#         if n > l+a >= 0 and k > m+b >= 0 and total[l+a][m+b] == 1:
#             q.append((l+a,m+b))
#             total[l+a][m+b] = total[l][m] + 1
#
# print(total[n-1][k-1])

#2579번 계단오르기
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = [0]
# for i in range(n):
#     arr.append(int(input()))
#
# if n == 1:
#     arr[1] = [0,arr[1]]
# else:
#     arr[1] = [0, arr[1]]
#     arr[2] = [arr[2],arr[1][1] + arr[2]]
#     for i in range(3,n+1):
#         arr[i] = [max(arr[i-2])+arr[i],arr[i-1][0]+arr[i]]
#
# print(max(arr[-1]))

#1780번 종이의 개수
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
#
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#
# answer = {'0':0,'1':0,'-1':0}
#
# def dfs(l,m,n):
#     mini = []
#     if n == 0:
#         return
#     for i in arr[l:l+n]:
#         for j in i[m:m+n]:
#             mini.append(j)
#     if len(set(mini)) == 1:
#         answer[str(mini[0])] += 1
#         return
#
#     dfs(l, m, n//3)
#     dfs(l, m+n//3, n//3)
#     dfs(l, m+2*(n//3), n // 3)
#     dfs(l+n//3, m, n // 3)
#     dfs(l+n//3, m+n//3, n // 3)
#     dfs(l+n//3, m+2*(n//3), n // 3)
#     dfs(l+2*(n//3), m, n // 3)
#     dfs(l+2*(n//3), m+(n//3), n // 3)
#     dfs(l+2*(n//3), m+2*(n//3), n // 3)
#
# dfs(0,0,n)
#
# print(answer['-1'])
# print(answer['0'])
# print(answer['1'])

# 7576번 토마토
# from collections import deque
#
# n,k = map(int,input().split())
# arr = []
#
# dm = [1, 0, -1, 0]
# dl = [0, 1, 0, -1]
# q = deque()
#
# for i in range(k):
#     arr.append(list(map(int,input().split())))
#
# for i in range(k):
#     for j in range(n):
#         if arr[i][j] == 1:
#             q.append((i,j))
#
# count = -1
#
# while q:
#     count += 1
#     for i in range(len(q)):
#         l,m = q.popleft()
#         for a, b in zip(dm, dl):
#             if k > l + b >= 0 and n > m + a >= 0 and arr[l + b][m + a] == 0:
#                 arr[l+b][m+a] = 'X'
#                 q.append((l+b, m+a))
#
# total = []
#
# for i in arr:
#     for j in i:
#         total.append(j)
#
# if 0 in total:
#     print(-1)
# else:
#     print(count)

# 17219번 비밀번호찾기
# import sys
# input = sys.stdin.readline
#
#
# n,m = map(int,input().split())
# dic = {}
#
# for i in range(n):
#     home,password = input().split()
#     dic[home] = password
#
# for i in range(m):
#     print(dic[input()[:-1]])

# 17626번 Four Squares
# import math
# n = int(input())
#
# arr = [5] * (n+1)
# arr[0] = 0
# arr[1] = 1
# arr[2] = 2
# arr[3] = 3
# for i in range(3,n+1):
#     for j in range(2, math.floor(math.sqrt(i))+1):
#         arr[i] = min(arr[i],arr[i-(j**2)]+1)
# print(arr[n])

# 2606번 바이러스
# from collections import deque
#
# n = int(input())
# m = int(input())
# q = deque()
#
# checked = [False] * (n+1)
# checked[1] = True
# dic = {i+1:[] for i in range(n)}
#
# for i in range(m):
#     a,b = map(int,input().split())
#     dic[a].append(b)
#     dic[b].append(a)
#
# for i in dic[1]:
#     q.append(i)
#
# answer = 0
#
# while q:
#     to = q.popleft()
#     if checked[to] == False:
#         answer += 1
#         checked[to] = True
#         for i in dic[to]:
#             q.append(i)
#
# print(answer)

# 2630번 색종이 만들기
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# answer = [0,0]
# total = []
#
# for i in range(n):
#     total.append(list(map(int,input().split())))
#
# def dfs(l,m,n):
#     if n == 0:
#         return
#
#     target = []
#
#     for i in total[l:l+n]:
#         for j in i[m:m+n]:
#             target.append(j)
#
#     if len(set(target)) == 1:
#         answer[target[0]] += 1
#         return
#
#     dfs(l,m,n//2)
#     dfs(l,m+(n//2),n//2)
#     dfs(l+(n//2),m,n//2)
#     dfs(l+(n//2),m+(n//2),n//2)
#
# dfs(0,0,n)
#
# for i in answer:
#     print(i)

# 2667번 단지번호 붙이기
# n = int(input())
# total = []
# answer = []
#
# def dfs(l,m):
#     dm = [1,0,-1,0]
#     dl = [0,1,0,-1]
#     if total[l][m] == 1:
#         answer[-1] += 1
#         total[l][m] = 'X'
#         for a,b in zip(dl,dm):
#             if n > l+a >= 0 and n > m+b >= 0 and total[l+a][m+b] == 1:
#                 dfs(l+a,m+b)
#
# for i in range(n):
#     total.append(list(map(int,list(input()))))
#
# for i in range(n):
#     for j in range(n):
#         if total[i][j] == 1:
#             answer.append(0)
#             dfs(i,j)
#
# print(len(answer))
# for i in sorted(answer):
#     print(i)

# 5525번 IOIOI
# from collections import deque
#
# n = int(input())
# m = int(input())
# arr = deque(list(input()))
# answer = 0
# target = deque([])
# while arr:
#     added = arr.popleft()
#     if added == 'I':
#         target.append(added)
#         while len(target) != 2*n+1:
#             if len(arr) != 0 and arr[0] != target[-1]:
#                 if len(target) < 2*n:
#                     target.append(arr.popleft())
#                 else:
#                     answer += 1
#                     target.popleft()
#                     target.popleft()
#                     break
#             else:
#                 target = deque()
#                 break
#
# print(answer)

#6064번 카잉 달력
# import sys
# import math
#
# input = sys.stdin.readline
#
# n = int(input())
# answer = []
# for i in range(n):
#     a,b,one,two = map(int,input().split())
#     gcd = math.gcd(a,b)
#     end = (a * b) // gcd
#     for j in range(one,end+1,a):
#         if j%b == two or (j%b == 0 and b == two):
#             answer.append(j)
#             break
#     else:
#         answer.append(-1)
#
# for i in answer:
#     print(i)

#11659번 구간합 구하기
# import sys
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# startSum = [0,arr[0]]
# answer = []
# for i in range(2,len(arr)+1):
#     startSum.append(startSum[i-1] + arr[i-1])
#
# for i in range(m):
#     a,b = map(int,input().split())
#     answer.append(startSum[b]-startSum[a-1])
#
# for i in answer:
#     print(i)

#16928번 뱀과 사다리게임
# from collections import deque
#
# n,m = map(int,input().split())
# INF = 1e9
# total = [INF] * 101
# total[1] = 0
# up = {}
# down = {}
#
# for i in range(n):
#     a,b = map(int,input().split())
#     up[str(a)] = b
#
# for i in range(m):
#     a, b = map(int, input().split())
#     down[str(a)] = b
#
# q = deque()
# q.append(1)
#
# while q:
#     start = q.popleft()
#     for j in range(1,7):
#         if start+j <= 100 and total[start+j] > total[start] + 1:
#             total[start+j] = total[start] + 1
#             if str(start+j) in up.keys():
#                 if total[up[str(start + j)]] > total[start] + 1:
#                     total[up[str(start + j)]] = total[start] + 1
#                     q.append(up[str(start + j)])
#             elif str(start+j) in down.keys():
#                 if total[down[str(start + j)]] > total[start] + 1:
#                     total[down[str(start + j)]] = total[start] + 1
#                     q.append(down[str(start + j)])
#             else:
#                 q.append(start + j)
#
# print(total[-1])

#18870번 좌표압축
# import heapq
#
# n = int(input())
#
# total = list(map(int,input().split()))
# new = [(v,i) for i,v in enumerate(total)]
# heapq.heapify(new)
# answer = [0] * n
# count = 0
#
# a,b = heapq.heappop(new)
# pivot = a
# answer[b] = count
#
# while new:
#     v,i = heapq.heappop(new)
#     if pivot < v:
#         pivot = v
#         count += 1
#     answer[i] = count
#
# print(' '.join(map(str,answer)))

#1389번 케빈 베이컨의 6단계 법칙
# import heapq
#
# n,m = map(int,input().split())
# INF = 1e8
# total = [[INF for i in range(n)] for j in range(n)]
#
# for i in range(m):
#     a,b = map(int,input().split())
#     total[a-1][b-1] = 1
#     total[b-1][a-1] = 1
#
# for i in range(n):
#     total[i][i] = 0
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             total[i][j] = min(total[i][j],total[i][k]+total[k][j])
#
# answer = []
#
# for i,v in enumerate(total):
#     answer.append((sum(v),i+1))
#
# heapq.heapify(answer)
# aa,answer = heapq.heappop(answer)
#
# print(answer)

#1260번 DFS와 BFS
from collections import deque

n,m,v = map(int,input().split())
dic = {i+1:[] for i in range(n)}
q = deque()
q.append(v)

BFSAnswer = []
DFSAnswer = []

for i in range(m):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)
for i in dic.keys():
    dic[i] = sorted(dic[i])

def dfs(startPoint):
    if startPoint in DFSAnswer:
        return
    DFSAnswer.append(startPoint)
    for i in dic[startPoint]:
        dfs(i)
dfs(v)
print(' '.join(map(str,DFSAnswer)))

while q:
    now = q.popleft()
    if now in BFSAnswer:
        continue
    BFSAnswer.append(now)
    for i in dic[now]:
        q.append(i)
print(' '.join(map(str,BFSAnswer)))








