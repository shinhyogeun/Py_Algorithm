## 그리디 알고리즘

# 최후의 문제 1번
# length = int(input())
# arr = list(map(int,input().split()))
#
# sortedArr = sorted(arr, reverse=True)
#
# answer = 0
#
# while len(sortedArr) != 0:
#     king = sortedArr[0]
#
#     if len(sortedArr) >= king:
#         del sortedArr[:king]
#         answer = answer + 1
#         continue
#     break
#
# print(answer)


# 최후의 문제 2번

# arr = list(map(int,list(input())))
# arr.insert(0,0)
#
# answer = 0
#
# for i in range(len(arr)-1):
#     if (arr[i] in [0,1] or arr[i+1] in [0,1]):
#         answer = answer + arr[i+1]
#     else:
#         answer = answer * arr[i+1]
#
# print(answer)

# 최후의 문제 3번

# arr = list(map(int,list(input())))
#
# a = 0
# b = 0
# pivot = 2
#
# for i in arr:
#     if(pivot != i):
#         pivot = i
#         if(i == 0):
#             a += 1
#         else:
#             b += 1
# print(a if a < b else b)


# 최후의 문제 4번

# length = int(input())
#
# arr = list(map(int,input().split(" ")))
# arr.sort()
#
# answer = 1
#
# for i in arr:
#     if i <= answer:
#         answer += i
#     else:
#         break
#
# print(answer)

# 최후의 문제 5번

# length, ran = map(int,input().split())
# arr = list(map(int,input().split(" ")))
#
# filterArr = set(arr)
#
# new = {}
#
# answer = (length * (length-1)) / 2
#
# for i in filterArr:
#     new[i] = arr.count(i)
#
# for key,value in new.items():
#     if value != 1:
#         answer -= (value * (value-1)) / 2
#
# print(int(answer))

# 최후의 문제 6번

## 별로인 방법
# def solution(food_times, k):
#     where = 0
#     count = 0
#
#     while count != k+1:
#         nowIndex = where % len(food_times)
#
#         if food_times[nowIndex] != 0:
#             if (count == k):
#                 return nowIndex+1
#             food_times[nowIndex] -= 1
#             count += 1
#             where += 1
#         else:
#             if(food_times.count(0) == len(food_times)):
#                 return -1
#             else:
#                 where += 1
#
# print(solution([3,1,2],5))

# import heapq
#
# def solution(food_times,k):
#     q = []
#     if sum(food_times) <= k:
#         return -1
#
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i+1))
#
#     minus = 0
#
#     while k >= (q[0][0]-minus) * len(q):
#         length = len(q)
#         new = heapq.heappop(q)[0]
#         good = (new-minus) * length
#         minus = new
#         k -= good
#
#     return sorted(q, key=lambda x:x[1])[k % len(q)][1]
#
# print(solution([2,3,1], 5))
# print(solution([4,3,5,6,2], 7))
# print(solution([3,1,1,1,2,4,3], 12))

# 구현 피지컬

# 최후의 문제 7번
# arr = list(map(int, input()))
#
# pivot = int(len(arr)/2)
#
# a = sum(arr[:pivot])
# b = sum(arr[pivot:])
# if(a == b):
#     print("LUCKEY")
# else:
#     print("READY")


# 최후의 문제 8번

# number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
# arr = list(input())
#
# arr = sorted(arr)
#
# total = 0
# j = 0
#
# for i in range(len(arr)):
#     if arr[i-j] in number:
#         total += int(arr[i-j])
#         del arr[i-j]
#         j += 1
#     else:
#         break
#
# arr.append(str(total))
#
# print(''.join(arr))

# 최후의 문제 9번

# def parse(s,i):
#     arr = ''
#     real = s[:i]
#     count = 1
#     for j in range(1, len(s)//i+2):
#         if real == s[i*j:i*(j+1)]:
#             count += 1
#         else:
#             real = (str(count) if count > 1 else '') + real
#             arr += str(real)
#             count = 1
#             real = s[i*j:i*(j+1)]
#     return len(arr)
#
# def solution(s):
#     dic = []
#     if len(s) == 1:
#         return 1
#     for i in range(1, len(s)//2+1):
#         dic.append(parse(s,i))
#     return min(dic)

