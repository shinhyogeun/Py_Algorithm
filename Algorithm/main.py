# 1.큰 수의 법칙(30분)(53분까지)

#내 코드

'''length, howMany, cutline = list(map(int,input().split()))
arr = list(map(int,input().split())) ; arr.sort()
cycle = howMany//(cutline+1)
recycle = howMany%(cutline+1)
print(arr[-1]*(cycle*cutline+recycle)+arr[-2]*(cycle))'''

#갓동빈 코드
'''length, howMany, cutline = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
result = 0

while True:
    for i in range(cutline):
        if howMany == 0:
            break
        result += arr[-1]
        howMany -= 1
    if howMany == 0:
        break
    result += arr[-2]
    howMany -= 1
print(result)'''



# 2.숫자 카드 게임(30분)(1시 38분까지)

'''row,col = map(int,input().split())
resultCompare = []
squre = [[0]*col for i in range(row)]
for i in range(row):
    squre[i] = list(map(int,input().split()))

for i in range(row):
    squre[i].sort()
    resultCompare.append(squre[i][0])

print(sorted(resultCompare)[-1])'''

# 3. 1이 될 때까지(30분)(2시 1분까지)
'''mother, sun = map(int,input().split())
result = 0

while True:
    if mother%sun != 0:
        mother -= 1
    elif mother%sun == 0:
        mother = mother/sun
    result += 1
    if mother == 1:
        print(result)
        break

print(1//2)'''

# 4. 상하좌우

'''squreSize = int(input())
startPoint = [1,1]
root = list(input())
for i in root:
    if i == "R":
        if startPoint[1] < squreSize:
            startPoint = [startPoint[0],startPoint[1]+1]
    elif i == "u":
        if startPoint[0] < 1:
            startPoint = [startPoint[0]-1, startPoint[1]]
    elif i == "D":
        if startPoint[0] < squreSize:
            startPoint = [startPoint[0]+1, startPoint[1]]
    elif i == "L":
        if startPoint[1] < 1:
             startPoint = [startPoint[0], startPoint[1]-1]

print(startPoint[0], startPoint[1])'''

# 4. 시각

# 내 풀이
'''a = int(input())
root = a//3
print((root*3600)+((a+1-root)*15*105))'''

#갓동빈 풀이
'''a = int(input())
count = 0

for i in range(a+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i)+str(j)+str(k):
                count += 1
print(count)'''

# 4.2 왕실의 나이트

'''a = list(input())
row = int(a[1])
col = a[0]
mother = ["a","b","c","d","e","f","g"]
numcol = mother.index(col)+1
answer = [[0]*2 for j in range(8)]
count = 0
answer[0] = [row-2,numcol-1]
answer[1] = [row-2,numcol+1]
answer[2] = [row-1,numcol-2]
answer[3] = [row+1,numcol-2]
answer[4] = [row-1,numcol+2]
answer[5] = [row+1,numcol+2]
answer[6] = [row+2,numcol-1]
answer[7] = [row+2,numcol+1]

for i in answer:
    if 1<=i[0]<=8 and 1<=i[1]<=8:
        count += 1
print(count)'''


# 4.3 게임 개발(개 어렵네..)

