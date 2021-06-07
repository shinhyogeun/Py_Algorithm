#
# # import heapq
# #
# # def solution(genres, plays):
# #     sortedGenres = {i: [] for i in set(genres)}
# #
# #     for i in range(len(genres)):
# #         heapq.heappush(sortedGenres[genres[i]], (-plays[i], i))
# #
# #     answers = sorted(sortedGenres.values(), key=lambda x : sum([i[0] for i in x]))
# #
# #     answer = []
# #
# #     for ans in answers:
# #         for i in range(2):
# #             if ans != []:
# #                 answer.append(heapq.heappop(ans)[1])
# #
# #     return answer
# #
# # print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
#
#
# def solution(a):
#     if len(a) < 2:
#         return 0
#
#     all = {i:[] for i in set(a)}
#     ende = len(a)
#     answer = []
#
#     for i in range(ende):
#         all[a[i]].append(i)
#
#     for key in all.keys():
#         total = []
#         count = 0
#         out = [0,[]]
#         for i in range(1, len(all[key])):
#             if all[key][i] == all[key][i-1] + 1:
#                 out[0] += 1
#                 out[1].append(all[key][i-1])
#             else:
#                 if out[1] == []:
#                     if not (all[key][i] - (all[key][i - 1]) == 2 and all[key][i - 1] in [0,ende-2]):
#                         count += 2
#                 else:
#                     if 0 in out[1]:
#                         if all[key][i] - (out[1][-1]+1) >= 3:
#                             count += 2
#                         else:
#                             count += 0
#                     else:
#                         if all[key][i] - (out[1][-1]+1) >= 3:
#                             count += 4
#                         else:
#                             count += 2
#
#                 for i in out[1]:
#                     total.append(i)
#
#                 out = [0, []]
#
#         if out[1] == []:
#             count += 2
#         else:
#             if 0 in out[1]:
#                 count = 0
#             elif ende - 2 in out[1]:
#                 count += 2
#             else:
#                 count += 4
#         answer.append(count)
#     # print(answer)
#     return max(answer)
#
# print(solution([1,5,1,5,4]))
# print(solution([1,4,2,3,4,5]))
# print(solution([5,2,3,3,5,3]))
# print(solution([1,2,2,3]))
# print(solution([1,2,2,3,4,5]))
# print(solution([1,2,3,4]))
# print(solution([0,3,3,0,7,2,0,2,2,0]))
# print(solution([4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]))
# print(solution([2,1,2,2,2,1,1,2]))
# print(solution([0,1,4,1,3,6,8,1]))

# def solution(inputString):
#     total = []
#     for i in range(1000):
#         st = list(str(i))
#         total.append(st)
#
#     inputString2 = list(str(inputString))
#     target = 0
#     answer = 0
#     for i in range(1000):
#         if target == len(inputString2):
#             return int(''.join(answer))
#
#         if inputString2[target] in total[i]:
#             startpoint = 0
#
#             for k in range(len(total[i])):
#                 if total[i][k] == inputString2[target]:
#                     startpoint = k
#
#             for j in range(startpoint,len(total[i])):
#                 if inputString2[target] == total[i][j]:
#                     target += 1
#                     answer = total[i]
#
# print(solution(123903))
# print(solution(12345))
# print(solution(7234032479947))

# def solution(n, data, limit):
#     problemNumber = []
#
#     for i in data:
#         problemNumber.append(i.split(' ')[1])
#
#     problemInfo = {i:[] for i in set(problemNumber)}
#
#     for i in data:
#         problemInfo[i.split(' ')[1]].append(i.split(' '))
#
#     for i in problemInfo.keys():
#         problemInfo[i] = sorted(problemInfo[i], key=lambda x : x[0])
#
#     mxin = sorted(problemInfo)
#
#     new = {i: problemInfo[i] for i in mxin}
#
#     answer = []
#     answerName = []
#
#     for key in list(new.keys()):
#         im = []
#         sd = []
#         for i in problemInfo[key]:
#             im.append([i[2],i[3]])
#             sd.append(i[0])
#         answer.append(im)
#         answerName.append(sd)
#
#     for i in range(1,len(answer)):
#         for k in answer[i]:
#             ultra = []
#             for j in answer[i-1]:
#                 if (limit[0] != 0 and k[0]+j[0] <= limit[0]) or limit[0] == 0:
#                     if (limit[1] != 0 and k[1]+j[1] <= limit[1]) or limit[1] == 0:
#                         ultra.append([k[0]+j[0], k[1]+j[1]])
#                 aa = []
#                 for i in ultra:
#                     aa.append(sum(i))
#                 ultra[aa.index(min(aa))]
#
#
#     return 0
#
# print(solution(2, ["a1 1 6 6", "a2 1 2 9", "b1 2 3 3", "b2 2 4 1"], "0 0"))
#
# a = "a1 4 6 6"
# print(a.split(' ')[1])

# def solution(m):
#     t = m
#
#     answer = []
#
#     while t > 0:
#         if t % 3 == 0:
#             answer.append('4')
#         elif t % 3 == 1:
#             answer.append('1')
#         elif t % 3 == 2:
#             answer.append('2')
#
#         t = (t-1) // 3
#
#     return ''.join(answer[::-1])
#
# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(9))
# print(solution(10))