# 최후의 문제 10번
# def tilt(s):
#     length = len(s)
#     answer = [[0 for i in range(length)] for j in range(length)]
#
#     for i in range(length):
#         for j in range(length):
#             answer[j][length-1-i] = s[i][j]
#     return answer
#
# def check(total, keyLength, length):
#     for i in range(keyLength-1, length-keyLength+1):
#         for j in range(keyLength-1, length-keyLength+1):
#             if total[i][j] in [0,2]:
#                 return False
#
#     return True
#
# def insert(total,row,col,key):
#     for i in range(len(key)):
#         for j in range(len(key)):
#             total[row+i][col+j] += key[i][j]
#     return total
#
# def solution(key, lock):
#     keyLength = len(key)
#     lockLength = len(lock)
#     key2 = key
#
#     length = lockLength + 2 * (keyLength - 1)
#
#     total = [[0 for i in range(length)] for i in range(length)]
#
#     for i in range(keyLength-1, length-keyLength+1):
#         for j in range(keyLength-1, length-keyLength+1):
#             total[i][j] = lock[i-(keyLength-1)][j-(keyLength-1)]
#
#     for i in range(4):
#         key2 = tilt(key2)
#         for i in range(length-keyLength+1):
#             for j in range(length-keyLength+1):
#                 copy = [[i for i in j] for j in total]
#                 result = insert(copy, i, j, key2)
#                 if check(result,keyLength,length):
#                     return True
#
#     return False
#
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

#최후의 문제 11번
# def findTail(total):
#     return min([(total[i][j], i, j) for i in range(len(total)) for j in range(len(total)) if total[i][j] > 0])[1:]
#
# length = int(input())
# total = [[0 for i in range(length+2)] for j in range(length+2)]
#
# apples = int(input())
# for i in range(apples):
#     row,col = list(map(int,input().split(' ')))
#     total[row][col] = -1
# total[1][1] = 1
# turns = int(input())
# turnsInfo = ['X' for i in range(10001)]
# for i in range(turns):
#     time, to = list(input().split(' '))
#     turnsInfo[int(time)] = to
#
# timeCount = 0
#
# # 0,1 -> 1,0 -> 0,-1 -> -1,0
#
# tilArr = [[0,1],[1,0],[0,-1],[-1,0]]
# til = 0
# ################
# tail = [1,1]
# head = [1,1]
# ################
# while True:
#     if turnsInfo[timeCount] == 'D':
#         til = til+1 if til < 3 else 0
#     elif turnsInfo[timeCount] == 'L':
#         til = til-1 if til > 0 else 3
#
#     nextPositionRow = head[0]+tilArr[til][0]
#     nextPositionCol = head[1]+tilArr[til][1]
#
#     if total[nextPositionRow][nextPositionCol] >= 1:
#         print(timeCount+1)
#         break
#     if nextPositionRow in [0, length+1] or nextPositionCol in [0, length+1]:
#         print(timeCount+1)
#         break
#
#     if total[nextPositionRow][nextPositionCol] == -1:
#         total[nextPositionRow][nextPositionCol] = total[head[0]][head[1]]+1
#         head=[nextPositionRow, nextPositionCol]
#     else:
#         total[nextPositionRow][nextPositionCol] = total[head[0]][head[1]] + 1
#         total[tail[0]][tail[1]] = 0
#         head = [nextPositionRow, nextPositionCol]
#         tail = findTail(total)
#
#     timeCount += 1

