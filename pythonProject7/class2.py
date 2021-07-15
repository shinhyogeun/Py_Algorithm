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

# n,m,b = map(int,input().split())
# total = []
# answerArr = []
#
# for i in range(n):
#     total.extend(list(map(int,input().split())))
#
# dic = {i:0 for i in set(total)}
#
# for i in total:
#     dic[i] += 1
#
# for i in range(min(total),max(total)+1):
#     an = b
#     time = 0
#     for j in dic.keys():
#         if j >= i:
#             time += (j-i)*dic[j]*2
#             an += (j-i)*dic[j]
#         else:
#             time += (i-j)*dic[j]
#             an -= (i-j)*dic[j]
#     if an >= 0:
#         answerArr.append((-time,i))
#
# result = sorted(answerArr,reverse=True)
#
# print(-result[0][0], result[0][1])

#15829번 Hashing
# n = int(input())
# word = list(input())
#
# answer = 0
#
# for i,v in enumerate(word):
#     answer += (ord(v) - 96)*(31**i)
#
# print(answer%1234567891)

#10845번 큐
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
#             print(mother.popleft())
#     elif n[0] == 'size':
#         print(len(mother))
#     elif n[0] == 'empty':
#         if len(mother) == 0:
#             print(1)
#         else:
#             print(0)
#     elif n[0] == 'front':
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother[0])
#     else:
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother[-1])

#10845번 덱
# from collections import deque
# import sys
# input = sys.stdin.readline
# mother = deque()
# n = int(input())
#
# for i in range(n):
#     n = list(input().split())
#     if n[0] == 'push_front':
#         mother.appendleft(n[1])
#     elif n[0] =='push_back':
#         mother.append(n[1])
#     elif n[0] =='pop_front':
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother.popleft())
#     elif n[0] =='pop_back':
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
#     elif n[0] == 'front':
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother[0])
#     else:
#         if len(mother) == 0:
#             print(-1)
#         else:
#             print(mother[-1])

#2805번 나무 자르기
# n, m = map(int,input().split())
#
# arr = [i for i in list(map(int,input().split()))]
#
# mini = 0
# maxi = max(arr)
# answer = 0
# while mini <= maxi:
#     pivot = (mini + maxi) // 2
#     target = sum([i-pivot for i in arr if i > pivot])
#     if target > m:
#         mini = pivot + 1
#         answer = pivot
#     elif target < m:
#         maxi = pivot - 1
#     else:
#         answer = pivot
#         break
#
# print(answer)