'''l,m = list(map(int,input().split()))
squre = [[0]*m for _ in range(l)]
nowX, nowY, nowDirection= list(map(int,input().split()))
count = 1
check = 0
for i in range(l):
    squre[i] = list(map(int,input().split()))
squre[nowX][nowY] = 9

# 그 위치에서 그 방향으로 이동가능하면 이동하고 아니면 회전해서 다시 판단하자!
def roll(startpotion,nowdirection):
    growth = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    global squre
    global check
    global count
    # 새로운 개척이 안될 때
    if squre[startpotion[0]+growth[nowdirection][0]][startpotion[1]+growth[nowdirection][1]] != 0:
        check += 1
        if check == 4:
            final(startpotion,nowdirection)
        else:
            nowdirection = nowdirection - 1 if nowdirection != 0 else 3
            roll(startpotion, nowdirection)
    # 새로운 개척이 될때
    else:
        check = 0
        count += 1
        squre[startpotion[0] + growth[nowdirection][0]][startpotion[1] + growth[nowdirection][1]] = 9
        startpotion = [startpotion[0]+growth[nowdirection][0],startpotion[1]+growth[nowdirection][1]]
        nowdirection = nowdirection - 1 if nowdirection != 0 else 3
        roll(startpotion, nowdirection)

def final(startpotion,nowdirection) :
    global check
    global count
    back = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    # 백을치기 가능할 때
    if squre[startpotion[0] + back[nowdirection][0]][startpotion[1] + back[nowdirection][1]] != 1:
        check = 0
        startpotion = [startpotion[0] + back[nowdirection][0], startpotion[1] + back[nowdirection][1]]
        roll(startpotion, nowdirection)
    # 백을치기 안될 때
    else:
        print(count)
roll([nowX,nowY],nowDirection)'''

# 민상이의 문제

'''def factorial(num):
    result = 0
    if num <= 0:
        return 0
    for i in range(num):
        result = result + (i+1)
    return result

a = int(input())
answer_arr = [0] * a
for i in range(a):
    c,d = list(map(int,input().split()))
    answer_arr[i] = d-c
t = 0
beforemove = 1
count = 1
aim = answer_arr[t]-1 # 처음에 한칸 이동한 후에 시작하는 거다.
while t < a:
    arr = []
    if aim == 0:
        print(1)
        t += 1
    else:
        candidate = [beforemove-1, beforemove, beforemove+1]
        for i in candidate:
            if (i != 0 and aim-i >= factorial(i-1)):
                arr.append(i)
        if aim - sorted(arr)[-1] != 0:
            count += 1
            beforemove = sorted(arr)[-1]
            aim = aim-sorted(arr)[-1]
        else:
            count += 1
            print(count)
            if t < a-1 : aim = answer_arr[t+1] - 1
            t += 1
            count = 1'''

# 간단한 재귀함수 표현
'''def recursive_function(i):
    if i == 100:
        return
    print(i,"번째 재귀함수에서 ", i+1,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀함수 종료")
recursive_function(1)'''

#깊이 우선탐색
#내가 하는 코드 (도중에 빡쳐서 그만 둠)
'''def dfs(startpoint):
    if check[startpoint-1] == False:
        check[startpoint-1] = True
        print(startpoint, sep=" ")
    candidate = []
    for i in graph[startpoint-1]:
        if check[i-1] == False:
            dfs(min(candidate))
    if len(candidate) > 0 :
    else:

        return
dfs(1)'''
#이쁜 코
'''graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4],
        [3, 5],
        [3, 4],
        [7],
        [6, 8],
        [1, 7],
    ]
vi = [False] * 9
def dfs2(graph,v,visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs2(graph,i,visited)

dfs2(graph,1,vi)

import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))'''


# def solution(numbers):
#     total = {i: False for i in range(10)}
#     answer = 0
#     for i in numbers:
#         if not total[i]:
#             total[i] = True
#
#     for i in total:
#         if total[i] != True: answer += i
#     return answer

# from itertools import product
#
# def solution(word):
#     total = ['A', 'E', 'I', 'O', 'U']
#     ultra = []
#     for i in range(1,6):
#         ultra += list(product(total, repeat=i))
#     ultra = sorted(ultra)
#     return ultra.index(tuple(word))+1
#
# print(solution('AAAE'))

# from collections import deque
#®
# def solution(enter, leave):
#     answer = [0 for i in range(len(enter))]
#     enter = deque(enter)
#     leave = deque(leave)
#     total = []
#     total.append(enter.popleft())
#     while leave:
#         if leave[0] not in total:
#             for i in total:
#                 answer[i-1] += 1
#             total.append(enter.popleft())
#             answer[total[-1]-1] = len(total)-1
#         else:
#             total.remove(leave.popleft())
#     return answer
#
# print(solution([1,4,2,3],[2,1,3,4]))
# print(solution([1,4,2,3],[2,1,4,3]))

