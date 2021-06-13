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

# def isSquareExist(board,number):
#     a = len(board) - number
#     b = len(board[0]) - number
#
#     for i in range(a+1):
#         for j in range(b+1):
#             trigger = False
#             for k in range(number):
#                 for u in range(number):
#                     if board[i+k][j+u] == 0:
#                         trigger = True
#                         break
#                 if trigger:
#                     break
#             if trigger:
#                 continue
#             return True
#     return False
#
# def solution(board):
#     short = len(board) if len(board[0]) >= len(board) else len(board[0])
#     for i in range(short,0,-1):
#         if isSquareExist(board,i):
#             return i**2
#     return 0
#
# print('답: ',solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
# print('답: ',solution([[0,0,1,1],[1,1,1,1]]))
# print('답: ',solution([[0,0,0,0]]))

# def solution(A,B):
#     a = sorted(A)
#     b = sorted(B,reverse=True)
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i] * b[i]
#
#     return answer

# def solution(land):
#     total = [land[0][:]]
#     for i in range(1,len(land)):
#         new = []
#         for j in range(4):
#             slsl = total[i-1][:j]
#             for k in total[i-1][j+1:]:
#                 slsl.append(k)
#             new.append(land[i][j]+max(slsl))
#         total.append(new)
#
#     return max(total[-1])
#
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# def jinbubConvert(jinbub,number):
#     if number == 0:
#         return '0'
#
#     maps = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     answer = []
#
#     while number > 0:
#         answer.append(maps[number % jinbub])
#         number //= jinbub
#
#     return ''.join(answer[::-1])
#
# def solution(n, t, m, p):
#     long = ''
#     answer = ''
#     until = p + (t-1) * m
#
#     king = 0
#     while len(long) < until:
#         long += jinbubConvert(n,king)
#         king += 1
#
#     for i in range(t):
#         answer += long[(p + i*m)-1]
#
#     return answer
#
# print(solution(2,4,2,1))
# print(solution(16,16,2,1))
# print(solution(16,16,2,2))


# def combination(arr):
#     answer = []
#
#     def pops(arr):
#         answer.append(arr.pop(0))
#         for i in arr:
#             pops(i)
#
#     for i in range(len(arr)):
#         answer.append(pops(arr[:]))

# def solution(n):
#     total = [[0 for k in range(i+1)] for i in range(n)]
#     target = n
#     a = 0
#     what = 0
#     while True:
#         print(total)
#         asd = 0
#         for i in total:
#             if 0 not in i:
#                 asd += 1
#         if asd == n:
#             break
#         for i in range(target-2*a):
#             total[a+i][a] = what
#             what += 1
#
#         for i in range(1,target-2*a):
#             total[(target-1)-a][i] = what
#             what += 1
# # 1,2
#         for i in range(a+1,target-2*(a+1)):
#             total[(target-1)-a-i][(target-2)-a] = what
#             what += 1
#
#         a += 1
#
#     return total

# def solution(skill, skill_trees):
#     skill = list(skill)
#     dic = {skill[i]:i+1 for i in range(len(skill))}
#
#     answer = 0
#
#     for skill_tree in skill_trees:
#         now = 0
#         possible = True
#         for i in skill_tree:
#             if i in skill:
#                 if dic[i] - now > 1:
#                     possible = False
#                     break
#                 if now + 1 == dic[i]:
#                     now += 1
#         if possible:
#             answer += 1
#
#     return answer

# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))

# def solution(n):
#     answer = 0
#     while n != 0:
#         if n % 2 == 0:
#             n /= 2
#         else:
#             answer += 1
#             n -= 1
#     return answer
#
# print(solution(5))

# def apend(string):
#     if string == '0':
#         return 0
#
#     while len(string) < 4:
#         string += string
#
#     return int(''.join(list(string)[:3]))
#
# def solution(numbers):
#     answer = ""
#     a = sorted(list(map(str,numbers)),reverse=True)
#     new = []
#
#     for i in a:
#         new.append([apend(i),i])
#
#     new = sorted(new,reverse=True)
#     print(new)
#
#     for i in new:
#         answer += i[1]
#
#     if answer.count('0') == len(answer):
#         return '0'
#
#     return answer
#
# print(solution([898,89]))