#1654번 랜선 자르기
# k,n = map(int,input().split())
# arr = []
# for i in range(k):
#     arr.append(int(input()))
#
# mini = 1
# maxi = max(arr)
#
# answer = 0
#
# while mini <= maxi:
#     pivot = (mini+maxi)//2
#     total = sum([i//pivot for i in arr])
#     if total >= n:
#         answer = pivot
#         mini = pivot+1
#     elif total < n:
#         maxi = pivot-1
#
# print(answer)

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class deque():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def at(self,index):
#         now = self.head
#         for _ in range(index):
#             if now == None:
#                 return None
#             now = now.next
#         return now.data
#
#     def max(self):
#         node = self.head
#
#         if node == None:
#             return None
#
#         maxValue = self.head.data
#
#         while node:
#             if maxValue < node.data:
#                 maxValue = node.data
#             node = node.next
#
#         return maxValue
#
#     def min(self):
#         node = self.head
#
#         if node == None:
#             return None
#
#         minValue = self.head.data
#
#         while node:
#             if minValue > node.data:
#                 minValue = node.data
#             node = node.next
#
#         return minValue
#
#     def append(self,node):
#         if self.head == None:
#             self.head = node
#             self.tail = node
#         else:
#             self.tail.next = node
#             self.tail = self.tail.next
#
#     def appendleft(self,value):
#         if self.head == None:
#             self.head = value
#             self.tail = value
#         else:
#             temp = value
#             temp.next = self.head
#             self.head = temp
#
#     def pop(self):
#         node = self.head
#         if node == None:
#             return None
#
#         while node.next.next:
#             node = node.next
#
#         answer = node.next.data
#         node.next = None
#         self.tail = node
#         return answer
#
#     def popleft(self):
#         if self.head == None:
#             return -1
#         v = self.head.data
#         self.head = self.head.next
#
#         if self.head == None:
#             self.tail = None
#
#         return v
#
#     def delete(self,data):
#         if self.head == None:
#             return None
#         if self.head.data == data:
#             temp = self.head
#             self.head = self.head.next
#             del temp
#         else:
#             node = self.head
#             while node.next:
#                 if node.next.data == data:
#                     temp = node.next
#                     node.next = node.next.next
#                     del temp
#                     return
#                 else:
#                     node = node.next
#
#     def isEmpty(self):
#         is_empty = False
#         if self.head is None:
#             is_empty = True
#         return is_empty
#
#     def isHave(self,target):
#         node = self.head
#         while node:
#             if node.data == target:
#                 return True
#             node = node.next
#         return False
#
#     def lastValue(self):
#         node = self.tail
#         if node == None:
#             return None
#
#         return node.data
#
#     def firstValue(self):
#         node = self.head
#         if node == None:
#             return None
#
#         return node.data
#
#     def length(self):
#         answer = 1
#         node = self.head
#         if node == None:
#             return 0
#         else:
#             while node != None and node.next:
#                 answer += 1
#                 node = node.next
#
#         return answer
#
#
# class heapq:
#     def __init__(self):
#         self.data = [None]
#
#     def insert(self, item):
#         self.data.append(item)
#         i = len(self.data) - 1
#         while i > 1:
#             if self.data[i] > self.data[(i // 2)]:
#                 self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
#                 i = i // 2
#             else:
#                 break
#
#     def remove(self):
#         if len(self.data) > 1:
#             self.data[1], self.data[-1] = self.data[-1], self.data[1]
#             data = self.data.pop(-1)
#             self.maxHeapify(1)
#         else:
#             data = None
#         return data
#
#     def maxHeapify(self, i):
#         left = 2 * i
#         right = (2 * i) + 1
#         smallest = i
#
#         if left < len(self.data) and self.data[i] < self.data[left]:
#             smallest = left
#
#         if right < len(self.data) and self.data[i] > self.data[right]:
#             smallest = right
#
#         if smallest != i:
#             self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
#
#             self.maxHeapify(smallest)
#
# now = heapq()
# now.insert(1)
# now.insert(3)
# now.insert(29)
# now.insert(292)
# now.insert(29123)
# # now.insert(29)
# # now.insert(29)
# print(now.remove())
# print(now.remove())
# print(now.remove())
# # print(now.remove())
# # print(now.remove())
# # print(now.remove())

# 15650번 n과 m(2)
# from itertools import combinations
#
# n, m = map(int,input().split())
#
# for i in combinations(range(1,n+1),m):
#     print(' '.join(map(str,i)))

# 15650번 n과 m(4)
# from itertools import combinations_with_replacement
#
# n, m = map(int,input().split())
#
# for i in combinations_with_replacement(range(1,n+1),m):
#     print(' '.join(map(str,i)))

# 15650번 n과 m(5)
# from itertools import permutations
#
# n, m = map(int,input().split())
# arr = sorted(list(map(int,input().split())))
#
# for i in permutations(arr,m):
#     print(' '.join(map(str,i)))

# 15650번 n과 m(8)
# from itertools import combinations_with_replacement
#
# n, m = map(int,input().split())
# arr = sorted(list(map(int,input().split())))
#
# for i in sorted(set(combinations_with_replacement(arr,m))):
#     print(' '.join(map(str,i)))

# 14938번 서강그라운드

# import heapq
#
# n,m,r = map(int,input().split())
#
# arr = list(map(int,input().split()))
# dic = {i+1:[] for i in range(n)}
# INF = 1e9
# answer = 0
#
# for i in range(r):
#     frm,to,cost = map(int,input().split())
#     dic[frm].append((to,cost))
#     dic[to].append((frm, cost))
#
# for i in dic.keys():
#     miniAnswer = 0
#     distance = [INF] * (n+1)
#     distance[i] = 0
#     q = []
#     heapq.heappush(q,(0,i))
#
#     while q:
#         nowCost,now = heapq.heappop(q)
#         if nowCost > distance[now]:
#             continue
#         for k in dic[now]:
#             if distance[k[0]] > nowCost + k[1]:
#                 distance[k[0]] = nowCost + k[1]
#                 heapq.heappush(q,(nowCost + k[1],k[0]))
#
#     for index,value in enumerate(distance):
#         if value <= m and value != INF:
#             miniAnswer += arr[index-1]
#
#     if miniAnswer > answer:
#         answer = miniAnswer
#
# print(answer)

# 17070번 파이프 옮기기1

