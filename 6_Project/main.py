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

# total = [0] * 30001
#
# total[1] = 0
# total[2] = 1
# total[3] = 1
# total[5] = 1
#
# def solution(number):
#     for i in range(2,number+1):
#         cc = [total[i-1]]
#
#         if i % 5 == 0:
#             cc.append(total[i // 5])
#         if i % 3 == 0:
#             cc.append(total[i // 3])
#         if i % 2 == 0:
#             cc.append(total[i // 2])
#
#         total[i] = min(cc) + 1
#
#     return total[number]
#
# print(solution(30000))


# def solution(number):
#     cc = [number-1]
#     if number in [1,2,3,5]:
#         return 1
#
#     if number % 5 == 0:
#         cc.append(number // 5)
#     if number % 3 == 0:
#         cc.append(number // 3)
#     if number % 2 == 0:
#         cc.append(number // 2)
#
#     total[number] = min([solution(i) if total[i] == 0 else total[i] for i in cc]) + 1
#
#     return total[number]
#
# print(solution(200))


# count = int(input())
#
# arr = list(map(int,input().split()))
#
# total = [0 for i in range(count+1)]
#
# total[1] = arr[0]
# total[2] = max(arr[0],arr[1])
# total[3] = max(arr[0]+arr[2], arr[1])
#
# for i in range(4,count+1):
#     total[i] = max(total[i-2] + arr[i-1], total[i-3] + arr[i-2])
#
# print(total[count])

# n, target = list(map(int,input().split()))
# arr = []
#
# for i in range(n):
#     arr.append(int(input()))
#
# total = [1e9] * 10001
#
# for i in arr:
#     total[i] = 1
#
# for i in range(1, target+1):
#     if i not in arr:
#         aa = [total[i-j] for j in arr if i-j > 0]
#         if aa != []:
#             total[i] = min([total[i-j] for j in arr if i-j > 0]) + 1
#
# print(total[target] if total[target] < 1e9 else -1)


# def solution(n,horizontal):
#     total = [[0 for i in range(n)] for i in range(n)]
#     now = [0,0]
#
#     def goTiltUp(now, total):
#         length = len(total)-1
#
#         if now == [length, length]: return
#
#         if now[0] == 0:
#             total[now[0]][now[1] + 1] = total[now[0]][now[1]] + 1
#             now = [now[0], now[1] + 1]
#             goTiltDown(now,total)
#         elif now[1] == length:
#             total[now[0] + 1][now[1]] = total[now[0]][now[1]] + 1
#             now = [now[0] + 1, now[1]]
#             goTiltDown(now, total)
#         else:
#             total[now[0] - 1][now[1] + 1] = total[now[0]][now[1]] + 2
#             now = [now[0] - 1, now[1] + 1]
#             goTiltUp(now, total)
#
#     def goTiltDown(now, total):
#         length = len(total)-1
#
#         if now == [length,length]: return
#
#         if now[0] == length:
#             total[now[0]][now[1] + 1] = total[now[0]][now[1]] + 1
#             now = [now[0], now[1] + 1]
#             goTiltUp(now, total)
#         elif now[1] == 0:
#             total[now[0] + 1][now[1]] = total[now[0]][now[1]] + 1
#             now = [now[0] + 1, now[1]]
#             goTiltUp(now,total)
#         else:
#             total[now[0] + 1][now[1] - 1] = total[now[0]][now[1]] + 2
#             now = [now[0] + 1, now[1] - 1]
#             goTiltDown(now, total)
#
#     if horizontal:
#         goTiltUp(now,total)
#     else:
#         goTiltDown(now,total)
#
#     return total
#
# print('answer: ',solution(4,True))
# print('answer: ',solution(5,False))

# length = int(input())
#
# arr = list(map(int,input().split()))
#
# def find(total):
#     start = 0
#     end = len(total)-1
#
#     while start <= end:
#         pivot = (start + end) // 2
#         if total[pivot] < pivot :
#             start = pivot+1
#         elif total[pivot] > pivot:
#             end = pivot-1
#
#         if total[pivot] == pivot:
#             return pivot
#
# print(find(arr))