# def solution(cacheSize, cities):
#     total = []
#     answer = 0
#     for city in cities:
#         if city in total:
#             answer += 1
#             total.remove(city)
#             total.append(city)
#         else:
#             answer += 5
#             if len(total) == cacheSize:
#                 total.pop(0)
#             total.append(city)
#
#     return answer



def howmany(arr,number):
    count = 0
    for i in arr:
        if i < number:
            count += 1
        else:
            break
    return len(arr) - count
#
# def solution(citations):
#     citations = sorted(citations)
#     max1 = 0
#
#     for i in range(len(citations)+1):
#         # i번 이상 인용된 논문의 수 == kick
#         kick = howmany(citations,i)
#         # 만약 i번 이상 인용된 논문의 수가 i편 이상일때
#         if i <= kick:
#             max = i
#
#     return max
#
# print(solution([3,0,6,1,5]))
# print(solution([0,0,1,2,3,45]))
# print([1,2,3,4][:0])

# def solution(citations):
#     citations = sorted(citations)
#
#     answer = 0
#
#     for i in range(len(citations)):
#         if howmany(citations,i) >= i:
#             answer = i
#     return answer
#
# print(solution([3,0,6,1,5]))
# print([1,2,3,4,5,6][:0])

# def solution(number):
#     answer = [0,0]
#     while number != '1':
#         answer[0] += 1
#         next = ''
#         for i in number:
#             if i == '0':
#                 answer[1] += 1
#                 continue
#             next += '1'
#         number = str(format(len(next),'b'))
#
#     return answer
#
# print(solution("01110"))

# def solution(n, words):
#     total = set()
#     beforeWord = 'a'
#
#     cycle = 0
#
#     while True:
#         for i in range(n):
#             if words == []:
#                 return [0,0]
#
#             if words[0] in total:
#                 return [i+1, cycle+1]
#             elif list(words[0])[0] != list(beforeWord)[-1] and len(total) != 0:
#                 return [i+1, cycle+1]
#             else:
#                 beforeWord = words.pop(0)
#                 total.add(beforeWord)
#
#         cycle += 1
#
# print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))

# def solution(number, k):
#     num = list(number)
#     length = len(num)
#     remain = length - k
#     dic = {str(i):[] for i in set(number)}
#     answer = ''
#
#     for i in range(length):
#         dic[num[i]].append(len(num)-i)
#
#     limit = 1e9
#     while remain:
#         for i in sorted(dic.keys(),reverse=True):
#             while dic[i] != [] and limit <= dic[i][0]:
#                 dic[i].pop(0)
#             if dic[i] != [] and limit > dic[i][0] >= remain:
#                 remain -= 1
#                 limit = dic[i].pop(0)
#                 answer += str(i)
#                 break
#
#     return str(int(answer))
#
# print(solution("4177252841",4))

# def solution(prices):
#     answers = []
#     king = []
#     while prices:
#         answer = 0
#         copyedKing = king[:]
#         new = prices.pop()
#         print(new)
#
#         while copyedKing:
#             if new <= copyedKing[0]:
#                 copyedKing.pop(0)
#                 answer += 1
#             else:
#                 answer += 1
#                 break
#         king.insert(0,new)
#         answers.append(answer)
#
#     return answers[::-1]
#
# print(solution([1,2,3,2,3]))

# from itertools import combinations
#
# def solution(clothes):
#     total = {j:[] for j in set([i[1] for i in clothes])}
#     mix = len(total)
#     answer = 0
#     for clothe in clothes:
#         total[clothe[1]].append(clothe[0])
#
#     for i in total.keys():
#         total[i] = len(total[i])
#
#     print(total)
#     # for i in range(1,mix+1):
#     #     miniAnswer = 0
#     #     for combi in list(combinations(total.keys(),i)):
#     #         a = 1
#     #         for eaxh in combi:
#     #             a *= len(total[eaxh])
#     #         miniAnswer += a
#     #     answer += miniAnswer
#
#     return answer

# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
# print(len(list(combinations([i for i in range(30)],6))))