# def dfs(total,i,j):
#     total[i][j] = 5
#     w = len(total[0])
#     h = len(total)
#     direction = [-1,0,1]
#     for a in direction:
#         for b in direction:
#             if (0<=i+a<h and 0<=j+b<w) and total[i+a][j+b] == 1:
#                 dfs(total,i+a,j+b)
#
#
# while True:
#      w,h = list(map(int,input().split()))
#      if w == 0 and h == 0: break
#      total = []
#      for i in range(h):
#          total.append(list(map(int,input().split())))
#      answer = 0
#      for i in range(h):
#          for j in range(w):
#              if total[i][j] == 1:
#                  answer += 1
#                  dfs(total,i,j)
#      print(answer)

# from collections import deque
#
# total = deque(list(input()))
# target = input()
# answer = 0
# now = ''
#
# while total:
#     now += total.popleft()
#     if now == target:
#         answer += 1
#         now = ''
#     elif not target.startswith(now) and len(now) > 1:
#         now = now[1:]
#     elif not target.startswith(now) and len(now) == 1:
#         now = ''
#
# print(answer)

# from collections import deque
# n = int(input())
# total = deque(map(int,input().split()))
#
# a1 = [total.popleft(), total.popleft()]
#
# while total:
#     newOne = total.popleft()
#     a2 = max(0,a1[0],newOne)
#     if a2 == 0:
#
#
# print(a2)


# total = ''.join(input().split(' '))
# if total == '12345678':
#     print('ascending')
# elif total == '87654321':
#     print('descending')
# else:
#     print('mixed')

# from itertools import combinations
#
# number, total = map(int,input().split())
# target = map(int,input().split())
# real = sorted(list([sum(i) for i in combinations(target,3)]))
# a = [i for i in real if i - total <= 0]
# if len(a) == 0:
#     print(real[-1])
# else:
#     print(a[-1])

# n = int(input())
# target = [int(input()) for i in range(n)]
# stack = []
# answer = []
#
# for i in range(1,n+1):
#     stack.append(i)
#     answer.append('+')
#     if (stack[-1] == target[0]):
#         while len(stack)!=0 and stack[-1] == target[0]:
#             stack.pop()
#             answer.append('-')
#             target.pop(0)
#
# if(len(stack)!=0):
#     print('NO')
# else:
#     for i in answer: print(i)

# n = int(input())
#
# for i in range(n):
#     length, target = map(int,input().split())
#     all = [[i,v] for v,i in enumerate(list(map(int,input().split())))]
#     count = 1
#     while all != []:
#         if all[0][0] >= max([i[0] for i in all]):
#             if(all[0][1] == target):
#                 print(count)
#                 break
#             else:
#                 all.pop(0)
#                 count += 1
#         else:
#             all.append(all.pop(0))



# import sys
#
# n = int(input())
#
# for i in range(n):
#     inputs = list(sys.stdin.readline().rstrip())
#     answerLeft = []
#     answerRight = []
#     cursor = 0
#     for i in inputs:
#         if i == '<':
#             if answerLeft != []:
#                 answerRight.append(answerLeft.pop())
#         elif i == '>':
#             if answerRight != []:
#                 answerLeft.append(answerRight.pop())
#         elif i == '-':
#             if answerLeft != []:
#                 answerLeft.pop()
#         else:
#             answerLeft.append(i)
#             cursor += 1
#     print(''.join(answerLeft)+''.join(answerRight[::-1]))

# import hashlib
#
# inp = input()
# print(hashlib.sha256(inp.encode()).hexdigest())


# n = int(input())
# total = list(map(int,input().split()))
# m = int(input())
# target = list(map(int,input().split()))
# total = sorted(total)
# answer = []
# for i in range(m):
#     start = 0
#     end = len(total)-1
#     while start <= end:
#         pivot = (start + end) // 2
#         if total[pivot] == target[i]:
#             answer.append(1)
#             break
#         elif total[pivot] > target[i]:
#             end = pivot-1
#         elif total[pivot] < target[i]:
#             start = pivot+1
#     if start > end:
#         answer.append(0)
# for i in answer:
#     print(i)

