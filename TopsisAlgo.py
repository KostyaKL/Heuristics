import math


def topsis(table, candidates_num, specs_num, candidate_dict, specs_weight):

    normal = table[:]
    normal_weight = specs_weight.copy()

    # step 1 create normalized table
    for spec in range(0, specs_num):
        r = 0
        for i in range(0, candidates_num):
            r += table[spec][i] * table[spec][i]
        for candidate in range(0, candidates_num):
            x = table[spec][candidate]
            normal[spec][candidate] = x / math.sqrt(r)

    # normalize weight
    weight_sum = sum(specs_weight)
    for i in range(0, specs_num):
        normal_weight[i] = specs_weight[i] / weight_sum

    # step 2 multiply by weight
    for spec in range(0, specs_num):
        for candidate in range(0, candidates_num):
            normal[spec][candidate] *= normal_weight[spec]

    # step 3 determine best and worst solution
    alt_worst = []
    alt_best = []

    for spec in range(0, specs_num):
        alt_worst.append(min(normal[spec]))
        alt_best.append(max(normal[spec]))

    # for test only DELETE
    # tmp = alt_worst[0]
    # alt_worst[0] = alt_best[0]
    # alt_best[0] = tmp

    # step 4 measure distance
    dist_worst = []
    dist_best = []
    for candidate in range(0, candidates_num):
        good_sum = 0
        bad_sum = 0
        for spec in range(0, specs_num):
            bad_sum += (normal[spec][candidate] - alt_worst[spec]) * (normal[spec][candidate] - alt_worst[spec])
            good_sum += (normal[spec][candidate] - alt_best[spec]) * (normal[spec][candidate] - alt_best[spec])

        dist_worst.append(math.sqrt(bad_sum))
        dist_best.append(math.sqrt(good_sum))

    # step 5 calculate relative closeness
    similarity = []
    for candidate in range(0, candidates_num):
        similarity.append(dist_worst[candidate] / (dist_worst[candidate] + dist_best[candidate]))

    return similarity


table = [[7, 8, 9, 6],
         [9, 7, 6, 7],
         [9, 8, 8, 8],
         [8, 7, 9, 6]
         ]

weight = [0.1, 0.4, 0.3, 0.2]

candidates = {0: "honda",
              1: "ford",
              2: "mazda",
              3: "subaru",
              }

print(topsis(table, 4, 4, candidates, weight))

table2 = [[250, 200, 300, 275, 225],
          [16, 16, 32, 32, 16],
          [12, 8, 16, 8, 16],
          [5, 3, 4, 4, 2]
          ]

weight2 = [0.25, 0.25, 0.25, 0.25]

candidates2 = {0: "ph1",
               1: "ph2",
               2: "ph3",
               3: "ph4",
               4: "ph5"
               }

print(topsis(table2, 5, 4, candidates2, weight2))