# 최후의 문제 12번
# def isPossible(copy,canvas2):
#     canvas = [[j[:] for j in i] for i in canvas2]
#     length = len(canvas)-1
#
#     for x, y, item in copy:
#         if item == 0:
#             canvas[length-y][x].append('2-1')
#             canvas[length-y-1][x].append('2-2')
#         else:
#             canvas[length-y][x].append('1-1')
#             canvas[length-y][x+1].append('1-2')
#
#     for x, y, item in copy:
#         if item == 0:
#             if y == 0 or ('1-1' in canvas[length-y][x]) or ('2-2' in canvas[length-y][x]) or '1-2' in canvas[length-y][x]:
#                 continue
#             else:
#                 return False
#         else:
#             if '2-1' in canvas[length-y+1][x] or '2-1' in canvas[length-y+1][x+1]:
#                 continue
#             elif '1-2' in canvas[length-y][x] and '1-1' in canvas[length-y][x+1]:
#                 continue
#             else:
#                 return False
#     return True
#
# def updateResult(item, result, canvas):
#     copy = [[j for j in i] for i in result]
#     x, y, what, make = item
#
#     if make == 1:
#         copy.append([x, y, what])
#     else:
#         copy.remove([x, y, what])
#
#     if isPossible(copy,canvas):
#         return copy
#
#     return result
#
# def solution(n, build_frame):
#     canvas = [[[] for i in range(n+1)] for j in range(n+1)]
#
#     result = []
#
#     for item in build_frame:
#         result = updateResult(item, result, canvas)
#
#     return sorted(result)
#
# print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# print(solution(100,[[0,0,0,1],[0,1,0,1]]))

# 최후의 문제 13번`

# from itertools import permutations
#
# def calculateDistance(arr,homeArr):
#     answer = []
#     for home in homeArr:
#         arr2 = []
#         for chicken in arr:
#             arr2.append(abs(chicken[0]-home[0])+abs(chicken[1]-home[1]))
#         answer.append(min(arr2))
#     return sum(answer)
#
#
# length, max = list(map(int,input().split()))
#
# total = [[] for i in range(length)]
# for i in range(length):
#     total[i] = list(map(int,input().split()))
#
# homeArr = []
# chickenArr = []
#
# for i in range(length):
#     for j in range(length):
#         if(total[i][j]) == 1:
#             homeArr.append((i,j))
#         elif total[i][j] == 2:
#             chickenArr.append((i,j))
#
# answerArr = []
#
# for i in range(1,max+1):
#     arr = list(permutations(chickenArr,i))
#     for j in arr:
#         answerArr.append(calculateDistance(j,homeArr))
#
# print(min(answerArr))

## 다잌스트라

# import heapq
#
# nodes,lines = list(map(int,input().split(' ')))
# fro = int(input())
#
# INF = int(1e9)
# answers = [INF for i in range(nodes+1)]
# visited = [False for i in range(nodes+1)]
#
# kings = []
# heapq.heappush(kings,(0, fro))
# infoArr = [[] for _ in range(nodes+1)]
#
# for i in range(lines):
#     start, end, time = list(map(int, input().split(' ')))
#     infoArr[start].append([end,time])
#
# while kings:
#     answer, index = heapq.heappop(kings)
#     if visited[index]:
#         continue
#     visited[index] = True
#     answers[index] = answer
#
#     for end, time in infoArr[index]:
#         if answers[end] > answer + time:
#             answers[end] = answer + time
#             heapq.heappush(kings,(answer + time, end))
#
# for i in range(1,len(answers)):
#     print(answers[i])

# INF = int(1e9)
# company, routes = list(map(int,input().split(' ')))
# total = [[INF for i in range(company+1)] for j in range(company+1)]
#
# for i in range(1,company+1):
#     total[i][i] = 0
#
# for i in range(routes):
#     fro,to = list(map(int,input().split(' ')))
#     total[fro][to] = 1
#     total[to][fro] = 1
#
# for k in range(1,company+1):
#     for i in range(1,company+1):
#         for j in range(1,company+1):
#             total[i][j] = min(total[i][k]+total[k][j], total[i][j])
#
# x, k = list(map(int,input().split()))
#
# if INF in [total[1][k], total[k][x]]:
#     print(-1)
# else:
#     print(total[1][k]+total[k][x])