# n = int(input())
#
# for i in range(n):
#     m = int(input())
#     total = {}
#     for i in range(m):
#         frm,to = input().split()
#         total[frm] = to

# n = int(input())
# a = [[] for i in range(200)]
# for i in range(n):
#     age,name = input().split()
#     age = int(age)
#     a[age-1].append(name)
#
# for i,v in enumerate(a):
#     for j in v:
#         print(i+1 , j)


# n = int(input())
# pibo = [0,1]
#
# def pibo(a):
#     if a == 1 :
#         return 1
#     if a == 0 :
#         return 0
#     else:
#         return pibo(a - 2) + pibo(a - 1)
#
# print(pibo(n))

# N,r,c = map(int,input().split())
#
# answer = 0
#
# def find(N,r,c):
#     global answer
#     if N == 0: return
#     if 0 <= r <= 2 ** (N - 1)-1 and 0 <= c <= 2 ** (N-1)-1:
#         return find(N - 1, r, c)
#     elif 0 <= r <= 2 ** (N - 1)-1 and 2 ** (N - 1) <= c <= 2 ** (N)-1:
#         answer += 2**(2*N)/4
#         return find(N - 1, r, c - 2 ** (N - 1))
#     elif 2 ** (N - 1) <= r <= 2 ** (N)-1 and 0 <= c <= 2 ** (N - 1)-1:
#         answer += (2**(2*N)/4) * 2
#         return find(N - 1, r - 2 ** (N - 1), c)
#     elif 2 ** (N - 1) <= r <= 2 ** (N) - 1 and 2 ** (N - 1) <= c <= 2 ** (N)-1:
#         answer += (2**(2*N)/4) * 3
#         return find(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1))
#
# find(N,r,c)
# print(int(answer))


# n = int(input())
# for i in range(n):
#     arr = [i for i in range(1,int(input())+1)]
#     answer = []
#     def check(index,value):
#         global arr
#         if index == len(arr)-1 and value!= '' and (eval(value.replace(" ",""))) == 0: return answer.append(value)
#         if index == len(arr)-1: return
#         check(index+1,value+'+'+str(arr[index+1]))
#         check(index+1,value+'-'+str(arr[index+1]))
#         check(index+1,value+' '+str(arr[index+1]))
#     check(0, '1')
#     for i in sorted(answer):print(i)
#     print()

# import sys
#
# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# for i in sorted(arr):
#     print(i)


# n,k = map(int, input().split())
# arr = list(map(int,input().split()))
# print(sorted(arr)[k-1])

# total = input()
# target = input()
# answer = 0
# while total:
#     if total.startswith(target):
#         answer += 1
#         for i in range(len(target)):
#             total = total[1:]
#     else:
#         total = total[1:]
# print(answer)

# n = int(input())
# dic = {}
# for i in range(n):
#     name = input()
#     if name in dic:
#         dic[name] += 1
#     else:
#         dic[name] = 0
#
# print(sorted(dic.items(),key=lambda x:(-x[1],x[0]))[0][0])

# l, m= map(int,input().split())
# col = [False for i in range(l)]
# row = [False for i in range(m)]
# for i in range(l):
#     a = list(input())
#     for j,k in enumerate(a):
#         if k == 'X':
#             col[i] = True
#             row[j] = True
# print(max(col.count(False),row.count(False)))

# n = int(input())

# tree = {}
# for i in range(n):
#     node,frm,to = input().split()
#     tree[node] = [frm,to]
#
# answer = []

# def firstCicle(node):
#     answer.append(node)
#     if tree[node][0] != '.': firstCicle(tree[node][0])
#     if tree[node][1] != '.': firstCicle(tree[node][1])

# def middleCicle(node):
#     if tree[node][0] != '.': middleCicle(tree[node][0])
#     answer.append(node)
#     if tree[node][1] != '.': middleCicle(tree[node][1])