# def solution(record):
#     uids = {}
#     answer = []
#
#     for i in record:
#         iArray =  i.split(' ')
#         if iArray[0] == "Enter":
#             uids[iArray[1]] = iArray[2]
#         elif iArray[0] == "Change":
#             uids[iArray[1]] = iArray[2]
#
#     for i in record:
#         iArray = i.split(' ')
#         if iArray[0] == "Enter":
#             answer.append(uids[iArray[1]]+"님이 들어왔습니다.")
#         elif iArray[0] =="Leave":
#             answer.append(uids[iArray[1]] + "님이 나갔습니다.")
#
#     return answer

# def solution(s):
#     arr = list(s)
#
#     answer = []
#
#     for i in arr:
#         if answer == []:
#             answer.append(i)
#         elif answer[-1] == i:
#             del answer[-1]
#         else:
#             answer.append(i)
#
#     if answer == []:
#         return 1
#     else:
#         return 0
#
# print(solution('baabaa'))
# print(solution('abccba'))

# def solution(n):
#     target = n // 2
#     answer = 0
#     for i in range(1, target + 1):
#         total = i
#         k = 1
#
#         while total < n:
#             total += i + k
#             k += 1
#
#         if total == n:
#             answer += 1
#
#     return answer + 1
#
# print(solution(15))

# def delete(arr,speed):
#     arr2 = arr[:]
#     speed2 = speed[:]
#     while True:
#         if arr2 == []:
#             break
#         elif arr2[0] < 100:
#             break
#         else:
#             del arr2[0]
#             del speed2[0]
#
#     return arr2,speed2
#
# def solution(progresses, speeds):
#     week = progresses[:]
#     speed = speeds[:]
#     answer = []
#
#     while week != []:
#         if week[0] >= 100:
#             a,speed = delete(week,speed)
#             answer.append(len(week)-len(a))
#             week = a[:]
#         else:
#             for i in range(len(week)):
#                 week[i] += speeds[i]
#
#     return answer

# print(solution([93, 30, 55], [1, 30, 5]))

# def solution(w,h):
#     answer = 0
#     h = max(w,h)
#     w = min(w,h)
#
#     total = w * h
#     tilt = w/h
#
#     ultra = 1
#
#     while int(h) == h and h != 2:
#         h = h/2
#         ultra *= 2
#     print(h)
#     k = 1
#
#     for i in range(1,int(tilt*h + 1)):
#         answer += int(1/tilt * i) - int(1/tilt * (i-1)) + 1
#
#     print(answer*ultra)
#
# solution(4,8)
# solution(8,12)
# solution(3,4)
# print(solution(3,3))

# def solution(numbers, target):
#     answer = []
#
#     def dfs(value,index):
#         if index != len(numbers):
#             dfs(value+numbers[index],index+1)
#             dfs(value-numbers[index],index+1)
#         else:
#             answer.append(value)
#
#     dfs(0,0)
#
#     return answer.count(target)
#
# print(solution(	[1, 1, 1, 1, 1], 3))

# import math
#
# def solution(w,h):
#     k = 1
#     answer = 0
#     while True:
#         if w%2 == 1:
#             if k == w//2 + 1:
#                 answer += math.ceil(h / w * k) - math.floor(h / w * (k - 1)) + answer
#                 return int(w*h - answer)
#
#         answer += math.ceil(h / w * k) - math.floor(h / w * (k - 1))
#
#         if int((h/w) * k) == (h/w) * k:
#             break
#
#         k+=1
#
#     answer *= (w / k)
#
#     return int(w*h - answer)
# print(solution(3,7))
# print(solution(5,7))
# print(solution(12,8))
# print(solution(4,3))
# print(solution(100,100))

# from collections import deque
#
# def solution(maps):
#     q = deque([])
#
#     q.append([0,0])
#     dm = [1,0,-1,0]
#     dl = [0,1,0,-1]
#
#     while q:
#         l,m = q.popleft()
#         for i in range(4):
#             if len(maps) > l+dl[i] >= 0 and len(maps[0]) > m+dm[i] >= 0:
#                 if maps[l+dl[i]][m+dm[i]] == 1:
#                     maps[l + dl[i]][m + dm[i]] = maps[l][m] + 1
#                     q.append([l + dl[i],m + dm[i]])
#
#     if maps[len(maps)-1][len(maps[0])-1] == 1:
#         return -1
#     else:
#         return maps[len(maps)-1][len(maps[0])-1]
#
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

def solution(name):
    answer = 0
    target = list(name)
    now = 0

    for i in range(len(target)):
        if i == 0:
            if abs(ord(target[i]) - 65) <= abs(91 - ord(target[i])):
                answer += abs(ord(target[i]) - 65)
            else:
                answer += abs(91 - ord(target[i]))
            continue

        if target[i] == 'A':
            continue
        else:
            if abs(i-now) <= len(target) - abs(i-now):
                answer += abs(i-now)
            else:
                answer += len(target) - abs(i-now)

            if abs(ord(target[i]) - 65) <= 91 - ord(target[i]):
                answer += abs(ord(target[i]) - 65)
            else:
                answer += abs(91 - ord(target[i]))

            now += abs(i - now)

    return answer

# print(solution("JEROEN"))
# print(solution("JAZ"))
# print(solution("ZAZA"))
print(solution("EEAAE"))
print(solution("ZZZZZZ"))
print(solution("BBAAABAAAAAAAAAAAABA"))