# import heapq
#
# city,tube,start = list(map(int,input().split(' ')))
#
# tubeInfo = [[] for j in range(city+1)]
#
# INF = int(1e9)
# for i in range(tube):
#     frm,to,distance = list(map(int,input().split(' ')))
#     tubeInfo[frm].append([to,distance])
#
# answers = [INF for i in range(city+1)]
# answers[start] = 0
#
# hist = []
# heapq.heappush(hist,(0,start))
#
# while hist:
#     answer, index = heapq.heappop(hist)
#
#     if answers[index] < answer:
#         continue
#
#     for to, distance in tubeInfo[index]:
#         if answers[to] > answer + distance:
#             answers[to] = answer+distance
#             heapq.heappush(hist,(answer+distance, to))
#
# print(len(answers)-answers.count(INF)-1, max([i for i in answers if i != INF]))

# l,m = list(map(int,input().split()))
#
# total = []
#
# for i in range(l):
#     total.append(list(map(int,list(input()))))
#
# answer = 0
#
# def dfs(i,j):
#     global total
#     total[i][j] = 1
#
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
#
#     for k in range(4):
#         if l-1 >= i+dy[k] >= 0 and m-1 >= j+dx[k] >= 0:
#             if total[i+dy[k]][j+dx[k]] == 0:
#                 dfs(i+dy[k], j+dx[k])
#
#
# for i in range(l):
#     for j in range(m):
#         if total[i][j] == 0:
#             answer += 1
#             dfs(i,j)
#
# print(answer)

# from collections import deque
#
# l,m = list(map(int,input().split()))
#
# total= []
#
# for i in range(l):
#     total.append(list(map(int,list(input()))))
#
# total = [[0 if j != 0 else -1 for j in i] for i in total]
# total[0][0] = 1
#
# q = deque([(0,0)])
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# while q:
#     x,y = deque.pop(q)
#     for i in range(4):
#         if l-1 >= y+dy[i] >= 0 and m-1 >= x+dx[i] >= 0:
#             if total[y+dy[i]][x+dx[i]] == 0:
#                 total[y+dy[i]][x+dx[i]] = total[y][x] + 1
#                 q.append((x+dx[i],y+dy[i]))
#
# print(total[l-1][m-1])

#4의 인덱스를 찾아라!

# def find(start,end,target,arr):
#     if start > end :
#         return '없어요'
#     pivot = start + (end-start)//2
#     if arr[pivot] > target:
#         return find(start,pivot-1,target,arr)
#     elif arr[pivot] < target:
#         return find(pivot+1, end, target, arr)
#     else:
#         return pivot

# def find(target,arr):
#     start = 0
#     end = len(arr)-1
#     while start <= end:
#         pivot = start + (end-start)//2
#         if arr[pivot] > target:
#             end = pivot-1
#         elif arr[pivot] < target:
#             start = pivot+1
#         else:
#             return pivot
#     return '없어요'
#
#
# print(find(10,[0,2,4,6,8,10,12,14,16,18]))

# how = int(input())
# total = list(map(int,input().split()))
# want = int(input())
# wantArr = list(map(int,input().split()))
#
# answer = []
#
# def find(i,total):
#     start = 0
#     end = len(total)-1
#     while start <= end:
#         pivot = start + (end-start)//2
#         if total[pivot] > i:
#             end = pivot-1
#         elif total[pivot] < i:
#             start = pivot+1
#         else:
#             return pivot
#     return None
#
# for i in wantArr:
#     if find(i,total) != None:
#         answer.append('yes')
#     else:
#         answer.append('no')
#
# print(' '.join(answer))

#
# n,m = list(map(int,input().split()))
#
# total = list(map(int,input().split()))
#
# def find(target,total):
#     start = 0
#     end = max(total)
#
#     while start <= end:
#         pivot = start + (end-start)//2
#         if sum([i-pivot for i in total if i > pivot]) < target:
#             end = pivot - 1
#         elif sum([i-pivot for i in total if i > pivot]) > target:
#             start = pivot + 1
#         else:
#             return pivot
#
#     return pivot-1
#
# print(find(m,total))