# def endCicle(node):
#     if tree[node][0] != '.': endCicle(tree[node][0])
#     if tree[node][1] != '.': endCicle(tree[node][1])
#     answer.append(node)

# firstCicle('A')
# print(''.join(answer))
# answer = []
# middleCicle('A')
# print(''.join(answer))
# answer = []
# endCicle('A')
# print(''.join(answer))
# answer = []

# import heapq
# import sys
#
# heap = []
# n = int(sys.stdin.readline())

# for i in range(n):
#     inp = int(sys.stdin.readline())
#     if inp == 0:
#         if len(heap) != 0:
#             print(heapq.heappop(heap))
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, inp)

# import heapq
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# total = []
# for i in range(n):
#     heapq.heappush(total,int(input()))
#
# if len(total) == 1: print(0)
# elif len(total) == 2: print(sum(total))
# else:
#     answer = 0
#     while len(total)!= 1:
#         now = heapq.heappop(total) + heapq.heappop(total)
#         answer += now
#         heapq.heappush(total,now)
#     print(answer)

# from collections import deque
#
# n, m = map(int,input().split())
# dic = {i:[] for i in range(1,n+1)}
# weight = []
#
# for i in range(m):
#     frm,to,cost = map(int,input().split())
#     weight.append(cost)
#     dic[frm].append([to,cost])
#     dic[to].append([frm, cost])
#
# weight = sorted(list(set(weight)))
# start,end = map(int,input().split())
#
# a = weight[0]
# b = weight[-1]
# answer = 0
#
# while a <= b:
#     pivot = (a + b) // 2
#     newDic = {}
#     for i in dic:
#         newDic[i] = []
#         for j in dic[i]:
#             if j[1] >= pivot:
#                 newDic[i].append(j)
#     queue = deque()
#     queue.append(start)
#     visited = []
#     isPossible = False
#     while queue:
#         now = queue.popleft()
#         if now not in visited:
#             visited.append(now)
#             for i in newDic[now]:
#                 queue.append(i[0])
#         if end in visited:
#             answer = pivot
#             isPossible = True
#             break
#     if isPossible: a = pivot+1
#     else: b = pivot-1
#
# print(answer)

# from bisect import bisect_left, bisect_right
# nums = [0,10,20,30,40,50,60,70,80,90]
# n = 90
# print(bisect_left(nums, n))
# print(bisect_right(nums, n))

# import sys
# from bisect import bisect_left
#
# input = sys.stdin.readline
#
# n,m = map(int,input().split())
# house = []
# for i in range(n): house.append(int(input()))
# house = sorted(house)
#
# start = 1
# end = house[-1]
# answer = 0
#
# while start <= end:
#     pivot = (start+end)//2
#     count = 1
#     now = house[0]
#     isPossible = False
#
#     while bisect_left(house,now + pivot) != len(house):
#         count += 1
#         if count == m :
#             isPossible = True
#             break
#         now = house[bisect_left(house,now + pivot)]
#
#     if isPossible:
#         answer = pivot
#         start = pivot+1
#     else:
#         end = pivot-1
#
# print(answer)


# n = int(input())
# answer = 0
# a = 0
# i = 1
#
# while n != 0:
#     if i > n :
#         i = 1
#     elif i == n:
#         answer += 1
#         break
#     else:
#         answer += 1
#         n -= i
#         i += 1
#
# print(answer)

# n = int(input())
# answer = []
#
# for i in range(n):  answer.append(int(input()))
#
# max = answer[0]
# max2 = answer[-1]
# a = 1
# b = 1
#
# for i in answer[1:]:
#     if i > max:
#         a += 1
#         max = i
#
# for i in answer[::-1][1:]:
#     if i > max2:
#         b += 1
#         max2 = i
#
#
# print(a)
# print(b)

# for i in range(10):
#     print('asd')

# n = int(input())
# a = [1,2,3]
# count = 3
# if n <= 3:
#     print(a[n-1])
# else:
#     while len(a) != n:
#         a.append((a[-3]+2*a[-2])%15746)
#     print(a[-1])