# n = int(input())
#
# arr = []
# answerArr = []
#
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#     answerArr.append([[0,0,0] for j in range(len(arr[0]))])
#
# answerArr[0][1] = [1,0,0]
#
# for i in range(n):
#     for j in range(n):
#         if (i == 0 and j == 0) or (i == 0 and j == 1) or arr[i][j] == 1:
#             continue
#
#         one = 0
#         two = 0
#         three = 0
#
#         if n > i >= 0 and n > j-1 >= 0:
#             one = answerArr[i][j-1][0] + answerArr[i][j-1][2]
#         if n > i-1 >= 0 and n > j >= 0:
#             two = answerArr[i-1][j][1] + answerArr[i-1][j][2]
#         if n > i-1 >= 0 and n > j-1 >= 0 and arr[i-1][j] != 1 and arr[i][j-1] != 1:
#             three = sum(answerArr[i-1][j-1])
#
#         answerArr[i][j] = [one,two,three]
#
# print(sum(answerArr[n-1][n-1]))

# 11779번 최소비용 구하기 2
# import heapq
# import sys
#
# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# INF = 1e9
#
# dic = {i+1:[] for i in range(n)}
# route = {i+1:[] for i in range(n)}
#
# for i in range(m):
#     frm,to,cost = map(int,input().split())
#     dic[frm].append((to,cost))
#
# start,end = map(int,input().split())
#
# q = []
# heapq.heappush(q,(0,start))
# route[start] = [start]
#
# distance = [INF] * (n+1)
# distance[start] = 0
#
# while q:
#     cost,now = heapq.heappop(q)
#
#     if cost > distance[now]:
#         continue
#
#     for i in dic[now]:
#         if distance[now] + i[1] < distance[i[0]]:
#             distance[i[0]] = distance[now] + i[1]
#             heapq.heappush(q,(distance[now] + i[1], i[0]))
#             newRoute = route[now][:]
#             newRoute.append(i[0])
#             route[i[0]] = newRoute
#
# print(distance[end])
# print(len(route[end]))
# print(' '.join(map(str,route[end])))

# 2206번 벽 부수고 이동하기
# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# n,m = map(int,input().rstrip().split())
# arr = []
# answer = []
#
# for i in range(n):
#     a = list(map(int, list(input().rstrip())))
#     arr.append(a)
#     answer.append([[0,0] for _ in range(m)])
# q = deque()
# q.append(((0,0),False))
# answer[0][0] = [1,0]
#
# while q:
#     now,turn = q.popleft()
#     dl = [0,1,0,-1]
#     dm = [1,0,-1,0]
#
#     for i in zip(dl,dm):
#         if n > now[0] + i[0] >= 0 and m > now[1] + i[1] >= 0:
#             if arr[now[0] + i[0]][now[1] + i[1]] == 1 and not turn and answer[now[0] + i[0]][now[1] + i[1]][1] == 0:
#                 answer[now[0] + i[0]][now[1] + i[1]][1] = answer[now[0]][now[1]][0] + 1
#                 q.append(((now[0] + i[0], now[1] + i[1]), not turn))
#             elif arr[now[0] + i[0]][now[1] + i[1]] == 0:
#                 if turn and answer[now[0] + i[0]][now[1] + i[1]][1] == 0:
#                     answer[now[0] + i[0]][now[1] + i[1]][1] = answer[now[0]][now[1]][1] + 1
#                     q.append(((now[0] + i[0], now[1] + i[1]), turn))
#                 elif not turn and answer[now[0] + i[0]][now[1] + i[1]][0] == 0:
#                     answer[now[0] + i[0]][now[1] + i[1]][0] = answer[now[0]][now[1]][0] + 1
#                     q.append(((now[0] + i[0],now[1] + i[1]),turn))
#
# if answer[n-1][m-1] == [0,0]:
#     print(-1)
# else:
#     if answer[n-1][m-1][0] == 0:
#         print(answer[n-1][m-1][1])
#     elif answer[n-1][m-1][1] == 0:
#         print(answer[n-1][m-1][0])
#     else:
#         print(min(answer[n-1][m-1]))

# 1043번 거짓말

# n,m = map(int,input().split())
# trues = set(list(map(int,input().split()))[1:])
# total = []
#
# for i in range(m):
#     now = list(map(int,input().split()))[1:]
#     total.append(now)
#
# for _ in range(len(total)):
#     for i in total:
#         for j in i:
#             if j in trues:
#                 for s in i:
#                     trues.add(s)
#
# answer = 0
#
# for i in total:
#     for j in i:
#         if j in trues:
#             break
#     else:
#         answer += 1
#
# print(answer)

