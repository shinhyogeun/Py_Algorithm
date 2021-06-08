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

# def solution(name):
#     answer = 0
#     target = list(name)
#     now = 0
#
#     for i in range(len(target)):
#         if i == 0:
#             if abs(ord(target[i]) - 65) <= abs(91 - ord(target[i])):
#                 answer += abs(ord(target[i]) - 65)
#             else:
#                 answer += abs(91 - ord(target[i]))
#             continue
#
#         if target[i] == 'A':
#             continue
#         else:
#             if abs(i-now) <= len(target) - abs(i-now):
#                 answer += abs(i-now)
#             else:
#                 answer += len(target) - abs(i-now)
#
#             if abs(ord(target[i]) - 65) <= 91 - ord(target[i]):
#                 answer += abs(ord(target[i]) - 65)
#             else:
#                 answer += abs(91 - ord(target[i]))
#
#             now += abs(i - now)
#
#     return answer

# print(solution("JEROEN"))
# print(solution("JAZ"))
# print(solution("ZAZA"))
# print(solution("EEAAE"))
# print(solution("ZZZZZZ"))
# print(solution("BBAAABAAAAAAAAAAAABA"))

# def solution(priorities, location):
#     indexArr = [i for i in range(len(priorities))]
#
#     nowIndex = -1
#     answer = 0
#
#     while nowIndex != location:
#         if priorities[0] == max(priorities):
#             value = priorities.pop(0)
#             nowIndex = indexArr.pop(0)
#             answer += 1
#         else:
#             value = priorities.pop(0)
#             now = indexArr.pop(0)
#             priorities.append(value)
#             indexArr.append(now)
#
#     return answer
#
# print(solution([2,1,3,2],2))
# print(solution([1,1,9,1,1,1],0))
#
# print(max([(1,1),(1,2),(1,3)]))

# def solution(s):
#     s = list(s)
#     del s[0]
#     del s[len(s)-1]
#     s = ''.join(s)
#
#     l = []
#     arr = []
#
#     for i in s:
#         if i == '{':
#             l = []
#         elif i == '}':
#             arr.append(l)
#         elif i == ',' and :
#             l.append(int(i))
#
#     new = {len(i):i for i in arr}
#     print(new)
#     answer = [new[1][0]]
#
#     if len(new) >= 2:
#         for i in range(2, len(arr)+1):
#             answer.append(list(set(new[i]) - set(new[i-1]))[0])
#
#     return answer

# print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# print(solution("{{20,111},{111}}"))


# def solution(s):
#     answer = ''
#     aa = s.split(' ')
#     k = 0
#     for i in range(len(aa)):
#         if aa[i] == '':
#             answer += ' '
#         else:
#             k += 1
#             if 122 >= ord(aa[i][0]) >= 97:
#                 answer += ''.join([aa[i][k].lower() if k != 0 else aa[i][k].upper() for k in range(len(aa[i]))])
#             else:
#                 answer += ''.join([aa[i][k].lower() if k != 0 else aa[i][k] for k in range(len(aa[i]))])
#
#             if i != len(aa)-1:
#                 answer += ' '
#     if k == 0:
#         return s
#     return answer
#
# for i in 'asd   ':
#     print(i,1)
# print(solution("3people unFollowed me"))
# print(solution("3people unFolloWed me   a  "))
# print(solution('   '))
# print(solution('apple asaa'))
# print('apple'.split(' '))

# def solution(s):
#     answer = ''
#     start = True
#     for i in s:
#         if i == ' ':
#             answer += ' '
#             start = True
#         else:
#             if start:
#                 start = False
#                 if 122 >= ord(i) >= 97:
#                     answer += i.upper()
#                 else:
#                     answer += i
#             else:
#                 answer += i.lower()
#
#     return answer
#
# print(solution("3people unFolloWed me   a  "))
# print(list(' '))

# def solution(numbers):
#     numbers = sorted((list(map(int,list(str(i)))) for i in numbers),reverse=True)
#     answer = ""
#
#     for i in range(9,-1,-1):
#         battleArr = [j for j in numbers if j[0] == i]
#         if battleArr == []:
#             continue
#         elif len(battleArr) == 1:
#             answer += ''.join(map(str,battleArr[0]))
#         else:
#
#
#
#
#     return answer
# 3 304721 37
# print(solution([3,30,300,5,9]))



# yellow = x-2 * y-2
# brown = 2x+2y-4
# yellow = x-2 * y-2

# import math
#
# def solution(brown, yellow):
#     total = brown + yellow
#     answerArr = []
#     for i in range(1,int(math.floor(math.sqrt(total)))+1):
#         if int(total/i) == total/i:
#             answerArr.append(sorted([i,int(total/i)]))
#
#     for i in answerArr:
#         if yellow == (i[0]-2) * (i[1]-2):
#             return i[::-1]
#
# print(solution(10,2))

# def makeSameSet(a,b):
#     same = []
#     for i in a:
#         if i in b:
#             b.remove(i)
#             same.append(i)
#
#     return same
#
# def makeAllSet(a,b):
#     same = makeSameSet(a[:],b[:])
#     all = same[:]
#
#     while same != []:
#         real = same.pop(0)
#
#         a.remove(real)
#         b.remove(real)
#
#     for k in [a,b]:
#         for i in k:
#             all.append(i)
#
#     return all

