# 9935번 폭발문자열
# from collections import deque
#
# arr = deque(input())
# bomb = list(input())
# answer = deque()
#
# while arr:
#     answer.append(arr.popleft())
#     if answer[-1] == bomb[-1] and len(answer) >= len(bomb):
#         for i in range(2,len(bomb)+1):
#             if answer[-i] != bomb[-i]:
#                 break
#         else:
#             for i in range(len(bomb)):
#                 answer.pop()
#
# if answer == deque():
#     print('FRULA')
# else:
#     print(''.join(answer))

#2407번 조합
# n,m = map(int,input().split())
# upper = 1
# under = 1
# for i in range(0,m):
#     upper *= n-i
# for i in range(2,m+1):
#     under *= i
# print(upper//under)

#1932번 정수삼각형
# n = int(input())
# arr = []
#
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
#
# for i in range(1,n):
#     for j in range(len(arr[i])):
#         if j == 0:
#             arr[i][0] += arr[i-1][0]
#         elif j == len(arr[i])-1:
#             arr[i][-1] += arr[i-1][-1]
#         else:
#             arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])
#
# print(max(arr[-1]))

#1629번 곱셈
