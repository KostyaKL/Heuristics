import math


def topsis(table, candidates_num, specs_num, candidate_dict):
    normal = table.copy()
    for spec in range(0, specs_num):
        for candidate in range(0, candidates_num):
            x = table[spec][candidate]
            r = 0
            for i in range(0, candidates_num):
                r += table[spec][i] * table[spec][i]
            normal[spec][candidate] = x/math.sqrt(r)


    score_res = []

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

print(topsis(table, 3, 21, candidates))