# def solution(bridge_length, weight, truck_weights):
#     complite = []
#     ing = []
#     k = 0
#
#     while truck_weights:
#         if weight >= sum(ing) + truck_weights[0]:
#             k += 1
#             ing.append(truck_weights.pop(0))
#         else:
#
#
#     answer = 0
#     return answer

# def solution(people, limit):
#     people = sorted(people)
#     answer = 0
#
#     left = 0
#     right = len(people) - 1
#
#     now = 0
#     while left != right:
#         if people[left] + people[right] > limit:
#             right -= 1
#         elif people[left] + people[right] < limit:
#             now += people[right]
#             left += 1
#         else:
#             answer += 1
#
#     return answer
#
# print(solution([160, 150, 140, 60, 50, 40], 200))

# def solution(prices):
#     min = [prices[-1],len(prices)-1]
#     max = [prices[-1],len(prices)-1]
#     answer = [0]
#     for i in range(len(prices)-2,-1,-1):
#         print(prices[i],'   min :',min,'max :',max)
#         if min[0] < prices[i]:
#             if max[0] < prices[i]:
#                 answer.append(1)
#                 max = [prices[i],i]
#                 # min = [prices[i],i]
#             else:
#                 # print(min[1],i)
#                 answer.append(min[1]-i)
#         else:
#             answer.append(len(prices)-i-1)
#             min = [prices[i],i]
#             max = [prices[i],i]
#     print(prices)
#     return answer[::-1]

# print(solution([1,2,3,2,3]))
# print(solution([0,1,6,7,1,4,2,5]))
# print(solution([1,2,3,4,5,7]))
# print(solution([2,1,4,9,2,1]))

# from collections import deque
#
# def solution(prices):
#     answer = []
#     q = deque(prices)
#
#     while q:
#         a = q.popleft()
#         an = 0
#         for i in range(len(q)):
#             an += 1
#             if q[i] < a:
#                 break
#         answer.append(an)
#
#     return answer
#
# print(solution([1,2,3,2,3]))
# print(solution([0,1,6,7,1,4,2,5]))
# print(solution([1,2,3,4,5,7]))
# print(solution([2,1,4,9,2,1]))

# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     q = deque(truck_weights)
#     now = deque()
#     complete = []
#     answer = 0
#
#     while len(q) != 0 and sum(now) + q[0] <= weight and len(now) < bridge_length:
#         now.append(q.popleft())
#         answer += 1
#
#     while complete != truck_weights:
#         # 이동!
#         answer += bridge_length - len(now)
#
#         # 다 내려
#         for i in range(len(now)):
#             complete.append(now.popleft())
#             # 한자리 탈 수 있니?
#             answer += 1
#             if len(q) != 0 and sum(now) + q[0] <= weight:
#                 now.append(q.popleft())
#         print(complete)
#
#         # 그 후에도 혹시 더 탈 수 있니?
#         while len(q) != 0 and sum(now) + q[0] <= weight and len(now) < bridge_length:
#             now.append(q.popleft())
#             answer += 1
#     return answer


# print(solution(1,100,[1,1,1,1,1,1]))
# print(solution(2,10,[7,4,5,6]))
# print(solution(2,110,[1,2,10]))
# print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))


# def solution(numbers):
#     answer = []
#     for number in numbers:
#         pivot = list(map(int,list(str(format(number,'b')))))
#         if pivot[-1] == 0:
#             number += 1
#         else:
#             count = -1
#             for i in range(1, len(pivot) + 1):
#                 if pivot[-i] == 0:
#                     break
#                 count += 1
#             bb = 0
#             for i in range(count):
#                 bb += 2**i
#             number += 1 + bb
#
#         answer.append(number)
#     return answer
#
# print(solution([2,7]))

# from collections import deque
#
# def solution(s):
#     s = deque(s)
#     s.popleft()
#     s.pop()
#     arr = []
#
#     while s:
#         start = s.popleft()
#         if start == '{':
#             new = s.popleft()
#             l = ''
#             while new != '}':
#                 l += new
#                 new = s.popleft()
#             arr.append(set(map(int,l.split(','))))
#     arr = sorted(arr, key=len)
#
#     answer = [list(arr[0])[0]]
#
#     for i in range(1,len(arr)):
#         answer.append(list(arr[i] - arr[i-1])[0])
#
#     return answer
#
# print(solution("{{2,1},{2},{2,1,3},{2,1,3,4}}"))

