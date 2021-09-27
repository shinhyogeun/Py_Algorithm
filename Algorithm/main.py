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

from collections import deque

def solution(enter, leave):
    answer = [0 for i in range(len(enter))]
    enter = deque(enter)
    leave = deque(leave)
    total = []
    total.append(enter.popleft())
    while leave:
        if leave[0] not in total:
            for i in total:
                answer[i-1] += 1
            total.append(enter.popleft())
            answer[total[-1]-1] = len(total)-1
        else:
            total.remove(leave.popleft())
    return answer

print(solution([1,4,2,3],[2,1,3,4]))
print(solution([1,4,2,3],[2,1,4,3]))