# def solution(str1, str2):
#     a = [''.join(list(str1)[i:i+2]) for i in range(len(str1)-1)]
#     b = [''.join(list(str2)[i:i+2]) for i in range(len(str2)-1)]
#
#     filtered = [[],[]]
#     for k in range(2):
#         for i in [a,b][k]:
#             if not (90 >= ord(list(i)[0]) >= 65) and not (97 <= ord(list(i)[0]) <= 122):
#                 continue
#             if not (90 >= ord(list(i)[1]) >= 65) and not (97 <= ord(list(i)[1]) <= 122):
#                 continue
#             filtered[k].append(i.lower())
#
#     same = makeSameSet(filtered[0][:],filtered[1][:])
#     all = makeAllSet(filtered[0][:],filtered[1][:])
#
#     if filtered == [[],[]]:
#         return 65536
#     return int(65536*(len(same)/len(all)))
#
# print(solution('FRANCE','FRENCH'))
# print(solution('E=M*C^2','e=m*c^2'))
# print(solution('handshake','shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))

# import math
# from itertools import permutations
#
# def solution(numbers):
#     total = []
#     for i in range(1,len(numbers)+1):
#         a = list(permutations(numbers,i))
#         for j in a:
#             total.append(j)
#
#     total = list(set([int(''.join(i)) for i in list(total)]))
#
#     if 0 in total:
#         total.remove(0)
#     if 1 in total:
#         total.remove(1)
#
#     answer = 0
#
#     for i in total:
#         sosu = True
#         for j in range(2,int(math.sqrt(i))+1):
#             if i%j == 0:
#                 sosu = False
#                 break
#         if sosu:
#             answer += 1
#
#
#     return answer
#
# print(solution("011"))
# print(len(list(permutations("1234567",7))))

# import math
#
# def solution(w,h):
#     multiple = math.gcd(w,h)
#     answer = 0
#     if h < w:
#         a = w
#         w = h
#         h = a
#
#     for i in range(1, int(w/multiple)+1):
#         answer += int(math.ceil((h/w)*(i)) - math.floor((h/w)*(i-1)))
#
#     return w*h - answer * multiple
#
# print(solution(8,12))

# def solution(phone_book):
#     hash = ' ' + ' '.join(phone_book)
#
#     for i in range(len(phone_book)):
#         a = ' ' + phone_book[i]
#         if hash.count(a) >= 2:
#             return False
#
#     return True

# def solution(phone_book):
#     phone_book = sorted(phone_book,key=len)
#
#     for i in range(len(phone_book)):
#         for j in range(i+1,len(phone_book)):
#             if ' ' + phone_book[i] in ' ' + phone_book[j]:
#                 return False
#     return True

# def solution(phone_book):
#     answer = True
#
#     phone_book = sorted(phone_book)
#     print(phone_book)
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         print(p1,p2)
#         if p2.find(p1) == 0:
#             answer = False
#             break
#
#     return answer

# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["9","10"]))

# def solution(people, limit):
#     people = sorted(people)
#     answer = 0
#
#     while people != []:
#         now = 0
#         now += people.pop(0)
#
#         if people == []:
#             answer += 1
#             break
#
#         while now + people[0] <= limit:
#             now += people.pop(len(people)-1)
#             if people == []:
#                 break
#
#         answer += 1
#
#     return answer
# print(solution([70],100))
# print(solution([70,80,50],100))
# print(solution([70,80,50,50],100))

import math


# def solution(arr):
#     a = max(arr)
#     k = 1
#     while True:
#         s = 0
#         for i in arr:
#             if a*k % i != 0:
#                 k += 1
#                 break
#             else:
#                 s += 1
#         if s == len(arr):
#             break
#     return a*k
#
# print(solution([2,6,8,14]))
# print(solution([1,1,1,1]))

# def solution(arr1, arr2):
#     a = len(arr1)
#     b = len(arr2[0])
#
#     answer = [[0 for i in range(b)] for j in range(a)]
#
#     for i in range(a):
#         for j in range(b):
#             x = arr1[i]
#             y = [k[j] for k in arr2]
#             answer[i][j] = sum(zi*zi2 for zi,zi2 in zip(x,y))
#
#     return answer
#
# print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))

# def binarry(n):
#     answer = ''
#     while n > 0:
#         if n%2 == 1:
#             answer += '1'
#         else:
#             answer += '0'
#         n //= 2
#
#     return ''.join(list(answer)[::-1])
#
#
# def solution(n):
#     target = binarry(n).count('1')
#
#     while True:
#         n += 1
#         if binarry(n).count('1') == target:
#             break
#
#     return n
#
# print(solution(1502051))

# def solution(s):
#     arr = list(s)
#
#     plate = []
#
#     for i in arr:
#         if i == '(':
#             plate.append('(')
#         else:
#             if plate == []:
#                 return False
#             else:
#                 if plate[-1] == '(':
#                     del plate[-1]
#
#     if plate == []:
#         return True
#     return False
#
# print(solution(')()('))

def isSquareExist(board,number):
    a = len(board) - number
    b = len(board[0]) - number

    for i in range(a+1):
        for j in range(b+1):
            trigger = False
            for k in range(number):
                for u in range(number):
                    if board[i+k][j+u] == 0:
                        trigger = True
                        break
                if trigger:
                    break
            if trigger:
                continue
            return True
    return False

def solution(board):
    short = len(board) if len(board[0]) >= len(board) else len(board[0])
    for i in range(short,0,-1):
        if isSquareExist(board,i):
            return i**2
    return 0

print('답: ',solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print('답: ',solution([[0,0,1,1],[1,1,1,1]]))
print('답: ',solution([[0,0,0,0]]))