# from collections import deque
#
# def isPossible(s):
#     s = deque(s)
#     total = deque([s.popleft()])
#     while s:
#         new = s.popleft()
#         if len(total) != 0 and total[-1] == '{':
#             if new == '}':
#                 total.pop()
#             else:
#                 total.append(new)
#         elif len(total) != 0 and total[-1] == '[':
#             if new == ']':
#                 total.pop()
#             else:
#                 total.append(new)
#         elif len(total) != 0 and total[-1] == '(':
#             if new == ')':
#                 total.pop()
#             else:
#                 total.append(new)
#         else:
#             total.append(new)
#
#     if len(total) == 0:
#         return True
#
#     return False
#
# def solution(s):
#     s = deque(s)
#     answer = 0
#
#     for i in range(len(s)):
#         if isPossible(s):
#             answer += 1
#         s.append(s.popleft())
#     return answer
#
# print('답',solution('[](){}'))
# print('답',solution('}]()[{'))
# print('답',solution('[)(]'))
# print('답',solution('}}}'))

from itertools import combinations

# def solution(clothes):
#     total = {j:[] for j in set([i[1] for i in clothes])}
#     mix = len(total)
#     answer = 1
#
#     for clothe in clothes:
#         total[clothe[1]].append(clothe[0])
#
#     for a in total.keys():
#         total[a] = len(total[a])
#
#     for a in total.values():
#         answer *= a+1
#
#     return answer - 1
#
# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

# from collections import deque
#
# def convert(file):
#     realName = file
#     head = ''
#     number = ''
#     file = deque(file)
#     numbers = ['0','1','2','3','4','5','6','7','8','9']
#
#     while True:
#         if len(file) == 0 or file[0] in numbers:
#             break
#         head += file.popleft()
#
#     for i in range(5):
#         if len(file) == 0 or file[0] not in numbers:
#             break
#         number += file.popleft()
#
#     return [head.lower(),int(number),''.join(file),realName]
#
# def solution(files):
#     total = []
#     for file in files:
#         total.append(convert(file))
#
#     total.sort(key=lambda x:(x[0], x[1]))
#
#     return [i[3] for i in total]
#
# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

# from collections import deque
#
# def solution(msg):
#     dic = [chr(i).upper() for i in range(97,123)]
#     msg = deque(msg)
#     answer = []
#
#     while msg:
#         mini = ''
#         while len(msg) != 0 and (mini + msg[0]) in dic:
#             mini += msg.popleft()
#
#         if len(msg) != 0:
#             dic.append(mini + msg[0])
#
#         answer.append(dic.index(mini)+1)
#
#     return answer
#
# print(solution("KAKAO"))
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))


# import datetime
# from collections import deque
#
# def calGap(startTime,endTime):
#     startTime = datetime.datetime.strptime(startTime,'%H:%M')
#     endTime = datetime.datetime.strptime(endTime,'%H:%M')
#
#     pretty = str(endTime-startTime).split(',')[-1].split(':')
#
#     return 60*int(pretty[0]) + int(pretty[1])
#
# def turnToList(music):
#     answer = []
#     music = deque(music)
#
#     while music:
#         alpha = music.popleft()
#         if len(music) != 0 and music[0] == '#':
#             alpha += music.popleft()
#         answer.append(alpha)
#     return '/'.join(answer)+'/',answer
#
# def solution(m, musicinfos):
#     for i,musicinfo in enumerate(musicinfos):
#         startTime,endTime,name,music = musicinfo.split(',')
#         musicinfos[i] = [calGap(startTime, endTime),name,music]
#
#     musicinfos.sort(key=lambda x:(-x[0]))
#
#     for dutaiton, name, music in musicinfos:
#         totalMusic = ''
#         newMusic, newList = turnToList(music)
#         for i in range(dutaiton):
#             totalMusic += newList[i%(len(newList))] + '/'
#         sting, target = turnToList(m)
#         # print(sting,(totalMusic))
#         if sting in totalMusic:
#             return name
#
#     return '(None)'
#
# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