# n = int(input())
# arr = list(map(int,input().split()))
# answer = []
#
# for i in range(len(arr)):
#     target = [k for k in range(len(arr[:i])) if arr[k] < arr[i]]
#     if target != []:
#         answer.append(max([answer[i] for i in target])+1)
#     else:
#         answer.append(1)
# print(max(answer))

# from collections import deque
#
# N,S,M = map(int,input().split())
# volume = list(map(int,input().split()))
# possible = deque([[]])
#
# if M >= S - volume[0] >= 0: possible[0].append(S - volume[0])
# if M >= S + volume[0] >= 0: possible[0].append(S + volume[0])
#
# a = True
# for i in range(1,N):
#     added = []
#     for j in possible[0]:
#         if M >= j + volume[i] >= 0 and j + volume[i] not in added :
#             added.append(j + volume[i])
#         if M >= j - volume[i] >= 0 and j - volume[i] not in added:
#             added.append(j - volume[i])
#     if added == []: break
#     possible.popleft()
#     possible.append(added)
# else:
#     if possible[0] != []:
#         print(max(possible[0]))
#     else:
#         print(-1)
#     a = False
# if a:
#     print(-1)


# 로또의 최고 순위와 최저 순위
# def solution(lottos, win_nums):
#     count = 0
#     zeroCount = 0
#     for i in lottos:
#         if i in win_nums: count += 1
#         elif i == 0: zeroCount += 1
#     if count == 0:
#         if zeroCount <= 1: return [6, 6]
#         else: return [6-zeroCount+1, 6]
#     elif count == 1:
#         if zeroCount == 0: return [6, 6]
#         else: return [6-zeroCount, 6]
#
#     else:
#         return [6-zeroCount-count+1, 6-count+1]

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


# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if signs[i] == False:
#             answer -= absolutes[i]
#         else:
#             answer += absolutes[i]
#     return answer

# from collections import deque
#
# totalCount, targetCount = map(int,input().split())
#
# targets = list(map(int,input().split()))
# total = deque([i for i in range(1,totalCount+1)])
# [1,2,3,4,5]
#
# answer = 0
#

# 회전하는 큐(1021)
# for i in targets:
#     frontCount = 0
#     for k in total:
#         if k == i:
#             break
#         else:
#             frontCount += 1
#     backCount = len(total)-frontCount
#     if frontCount < backCount:
#         while total[0] != i:
#             total.append(total.popleft())
#             answer += 1
#     else:
#         while total[0] != i:
#             total.appendleft(total.pop())
#             answer += 1
#     total.popleft()
# print(answer)


# 분수찾기 (브론즈1) 1193번
# n = int(input())
# k = 0
# while (k*(k+1))/2 <= n:
#     k += 1
# under = k-1
#
# i = 0
# while k*(k-1)/2 + i != n:
#     i += 1
#
# if (i == 0):
#     if (((k-1) % 2) == 0):
#         print(k - 1, '/', 1, sep='')
#     else:
#         print(1, '/', k - 1, sep='')
# else:
#     if (((k - 1) % 2) == 0):
#         print(k - i + 1, '/', i, sep='')
#     else:
#         print(i, '/', k + 1 - i, sep='')

# 소트인사이드 (실버5) 1427번

# total = list(map(int,list(input())))
# total = sorted(total,reverse=True)
# print(''.join(map(str,total)))


# 늑대와 양 (실버3) 16956번
# from collections import deque
#
# r,c = map(int,input().split())
# total = []
#
# for i in range(r):
#     total.append(list(input()))
#
# q = deque([])
# for i in range(r):
#     for j in range(c):
#         if total[i][j] == '.':
#             total[i][j] = 'D'
#         if total[i][j] == 'W':
#             q.append([i,j])
#
# possible = 1
# while q:
#     i,j = q.popleft()
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     for k in range(4):
#         if 0 <= i+dx[k] < r and 0 <= j+dy[k] < c and (total[i+dx[k]][j+dy[k]] == 'S'):
#             possible = 0
#
# if possible == 1:
#     print(possible)
#     for i in total:
#         print(''.join(i))
# else:
#     print(possible)


