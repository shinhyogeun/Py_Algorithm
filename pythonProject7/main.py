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

def solution(n, data, limit):
    problemNumber = []

    for i in data:
        problemNumber.append(i.split(' ')[1])

    problemInfo = {i:[] for i in set(problemNumber)}

    for i in data:
        problemInfo[i.split(' ')[1]].append(i.split(' '))

    for i in problemInfo.keys():
        problemInfo[i] = sorted(problemInfo[i], key=lambda x : x[0])

    mxin = sorted(problemInfo)

    new = {i: problemInfo[i] for i in mxin}

    answer = []
    answerName = []

    for key in list(new.keys()):
        im = []
        sd = []
        for i in problemInfo[key]:
            im.append([i[2],i[3]])
            sd.append(i[0])
        answer.append(im)
        answerName.append(sd)

    for i in range(1,len(answer)):
        for k in answer[i]:
            ultra = []
            for j in answer[i-1]:
                if (limit[0] != 0 and k[0]+j[0] <= limit[0]) or limit[0] == 0:
                    if (limit[1] != 0 and k[1]+j[1] <= limit[1]) or limit[1] == 0:
                        ultra.append([k[0]+j[0], k[1]+j[1]])
                aa = []
                for i in ultra:
                    aa.append(sum(i))
                ultra[aa.index(min(aa))]


    return 0

print(solution(2, ["a1 1 6 6", "a2 1 2 9", "b1 2 3 3", "b2 2 4 1"], "0 0"))

a = "a1 4 6 6"
print(a.split(' ')[1])