# from itertools import combinations
#
# def isIn(a,b):
#     count = 0
#     for i in a:
#         for j in b:
#             if i == j:
#                 count += 1
#     if count == len(a):
#         return True
#     return False
#
# def solution(relation):
#     kind = [i for i in range(len(relation[0]))]
#     k = 1
#     answer = 0
#     total = []
#
#     while k <= len(kind):
#         miniAnswer = []
#         for case in list(combinations(kind,k)):
#             news = []
#             for i in relation:
#                 new = ''
#                 for j in case:
#                     new += i[j]
#                 news.append(new)
#             if len(news) == len(list(set(news))):
#                 miniAnswer.append(case)
#
#         real = []
#         for i in miniAnswer:
#             for j in total:
#                 if isIn(j,i):
#                     break
#             else:
#                 real.append(i)
#
#         for i in real:
#             total.append(i)
#
#         answer += len(real)
#
#         k += 1
#
#     return answer

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# solution([
#     ['a','1','aaa','c','ng'],
#     ['b','1','bbb','c','g'],
#     ['c','1','aaa','d','ng'],
#     ['d','2','bbb','d','ng']
# ])

# def flat(arr):
#     new = []
#     for i in arr:
#         for j in i:
#             new.append(j)
#     return new
#
# def solution(arr):
#     answer = [0,0]
#
#     def cal(arr):
#         if len(arr) == 1:
#             answer[arr[0][0]] += 1
#         else:
#             if 0 not in flat(arr):
#                 answer[1] += 1
#             elif 1 not in flat(arr):
#                 answer[0] += 1
#             else:
#                 cal([[i for i in j[:len(arr) // 2]] for j in arr[:len(arr) // 2]])
#                 cal([[i for i in j[len(arr) // 2:]] for j in arr[:len(arr) // 2]])
#                 cal([[i for i in j[:len(arr) // 2]] for j in arr[len(arr) // 2:]])
#                 cal([[i for i in j[len(arr) // 2:]] for j in arr[len(arr) // 2:]])
#
#     cal(arr)
#
#     return answer
#
# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))

# def down(board):
#     for i in range(1,len(board)):
#         for k in range(len(board[0])):
#             if board[i][k] == '^':
#                 for j in range(i,0,-1):
#                     board[j][k] = board[j-1][k]
#                     board[j-1][k] = '^'

    # for i in board:
    #     print(i)
#     return  board
#
# down([
#     ['H', 'G', 'N', 'H', 'U'],
#     ['C', 'R', 'S', 'H', 'V'],
#     ['U', 'K', 'H', 'V', 'L'],
#     ['M', 'J', 'H', 'Q', 'B'],
#     ['G', 'S', 'H', 'O', 'T'],
#     ['M', 'Q', 'M', 'J', 'J'],
#     ['A', 'G', 'J', '^', '^'],
#     ['Q', 'U', 'L', '^', '^']
#     ])

# def solution(m, n, board):
#     board = [[j for j in list(i)] for i in board]
#     answer = [0]
#
#     def pissoff(arr):
#         for i in arr:
#             print(i)
#         print()
#         total = []
#         for i in range(m-1):
#             for j in range(n-1):
#                 sqaur = [arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1]]
#                 if len(list(set(sqaur))) == 1 and sqaur[0] != '^':
#                     for k in [(i,j),(i,j+1),(i+1,j),(i+1,j+1)]:
#                         total.append(k)
#         print(total)
#         total = list(set(total))
#         answer[0] += len(total)
#
#         if total != []:
#             for x,y in total:
#                 board[x][y] = '^'
#             pissoff(down(board))
#         else:
#             return
#
#     pissoff(board)
#
#     return answer[0]
#
# print(solution(8,5,[
#     "HGNHU",
#     "CRSHV",
#     "UKHVL",
#     "MJHQB",
#     "GSHOT",
#     "MQMJJ",
#     "AGJKK",
#     "QULKK"
# ]))

