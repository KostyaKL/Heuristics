# input will be a table using dictionary
# each row is a ranker
# each column is a candidate
# copy each row as a dictionary and sort it by rank, you get the score for each candidate from currant ranker
# add result to score count
# return score result


def borda(table, candidates_num, rankers_num, candidate_dict):
    score_res = []
    for candidate in range(0, candidates_num):
        score_res.append([candidate_dict[candidate], 0])

    for ranker in range(0, rankers_num):
        tmp_ranker = []
        for candidate in range(0, candidates_num):
            tmp_ranker.append([candidate, table[ranker][candidate]])
        tmp_ranker.sort(key=lambda x: x[1], reverse=True)
        score = candidates_num - 1
        for candidate in range(0, candidates_num):
            score_res[tmp_ranker[candidate][0]][1] += score
            score -= 1
    return score_res


table = [[3, 2, 1],
         [3, 1, 2],
         [3, 1, 2],
         [3, 1, 2],
         [3, 1, 2],
         [3, 1, 2],
         [3, 1, 2],
         [3, 1, 2],
         [1, 3, 2],
         [1, 3, 2],
         [1, 3, 2],
         [1, 3, 2],
         [1, 3, 2],
         [1, 3, 2],
         [1, 3, 2],
         [1, 2, 3],
         [1, 2, 3],
         [1, 2, 3],
         [1, 2, 3],
         [1, 2, 3],
         [1, 2, 3],
         ]

candidates = {0: "a",
              1: "b",
              2: "c"
              }

print(borda(table, 3, 21, candidates))