# from itertools import combinations
#
# n = int(input())
#
# total = []
#
# for i in range(n):
#     total.append(input().split())
#
# def find(what):
#     box = []
#     for i in range(n):
#         for j in range(n):
#             if total[i][j] == what:
#                 box.append([i,j])
#     return box
#
# teachers = find('T'); students = find('S'); remains = find('X')
#
# def solution():
#     for i in list(combinations(remains, 3)):
#         total2 = [[i for i in j] for j in total]
#         def colDFS(l, m, checkmark):
#             total2[l][m] = 'T'+checkmark
#             for k in [-1, 1]:
#                 if n-1 >= l + k >= 0 and total2[l + k][m] not in ['O', 'T'+checkmark]:
#                     colDFS(l + k, m, checkmark)
#
#         def rowDFS(l, m, checkmark):
#             total2[l][m] = 'T' + checkmark
#             for k in [-1, 1]:
#                 if n-1 >= m+k >= 0 and total2[l][m + k] not in ['O', 'T'+checkmark]:
#                     rowDFS(l, m + k, checkmark)
#
#         for j in i:
#             total2[j[0]][j[1]] = 'O'
#
#         for teacher in teachers:
#             colDFS(teacher[0], teacher[1], ''.join(list(map(str,teacher))))
#             rowDFS(teacher[0], teacher[1], ''.join(list(map(str,teacher))))
#
#         count = 0
#         for i in range(n):
#             for j in range(n):
#                 if total2[i][j] == 'S':
#                     count += 1
#
#         if count == len(students):
#             for i in total2:
#                 print(i)
#             print()
#             return 'YES'
#
#     return 'NO'
#
# print(solution())

# t = int(input())
#
# answer = []
# for i in range(t):
#     n, m = list(map(int,input().split()))
#     flatArr = list(map(int,input().split()))
#     arr2 = []
#     arr = []
#     for i in range(n):
#         arr2.append(flatArr[m*i:m*(i+1)])
#
#     for j in range(m):
#         arr.append([i[j] for i in arr2])
#
#     total = [arr[0]]
#
#     for i in range(m-1):
#         added = []
#         for j in range(n):
#             if j == 0:
#                 added.append(arr[i+1][j] + max(total[i][j],total[i][j+1]))
#             elif j == n-1:
#                 added.append(arr[i+1][j] + max(total[i][j],total[i][j-1]))
#             else:
#                 added.append(arr[i+1][j] + max(total[i][j],total[i][j+1],total[i][j-1]))
#         total.append(added)
#
#     answer.append(max(total[m-1]))
#
# for i in answer:
#     print(i)

# n = int(input())
#
# arr = []
#
# for i in range(n):
#     arr.append(list(map(int,input().split())))
#
# total = [arr[0]]
#
# for i in range(1, n):
#     length = len(arr[i])
#     added = []
#     for j in range(length):
#         if j == 0:
#             added.append(total[i-1][j] + arr[i][j])
#         elif j == length-1:
#             added.append(total[i-1][j-1] + arr[i][j])
#         else:
#             added.append(max(total[i-1][j-1],total[i-1][j]) + arr[i][j])
#
#     total.append(added)
#
# print(max(total[n-1]))

# import heapq
#
# node,line = list(map(int,input().split()))
# start = int(input())
# INF = 1e9
#
# answers = [INF] * (node+1)
#
# q = []
#
# heapq.heappush(q,(0, start))
#
# info = [[] for i in range(node+1)]
#
# for i in range(line):
#     frm,to,cost = list(map(int,input().split()))
#     info[frm].append((to,cost))
#
# while q:
#     answer, index = heapq.heappop(q)
#     if answers[index] < answer:
#         continue
#     answers[index] = answer
#     for to, cost in info[index]:
#         if answers[to] > answers[index] + cost:
#             answers[to] = answers[index] + cost
#             heapq.heappush(q,(answers[to], to))
#
# for i in answers:
#     print(i)

# n = int(input())
#
# total = [[]]
#
# for i in range(n):
#     total.append(list(map(int,input().split())))
#
# answer = [0 for i in range(n+1)]
#
# # Day까지 벌수 있는 최대 돈
# for day in range(1, n+1):
#     interval, cost = total[day]
#     if day + interval - 1 <= n:
#         if answer[day + interval - 1] < answer[day - 1] + cost:
#             answer[day + interval - 1] = answer[day - 1] + cost
#         if answer[day] < answer[day - 1]:
#             answer[day] = answer[day - 1]
#
# print(max(answer))



