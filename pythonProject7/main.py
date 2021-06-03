
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
    all = {i:[] for i in set(a)}
    ende = len(a)
    answer = []

    for i in range(ende):
        all[a[i]].append(i)

    for key in all.keys():
        count = 0
        out = [0,[]]

        for i in range(1, len(all[key])):
            if all[key][i] == all[key][i-1] + 1:
                out[0] += 1
            else:
                if (1 in out[1]):
                    count += 2 + 2
                elif ende in out[1]:
                    count += 2 + 2
                elif out[0] > 0:
                    count += 4 + 2
                out = [0,[]]

            if (1 in out[1]):
                count += 2 + 2
            elif ende in out[1]:
                count += 2 + 2
            elif out[0] > 0:
                count += 4 + 2

        answer.append(count)
    return max(answer)

print(solution([5,2,3,3,5,3]))
print(solution([1,2,2,3]))