# print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# import heapq
#
# def solution(N, road, K):
#     INF = int(1e9)
#     answer = [INF for _ in range(N+1)]
#
#     info = {i: [] for i in range(1,N+1)}
#
#     for frm, t, time in road:
#         info[frm].append((t,time))
#         info[t].append((frm,time))
#
#     answer[1] = 0
#     q = []
#     heapq.heappush(q,(0,1))
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if dist <= answer[now]:
#             for i in info[now]:
#                 if dist + i[1] < answer[i[0]]:
#                     answer[i[0]] = dist + i[1]
#                     heapq.heappush(q,(dist + i[1], i[0]))
#     count = 0
#
#     for i in answer[1:]:
#         if i <= K:
#             count += 1
#
#     return count
#
# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))

# def solution(dirs):
#     dic = {'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}
#     total = [['X' for i in range(11)] for j in range(11)]
#     now = [5, 5]
#     answer = []
#
#     for dir in dirs:
#         if 10 >= now[0] + dic[dir][0] >= 0 and 10 >= now[1] + dic[dir][1] >= 0:
#             answer.append([(now[0],now[1]),(now[0] + dic[dir][0],now[1] + dic[dir][1])])
#             now = [now[0] + dic[dir][0],now[1] + dic[dir][1]]
#
#
#     return len(list(set([tuple(sorted(i)) for i in answer])))
#
# print(solution('ULURRDLLU'))
# print(solution('LULLLLLLU'))

# def solution(n):
#
#     total = [[0 for i in range(j)] for j in range(1,n+1)]
#     pivot = [1]
#     N = [n]
#     def pissoff(depth):
#         if N[0] == 0: return
#         for i in range(N[0]):
#             total[(2*depth)+i][depth] = pivot[0]
#             pivot[0] += 1
#         N[0] -= 1
#         if N[0] == 0: return
#         for i in range(N[0]):
#             total[len(total)-1-depth][depth+1+i] = pivot[0]
#             pivot[0] += 1
#         N[0] -= 1
#         if N[0] == 0: return
#         for i in range(N[0]):
#             total[len(total)-1-(depth+1)-i][len(total)-1-(2*depth+1)-i] = pivot[0]
#             pivot[0] += 1
#         N[0] -= 1
#         if N[0] == 0: return
#         return pissoff(depth+1)
#
#     pissoff(0)
#     answer = []
#
#     for i in total:
#         for j in i:
#             answer.append(j)
#
#     return answer

# from collections import deque
#
# def solution(people, limit):
#     people = deque(sorted(people))
#     answer = 0
#
#     while people:
#         new = [people.pop()]
#         if len(people) != 0 and new[0] + people[0] <= limit:
#             new.append(people.popleft())
#         answer += 1
#
#     return answer

from bisect import bisect_left,bisect_right

from collections import deque

# def solution2(bridge_length, weight, truck_weights):
#     q = deque(truck_weights)
#     now = deque()
#     complete = []
#     answer = 0
#
#     while len(q) != 0 and sum(now) + q[0] <= weight and len(now) < bridge_length:
#         now.append(q.popleft())
#         answer += 1
#
#     while complete != truck_weights:
#         # 이동!
#         answer += bridge_length - len(now)
#
#         # 다 내려
#         for i in range(len(now)):
#             answer += 1
#             complete.append(now.popleft())
#             # 한자리 탈 수 있니?
#             if len(q) != 0 and sum(now) + q[0] <= weight and len(now) < bridge_length:
#                 now.append(q.popleft())
#
#         # 그 후에도 혹시 더 탈 수 있니?
#         while len(q) != 0 and sum(now) + q[0] <= weight and len(now) < bridge_length:
#             now.append(q.popleft())
#             answer += 1
#
#     return answer
#
# from collections import deque
#
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     wait = deque(truck_weights[:])
#     passed = []
#     passing = deque([0] * bridge_length)
#     passingWeight = 0
#
#     while len(passed) != len(truck_weights):
#         print(passing)
#         answer += 1
#         if passing[-1] != 0:
#             if len(wait) != 0 and passingWeight + wait[0] - passing[-1] <= weight:
#                 passingWeight += wait[0]
#                 passing.appendleft(wait.popleft())
#             else:
#                 passing.appendleft(0)
#             passingWeight -= passing[-1]
#             passed.append(passing.pop())
#         else:
#             if len(wait) != 0 and passingWeight + wait[0] <= weight:
#                 passingWeight += wait[0]
#                 passing.appendleft(wait.popleft())
#                 passing.pop()
#             else:
#                 passing.appendleft(passing.pop())
#     return answer
#
# print([1,2,3,4][:3])
#
# print(solution(2,10,[2,1,6,8,5,3,2,3,5,2,3,5]))
# print(solution2(2,10,[2,1,6,8,5,3,2,3,5,2,3,5]))