# def solution(s):
#     number = ['zero','one','two','three','four','five','six','seven','eight','nine']
#     real = ['0','1','2','3','4','5','6','7','8','9']
#     arr = list(s)
#     em = []
#     answer = []
#     for i in range(len(arr)):
#         if arr[i] not in real:
#             em.append(arr[i])
#             if ''.join(em) in number:
#                 answer.append(str(number.index(''.join(em))))
#                 em = []
#         else:
#             answer.append(arr[i])
#     aa = ''.join(answer)
#     return int(aa)
#
#
# print(solution("one4seveneight"))

# from itertools import combinations
#
# def solution(places):
#     answer = []
#     for place in places:
#         PArr = []
#         for i in range(len(place)):
#             for j in range(len(place)):
#                 if place[i][j] == 'P':
#                  PArr.append((i,j))
#
#         allCombi = list(combinations(PArr,2))
#
#         result = 1
#
#         for combi in allCombi:
#             a,b = combi
#             if abs(a[0]-b[0]) + abs(a[1]-b[1]) > 2:
#                 continue
#
#             if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1:
#                 result = 0
#                 break
#
#             if abs(a[0]-b[0]) + abs(a[1]-b[1]) == 2:
#                 if a[0] == b[0] or a[1] == b[1]:
#                     if a[0] == b[0]:
#                         if a[1] > b[1]:
#                             if place[a[0]][a[1]-1] != 'X':
#                                 result = 0
#                                 break
#                         else:
#                             if place[a[0]][a[1]+1] != 'X':
#                                 result = 0
#                                 break
#                     if a[1] == b[1]:
#                         if a[0] > b[0]:
#                             if place[a[0]-1][a[1]] != 'X':
#                                 result = 0
#                                 break
#                         else:
#                             if place[a[0]+1][a[1]] != 'X':
#                                 result = 0
#                                 break
#                 else:
#                     if a[1] < b[1]:
#                         if a[0] < b[0]:
#                             if place[a[0]+1][a[1]] != 'X' or place[a[0]][a[1]+1] != 'X':
#                                 result = 0
#                                 break
#                         else:
#                             if place[a[0]-1][a[1]] != 'X' or place[a[0]][a[1]+1] != 'X':
#                                 result = 0
#                                 break
#                     else:
#                         if a[0] < b[0]:
#                             if place[a[0]][a[1]-1] != 'X' or place[a[0]+1][a[1]] != 'X':
#                                 result = 0
#                                 break
#                         else:
#                             if place[a[0]-1][a[1]] != 'X' or place[a[0]][a[1]-1] != 'X':
#                                 result = 0
#                                 break
#         answer.append(result)
#     return answer
#
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))