# 알파벳
# from collections import deque

# r,c = map(int,input().split())
# total = []
# for i in range(r):
#     total.append(list(input()))
# answer = 0
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# newAcc = [total[0][0]]
#
# def check():
#     global answer
#     q = set()
#     q.add((0,0,total[0][0]))
#     while q:
#         x,y,route = q.pop()
#         if len(route) > answer :
#             answer = len(route)
#
#         for i in range(4):
#             if 0 <= x+dx[i] < r and 0 <= y+dy[i] < c:
#                 if total[x+dx[i]][y+dy[i]] not in route:
#                     q.add((x+dx[i], y+dy[i], route + total[x+dx[i]][y+dy[i]]))
# check()
# print(answer)

# 주사위 4개 브론즈2 2484번
# n =  int(input())
# total = []
# for i in range(n):
#     total.append(list(map(int,input().split())))
# answer = []
#
# def countSameNumber(arr):
#     a = [0,0]
#     for i in arr:
#         if arr.count(i) > a[1]:
#             a = [i,arr.count(i)]
#     return a
#
# for i in total:
#     setedList = set(i)
#     if len(setedList) == 1:
#         answer.append(50000 + list(setedList)[0]*5000)
#     elif len(setedList) == 2 and countSameNumber(i)[1] == 3:
#         answer.append(10000 + countSameNumber(i)[0] * 1000)
#     elif len(setedList) == 2 and countSameNumber(i)[1] == 2:
#         answer.append(2000 +  list(setedList)[0] * 500 +  list(setedList)[1] * 500)
#     elif len(setedList) == 3:
#         answer.append(1000 + countSameNumber(i)[0] * 100)
#     elif len(setedList) == 4 :
#         answer.append(max(setedList)*100)
# print(max(answer))

# 꽃길 실버2 14620번
# from itertools import combinations
#
# n = int(input())
# total = []
# for i in range(n):
#     total.append(list(map(int,input().split())))
# answer = []
# target = []
#
# def possible(arr):
#     z = []
#     dx = [-1, 0, 1, 0, 0]
#     dy = [0, 1, 0, -1, 0]
#     for i in arr:
#         for a in range(5):
#             z.append((i[0]+dx[a],i[1]+dy[a]))
#     if(len(set(z)) == len(z)):
#         return sum([total[i[0]][i[1]] for i in z])
#     return -1
#
# for i in range(1,n-1):
#     for j in range(1,n-1):
#         target.append([i,j])
#

# for i in list(combinations(target,3)):
#     possi = possible(i)
#     if (possi != -1): answer.append(possi)
#
# print(min(answer))

# 생일 5635 실버 5
# n = int(input())
# total = []
# for i in range(n):
#     a = list(input().split())
#     a[1] = int(a[1])
#     a[2] = int(a[2])
#     a[3] = int(a[3])
#     total.append(list(reversed(a)))
# total = sorted(total)
# print(total[-1][3])
# print(total[0][3])



#나이트의 이동 7562번 실버2
# from collections import deque
#
# n = int(input())
#
# for i in range(n):
#     a = int(input())
#     total = [[False for k in range(a)] for j in range(a)]
#     now = list(map(int,input().split()))
#     target = list(map(int, input().split()))
#     q = deque([])
#     q.append([now[0],now[1],0])
#     total[now[0]][now[1]] = True
#     direction = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]
#
#     while q:
#         x,y,count = q.popleft()
#         if [x, y] == target:
#             print(count)
#             break
#
#         for i in direction:
#             if 0 <= x + i[0] < a and 0 <= y + i[1] < a and total[x + i[0]][y + i[1]] == False:
#                 total[x + i[0]][y + i[1]] = True
#                 q.append([x + i[0],y + i[1],count+1])

# 다이얼 브론즈2
total = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = list(input())
number = []
for i in word:
    for j in range(len(total)):
        if i in total[j]:
            number.append(2+j)
print(sum(number)+len(number))