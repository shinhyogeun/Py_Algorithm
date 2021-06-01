
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
# print(solution(["classic", "pop", "classic", ®"classic", "pop"],[500, 600, 150, 800, 2500]))

def solution(a):
    if len(a) <= 3:
        return 0

    answerArrs = []
    answerArrs.append([[a[0]]])

    target = [[a[0]]]
    for i in range(len(a)):
        for j in range(len(answerArrs)):
            if len(answerArrs[j])//2 == 0:
                if target[j]:
            else:
                answerArr

        answerArrs.append([a[i]])
        target.append([a[i]])

    answer = -1
    return answer

solution([5,2,3,3,5,3])