# import heapq
#
# def solution(n, start, end, roads, traps):
#     INF = 1e9
#
#     answers = [INF] * (n+1)
#
#     q = []
#
#     heapq.heappush(q,(0, start))
#
#     info = [[] for i in range(n+1)]
#
#     for road in roads:
#         frm,to,cost = road
#         info[frm].append((to, cost))
#
#     reverse = [[] for i in range(n + 1)]
#     for one in range(n + 1):
#         for to, cost in info[one]:
#             reverse[to].append((one, cost))
#
#     while q:
#         answer, index = heapq.heappop(q)
#         if index in traps:
#             if answers[index] < answer:
#                 new = [[] for i in range(n + 1)]
#                 for one in range(n+1):
#                     for to,cost in info[one]:
#                         new[to].append((one,cost))
#                 info = new
#                 for to, cost in info[index]:
#                     if answers[to] > answers[index] + cost:
#                         answers[to] = answers[index] + cost
#                         heapq.heappush(q, (answers[to], to))
#             else:
#                 new = [[] for i in range(n+1)]
#                 for one in range(n+1):
#                     for to,cost in info[one]:
#                         new[to].append((one,cost))
#                 info = new
#                 answers[index] = answer
#             for to, cost in info[index]:
#                 if answers[to] > answers[index] + cost:
#                     answers[to] = answers[index] + cost
#                     heapq.heappush(q, (answers[to], to))
#         else:
#             if answers[index] < answer:
#                 continue
#             answers[index] = answer
#             for to, cost in info[index]:
#                 if answers[to] > answers[index] + cost:
#                     answers[to] = answers[index] + cost
#                     heapq.heappush(q,(answers[to], to))
#
#     return answers[end]
#
# # print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
# print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	,[2,3]))
# a = [1,2,3,4]
# del a[-1]
# print(a)
# def solution(n, k, cmd):
#     total = [str(i) for i in range(n)]
#     print(total)
#     deletedArr = []
#     now = k
#
#     for order in cmd:
#         if order == 'C':
#             deletedArr.append(total[now])
#             del total[now]
#             if now == len(total):
#                 now -= 1
#         elif order == 'Z':
#             total.insert(int(deletedArr[-1]), deletedArr[-1])
#             if int(deletedArr[-1]) <= now:
#                 now += 1
#             del deletedArr[-1]
#         else:
#             wher, number = order.split()
#             if wher == 'D':
#                 now += int(number)
#             else:
#                 now -= int(number)
#
#     answer = ['O'] * n
#     for i in deletedArr:
#         answer[int(i)] = 'X'
#
#     return ''.join(answer)

# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(5,1,["C","Z","C","C","C","Z","Z","Z"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

# def solution(code, day, data):
#     answer = []
#     new = []
#     for dat in data:
#         price, code2, time = dat.split(' ')
#         a, exactCode = code2.split('=')
#         b, exactTime = time.split('=')
#         c, exactPrice = price.split('=')
#         new.append([exactPrice,exactCode,int(exactTime)])
#         new = sorted(new,key=lambda x:x[2])
#     for dat in new:
#         price, code2, time = dat
#         if code == code2 and str(time)[:8] == day:
#             answer.append(int(price))
#
#     return answer
#
# print(solution("012345",'20190620',["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))


# import heapq
#
# def solution(t, r):
#     total = []
#     for i in range(len(t)):
#         total.append([r[i],t[i],i])
#     now = 0
#     q = []
#     answer = []
#     while len(answer) != len(t):
#         for i in total:
#             if i[1] == now:
#                 heapq.heappush(q,i)
#
#         if q != []:
#             ridePoeple = heapq.heappop(q)
#             answer.append(ridePoeple[2])
#         now += 1
#     return answer
#
# print(solution([0,1,3,0],[0,1,2,3]))
# print(solution([7,6,8,1],[0,1,2,3]))

# def calculate(maps,p,r,i,j):
#     count = 0
#     king = r//2 - 1
#     what = []
#     for a in range(-king,king):
#         for b in range(-king,king):
#             if a == -king and b in [-king,king-1]:
#                 continue
#             if b == -king and a in [-king, king-1]:
#                 continue
#             if a ==king-1 and b == king-1:
#                 continue
#
#             if len(maps) > i+a >=0 and len(maps) > j+b >=0:
#                 if maps[i+a][j+b] <= p:
#
#                     what.append([maps[i+a][j+b]])
#                     count += 1
#
#         for j in range(king):
#             if maps[j+(r//2 - 2)-j][i-r//2] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2)-king - i][i-r//2 + i] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2)-king - king][i-r//2 + king+i] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2)-king - king + i][i-r//2 + king + king + i] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2)-king + i][i-r//2 + king + king + king] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2) + i][i-r//2 + king + king + king - i] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2) + king][i-r//2 + king + king-i] <= p/2:
#                 count += 1
#         for i in range(king):
#             if maps[j+(r//2 - 2) + king - i][i-r//2 + king - i] <= p/2:
#                 count += 1
#
#         return count
#
#     return what
# print(calculate([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],19,6,1,1))
# def solution(maps, p, r):
#     answer = []
#     for i in range(len(maps)+1):
#         for j in range(len(maps)+1):
#             answer.append(calculate(maps,p,r,i,j))
#     return max(answer)

