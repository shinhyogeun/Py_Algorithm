
# import heapq
#
# def solution(genres, plays):
#     sortedGenres = {i: [] for i in set(genres)}
#
#     for i in range(len(genres)):
#         heapq.heappush(sortedGenres[genres[i]], (-plays[i], i))
#
#     answers = sorted(sortedGenres.values(), key=lambda x : sum([i[0] for i in x]))
#
#     answer = []
#
#     for ans in answers:
#         for i in range(2):
#             if ans != []:
#                 answer.append(heapq.heappop(ans)[1])
#
#     return answer
#
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


def solution(a):
    if len(a) < 2:
        return 0

    all = {i:[] for i in set(a)}
    ende = len(a)
    answer = []

    for i in range(ende):
        all[a[i]].append(i)

    for key in all.keys():
        total = []
        count = 0
        out = [0,[]]
        for i in range(1, len(all[key])):
            if all[key][i] == all[key][i-1] + 1:
                out[0] += 1
                out[1].append(all[key][i-1])
            else:
                if out[1] == []:
                    if not (all[key][i] - (all[key][i - 1]) == 2 and all[key][i - 1] in [0,ende-2]):
                        count += 2
                else:
                    if 0 in out[1]:
                        if all[key][i] - (out[1][-1]+1) >= 3:
                            count += 2
                        else:
                            count += 0
                    else:
                        if all[key][i] - (out[1][-1]+1) >= 3:
                            count += 4
                        else:
                            count += 2

                for i in out[1]:
                    total.append(i)

                out = [0, []]

        if out[1] == []:
            count += 2
        else:
            if 0 in out[1]:
                count = 0
            elif ende - 2 in out[1]:
                count += 2
            else:
                count += 4
        answer.append(count)
    # print(answer)
    return max(answer)

print(solution([1,5,1,5,4]))
print(solution([1,4,2,3,4,5]))
print(solution([5,2,3,3,5,3]))
print(solution([1,2,2,3]))
print(solution([1,2,2,3,4,5]))
print(solution([1,2,3,4]))
print(solution([0,3,3,0,7,2,0,2,2,0]))
print(solution([4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3]))
print(solution([2,1,2,2,2,1,1,2]))
print(solution([0,1,4,1,3,6,8,1]))