#1238번 파티
# import heapq
#
# n,m,x = map(int,input().split())
# dic = {i+1:[] for i in range(n)}
#
# for i in range(m):
#     frm,to,cost = map(int,input().split())
#     dic[frm].append((to,cost))
#
# lists = [i+1 for i in range(n)]
# INF = 1e9
# back = []
# go = [[]]
#
# for i in lists:
#     q = []
#     distance = [INF] * (n+1)
#     heapq.heappush(q,(0,i))
#     distance[i] = 0
#
#     while q:
#         cost,now = heapq.heappop(q)
#
#         if cost > distance[now]:
#             continue
#
#         for k in dic[now]:
#             if cost+k[1] < distance[k[0]]:
#                 distance[k[0]] = cost+k[1]
#                 heapq.heappush(q,(cost+k[1],k[0]))
#
#     if i == x:
#         back = distance[:]
#         go.append([])
#     else:
#         go.append(distance[:])
#
# answer = 0
#
# for i,v in enumerate(go):
#     if v != [] and answer < v[x] + back[i]:
#         answer = v[x] + back[i]
#
# print(answer)


# 알고리즘 3주차 과제

# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
# 
#
# class LinkedQueue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#
#     def is_empty(self):
#         if self.front == None:
#             return True
#         return False
#
#     def put(self, data):
#         if self.front == None:
#             self.front = Node(data)
#             self.rear = self.front
#         else:
#             node = self.front
#             while node.next:
#                 node = node.next
#             new = Node(data)
#             node.next = new
#             new.prev = node
#             self.rear = new
#
#     def get(self):
#         if self.front == None:
#             return None
#         returnValue = self.front
#         self.front = self.front.next
#         return returnValue.data
#
#     def peek(self):
#         if self.front == None:
#             return None
#         return self.front.data
#
# class Stack:
#     def __init__(self):
#         self.list = list()
#
#     def push(self, data):
#         self.list.append(data)
#
#     def pop(self):
#         return self.list.pop()
#
#
# class Calculator:
#     def __init__(self):
#         self.stack = Stack()
#
#     def calculate(self, string):
#         for i in string.split(' '):
#             if i in ['+', '-', '*', '/']:
#                 self.stack.push(eval(str(self.stack.pop()) + str(i) + str(self.stack.pop())))
#             elif i != ' ':
#                 self.stack.push(i)
#
#         return int(self.stack.pop())
#
#
# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#
#
# class Tree:
#     def __init__(self, root):
#         self.root = root
#
#     def preorder(self):
#         if self.root:
#             print(self.root.data)
#             king1 = self.root.left
#             king2 = self.root.right
#             if king1:
#                 self.root = king1
#                 self.preorder()
#             if king2:
#                 self.root = king2
#                 self.preorder()

# def hash_func(key):
#     return ord(key[0]) % 10
#
#
# class HashTable:
#     def __init__(self):
#         self.table = [None] * 10
#
#     def set(self, key, value):
#         self.table[hash_func(key)] = value
#
#     def get(self, key):
#         return self.table[hash_func(key)]
#
#
# class Node:
#     def __init__(self, key, data):
#         self.key = key
#         self.data = data
#         self.next = None
#
#
# class ChainedHashTable(HashTable):
#     def __init__(self):
#         self.table = [None] * 10
#
#     def set(self, key, value):
#         hash_address = hash_func(key)
#         if self.table[hash_address] != None:
#             now = self.table[hash_address]
#             while now.next:
#                 if now.key == key:
#                     now.data = value
#                     return
#                 now = now.next
#             now.next = Node(key, value)
#         else:
#             self.table[hash_address] = Node(key, value)
#
#     def get(self, key):
#         hash_address = hash_func(key)
#         if self.table[hash_address] != None:
#             now = self.table[hash_address]
#             while now:
#                 if now.key == key:
#                     return now.data
#                 now = now.next
#             return None
#         else:
#             return None


# 버블 정렬
# data_list = [1,3,4,2,3,4,5,1,2,3,4]
#
# for i in range(len(data_list)-1):
#     isSwap = False
#     for j in range(len(data_list)-i-1):
#         if data_list[j] > data_list[j+1]:
#             data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
#     if isSwap:
#         break
#
# print(data_list)

# 선택 정렬
# data_list = [1,3,4,2,3,4,5,1,2,3,4]
#
# for i in range(len(data_list)-1):
#     mini = i
#     for j in range(i+1,len(data_list)):
#         if data_list[mini] > data_list[j]:
#             mini = j
#
#     data_list[i],data_list[mini] = data_list[mini],data_list[i]
#
# print(data_list)

# 삽입정렬
def selection_sort(data):
    for i in range(1,len(data)):
        for j in range(i,0,-1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data

def func(num):
    print(num)
    if num == 1:
        return
    if num % 2 == 1:
        func(num*3+1)
    else:
        func(num//2)

func(3)


t