# from itertools import combinations
#
# def solution(orders,course):
#     answer = []
#     news = []
#     for order in orders:
#         for j in order:
#             news.append(j)
#     news = sorted(list(set(news)))
#
#     real = []
#
#     for new in news:
#         count = 0
#         for order in orders:
#             if new in order:
#                 count += 1
#         if count >= 2 :
#             real.append(new)
#
#     for i in course:
#         totaldic = {}
#
#         for order in orders:
#             target = ''
#
#             for one in order:
#                 if one in real:
#                     target += one
#
#             oneTotal = combinations(target,i)
#
#             for one in oneTotal:
#                 if ''.join(sorted(one)) in  totaldic.keys():
#                     totaldic[''.join(sorted(one))] += 1
#                 else:
#                     totaldic[''.join(sorted(one))] = 1
#
#             result = sorted([(totaldic[one], one) for one in totaldic if totaldic[one] >= 2],reverse=True)
#
#
#         if result != []:
#             big = result[0][0]
#             for j in result:
#                 if j[0] == big and big >= 2:
#                     answer.append(j[1])
#
#     return sorted(answer)




# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

# from itertools import permutations
#
# def solution(expression):
#     number = []
#     pri = []
#     buket = []
#
#     answer = []
#     for i in expression:
#         if i in ['*','+','-']:
#             number.append(int(''.join(buket)))
#             buket = []
#             pri.append(i)
#         else:
#             buket.append(i)
#     number.append(int(''.join(buket)))
#
#     print(number, pri, buket)
#     for oper in permutations(['*','+','-'],3):
#         count = 'start'
#         for op in oper:
#             for index in range(len(pri)):
#                 if pri[index] == op:
#                     if count == 'start':
#                         count = number[index]
#                     if op == '*':
#                         count *= number[index + 1]
#                     elif op == '+':
#                         count += number[index + 1]
#                     else:
#                         count -=  number[index + 1]
#
#         answer.append(abs(count))
#
#     return max(answer)
#
# print(solution('100-200*300-500+20'))

# import datetime
#
# def solution(lines):
#     total = []
#     answer = []
#
#     for line in lines:
#         convertedLine = ' '.join(line.split(' ')[:2])
#         length = float(line.split(' ')[2].replace('s',''))*1000-1
#         convertedLine = datetime.datetime.strptime(convertedLine,"%Y-%m-%d %H:%M:%S.%f")
#         total.append([convertedLine - datetime.timedelta(milliseconds=length), convertedLine])
#
#     for startTime, endTime in total:
#         interval1 = [startTime, startTime + datetime.timedelta(milliseconds=999)]
#         interval2 = [endTime, endTime + datetime.timedelta(milliseconds=999)]
#
#         vs = [0,0]
#         for start, end in total:
#             if not ((interval1[1] < start) or (interval1[0] > end)):
#                vs[0] += 1
#             if not ((interval2[1] < start) or (interval2[0] > end)):
#                vs[1] += 1
#
#         answer.append(max(vs))
#
#     return max(answer)
#
#
#  print(solution([
#  "2016-09-15 20:59:57.421 0.351s",
#  "2016-09-15 20:59:58.233 1.181s",
#  "2016-09-15 20:59:58.299 0.8s",
#  "2016-09-15 20:59:58.688 1.041s",
#  "2016-09-15 20:59:59.591 1.412s",
#  "2016-09-15 21:00:00.464 1.466s",
#  "2016-09-15 21:00:00.741 1.581s",
#  "2016-09-15 21:00:00.748 2.31s",
#  "2016-09-15 21:00:00.966 0.381s",
#  "2016-09-15 21:00:02.066 2.62s"
#  ]))
#
#  print(solution([
#  "2016-09-15 01:00:04.002 2.0s",
#  "2016-09-15 01:00:07.000 2s"
#  ]))
#
# print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))


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

import math

def solution(n, times):
    end = math.ceil(n//len(times)) * max(times)
    start = 0
    pivot = 0
    answer = 0
    while start <= end:
        pivot = (end + start) // 2
        target = 0
        for time in times:
            target += pivot//time
        print('pivot: ',pivot,'target: ',target,'start: ',start,'end: ',end)
        if target >= n:
            answer = pivot
            end = pivot - 1
        elif target < n:
            start = pivot + 1
    return answer

print(solution(6,[7,10]))