# print(solution(100,100,[10]))
# print(solution(100,100,[100]))
# print(solution(100,100,[100,100,100,100,100,100,100,100,100,100]))

# def solution(rows, columns, queries):
#     total = [[i+1 for i in range(j*columns, j*columns + columns)] for j in range(rows)]
#     answer = []
#
#     def circlePop(query):
#         target = []
#         for i in range(query[1]-1,query[3]):
#             target.append(total[query[0]-1][i])
#         for i in range(query[0],query[2]):
#             target.append(total[i][query[3]-1])
#         for i in range(query[3]-2, query[1]-2,-1):
#             print(i)
#             target.append(total[query[2]-1][i])
#         for i in range(query[2]-2, query[0]-1,-1):
#             target.append(total[i][query[1]-1])
#         return target
#
#     def circlePush(query, target):
#         k = 0
#         for i in range(query[1]-1,query[3]):
#             total[query[0]-1][i] = target[k]
#             k+=1
#         for i in range(query[0],query[2]):
#             total[i][query[3]-1] = target[k]
#             k += 1
#         for i in range(query[3]-2, query[1]-2,-1):
#             total[query[2]-1][i] = target[k]
#             k += 1
#         for i in range(query[2]-2, query[0]-1,-1):
#             total[i][query[1]-1] = target[k]
#             k += 1
#
#     for query in queries:
#         for i in total:
#             print(i)
#         print()
#         circle = circlePop(query)
#         circle.insert(0,circle.pop())
#         answer.append(min(circle))
#         circlePush(query,circle)
#     for i in total:
#         print(i)
#     return answer

# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(4,6,[[2,2,3,5],[1,1,2,2],]))
# print(solution(100,97,[[1,1,100,97]]))

# def isSquareExist(board,number):
#     a = len(board) - number
#     b = len(board[0]) - number
#
#     for i in range(a+1):
#         for j in range(b+1):
#             trigger = False
#             for k in range(number):
#                 for u in range(number):
#                     if board[i+k][j+u] == 0:
#                         trigger = True
#                         break
#                 if trigger:
#                     break
#             if trigger:
#                 continue
#             return True
#     return False
#
# def solution(board):
#     short = len(board) if len(board[0]) >= len(board) else len(board[0])
#     for i in range(short,0,-1):
#         if isSquareExist(board,i):
#             return i**2
#     return 0

def solution(name):
    target = list(name)
    total = []
    mini = 0
    for i in range(len(target)):
        if abs(ord(target[i]) - 65) <= abs(91 - ord(target[i])):
            mini += abs(ord(target[i]) - 65)
        else:
            mini += abs(91 - ord(target[i]))

    def check(target,now,much):
        target[now] = 'A'
        if ''.join(target) == 'A' * len(target):
            total.append(much)
            return
        #['A','C','A','D']
        for i in range(1,len(target)):
            if target[now-i] != 'A':
                new = target[:]
                new[now-i] = 'A'
                if now-i < 0:
                    check(new,len(target)+now-i,much+i)
                else:
                    check(new, now-i, much+i)
                break
        for i in range(1,len(target)):
            if now+i < len(target) and target[now+i] != 'A':
                new = target[:]
                new[now+i] = 'A'
                check(new,now+i,much+i)
                break

    check(target,0,0)
    return mini+min(total)

print(solution('JAAABANSKJDLKSDLNSDLKSJNDOIDJSODJSOIDNDOISNOIDSNODIINDSOIDNSOIN'))
print(solution('JEROEN'))
print(solution('JAN'))