# def find_peice(table2, i, j, pivot):
#     peice = []
#
#     def dfs(table2, i, j, startY, startX):
#         x = len(table2[0]) - 1
#         y = len(table2) - 1
#
#         dx = [1, 0, -1, 0]
#         dy = [0, 1, 0, -1]
#
#         if table2[i][j] == pivot:
#             table2[i][j] = 7
#             for k in range(4):
#                 if y >= i + dy[k] >= 0 and x >= j + dx[k] >= 0:
#                     if table2[i + dy[k]][j + dx[k]] == pivot:
#                         peice.append([i + dy[k] - startY, j + dx[k] - startX])
#                         dfs(table2, i + dy[k], j + dx[k], startY, startX)
#
#         return peice
#
#     if table2[i][j] != pivot:
#         return None
#
#     peice.append([0, 0])
#
#     return dfs(table2, i, j, i, j)
#
# def tilt(game_board):
#     length = len(game_board)
#     new = [[0 for i in range(length)] for j in range(length)]
#
#     for i in range(length):
#         for j in range(length):
#             new[j][length-1-i] = game_board[i][j]
#
#     return new
#
# def solution(game_board,table):
#     table2 = table
#
#     length1 = len(game_board)
#     length2 = len(table)
#
#     peices = []
#     for i in range(length2):
#         for j in range(length2):
#             result = find_peice(table2,i,j,1)
#             if result != None:
#                 peices.append(result)
#     answer = 0
#
#     tiledTable = game_board
#     for i in range(4):
#         table1 = tilt(tiledTable)
#         tiledTable = [[i for i in j] for j in table1]
#         king = []
#         for i in range(length1):
#             for j in range(length1):
#                 result2 = find_peice(table1,i,j,0)
#                 if result2 != None:
#                     king.append(result2)
#
#         for peice in peices:
#             if peice in king:
#                 answer += len(peice)
#                 peices.remove(peice)
#
#     return answer
#
# print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))
# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
#                [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))




# def solution(inputString):
#     arr = list(inputString)
#     openTarget = ['[','<','{','(']
#     closeTarget = [']','>','}',')']
#
#     cont = 0
#     for i in arr:
#         if i in openTarget or i in closeTarget:
#             cont += 1
#
#     if cont == 0:
#         return 0
#
#     open = []
#
#     total = 0
#
#     for i in range(len(arr)):
#         if arr[i] in openTarget:
#             open.append(arr[i])
#         if arr[i] in closeTarget:
#             if open == []:
#                 return -i
#             if arr[i] != closeTarget[openTarget.index(open[-1])]:
#                 return -i
#             else:
#                 del open[-1]
#                 if open == []:
#                     total += 1
#
#     if open != []:
#         return -(len(arr)-1)
#     return total
#
# print(solution('Hello, world!'))
# print(solution('line [({<plus>)}]'))
# print(solution('line [({<plus>})'))
# print(solution('line [({<plus>)}]'))
# print(solution('x * (y + z) ^ 2 = ?'))
# import heapq
#
# def solution(array):
#     answer = []
#     new = []
#     length = len(array)
#
#     for i in range(length):
#         heapq.heappush(new, (array[i],i))
#
#     a = heapq.heappop(new)
#
#     for i in range(1,length):
#            b = heapq.heappop(new)
#
#     answer = []
#     return answer

# import heapq
#
# def find(arr,i,a):
#     new = []
#     for j in range(len(arr)):
#         if i < arr[j]:
#             heapq.heappush(new,(abs(a-j),j))
#
#     if new == []:
#         return -1
#
#     w,b = heapq.heappop(new)
#
#     return b
#
#
# def solution(array):
#     answer = []
#     a = 0
#     for i in array:
#         answer.append(find(array,i,a))
#         a+=1
#     return answer
#
# print(solution([3, 5, 4, 1, 2]))

# INF = int(1e9)

#i번째 광고를 어떤 것을 틀까? 그것을 틀었을 떄 추가되는 비용,그때의 시간,틀었던 광고를 돌려줘라!

# def calculateTime(now, ads):
#     print("ads : ",ads)
#     answer = []
#     for ad in ads:
#         startTime, cost = ad
#         king = startTime + 5 if now < startTime else now + 5
#         answer.append((
#             sum([j * (king - max(i, now)) for i, j in ads if i < king and [i,j] != ad]),
#             ad,
#             king
#         ))
#     print('answer 3: ',answer)
#     addCost, ad, now2 = min(answer)
#     return [now2, addCost,ad]
#
# def solution(ads):
#     copyedAds = [i[:] for i in ads]
#     now = 0
#     answer = 0
#
#     for i in range(len(ads)):
#         now, addCost, ad = calculateTime(now,copyedAds)
#         print(now, addCost, ad)
#         answer += addCost
#         copyedAds.remove(ad)
#
#     return answer
# print('answer :',solution([[0,3],[5,4]]))
# print('answer :',solution([[1,3],[3,2],[5,4]]))
# print('answer :',solution([[0,1],[0,2],[6,3],[8,4]]))
# print(solution([[1,3],[3,2],[5,4]]))
# print('answer :',solution([[5,2],[2,2],[6,3],[9,2]]))

# import heapq
#
# def solution(jobs):
#     copy = [i[:] for i in jobs]
#     copy2 = [i[:] for i in jobs]
#     q = []
#     time = 0
#     running = False
#     expectedTime = 0
#     result = []
#
#     while len(result) != len(jobs):
#         #지금 실행되야하는 애들을 다 뽑아라
#         dm = []
#         for startTime, length in copy:
#             if startTime <= time:
#                 heapq.heappush(q,(length, startTime))
#                 dm.append([startTime, length])
#
#         for i in dm:
#             copy.remove(i)
#
#         # 시간에 도착하면 running을 멈추자
#         if time == expectedTime:
#             running = False
#
#         # 새로운 애들을 돌려야할 때
#         if not running and q != []:
#             leng, startime = heapq.heappop(q)
#             result.append(time + leng - startime)
#             expectedTime = time + leng
#             running = True
#
#         time += 1
#     return sum(result)//len(result)
#
# print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)

# import heapq
#
# def solution(arr):
#     time = 0
#     copy = [[i,j] for i,j in arr]
#     q = []
#     total = []
#     running = False
#     expectedTime = 0
#     while len(total) != len(arr):
#         qq = []
#         if running and time == expectedTime:
#             running = False
#
#         for startTime, cost in copy:
#             if startTime == time:
#                 heapq.heappush(q,[-cost, startTime])
#                 qq.append([startTime,cost])
#
#         if qq != []:
#             for i in qq:
#                 copy.remove(i)
#
#         if not running and q != []:
#             running = True
#             minusCost, startTime = heapq.heappop(q)
#             total.append((time-startTime) * -minusCost)
#             expectedTime = time + 5
#
#         time += 1
#
#     return sum(total)
#
# print(solution([[1,10],[3,1],[5,3]]))
# print(solution([[1,3],[3,2],[5,4]]))
# print(solution([[0,3],[5,4]]))
# print(solution([[0,1],[0,2],[6,3],[8,4]]))
# print(solution([[5,2],[2,2],[6,3],[9,2]]))

# total = [0 for i in range(10001)]


# def pibo(x):
#     total[1] = 1
#     total[2] = 2
#
#     for i in range(3,x+1):
#         total[i] = total[i-1] + total[i-2]
#
#     return total[x]

# print(pibo(10000))

# def fibonachi(number):
#     if number in [1, 2]:
#         return 1
#
#     if total[number] != 0:
#         return total[number]
#
#     total[number] = fibonachi(number-1) + fibonachi(number-2)
#
#     return total[number]
#
# print(fibonachi(9))

total = [0] * 30001

total[1] = 1
total[2] = 1
total[3] = 1
total[5] = 1

def solution(number):
    cc = [number-1]
    if number in [1,2,3,5]:
        return 1

    if number % 5 == 0:
        cc.append(number // 5)
    if number % 3 == 0:
        cc.append(number // 3)
    if number % 2 == 0:
        cc.append(number // 2)

    total[number] = min([solution(i) if total[i] == 0 else total[i] for i in cc]) + 1

    return total[number]

print(solution(200))