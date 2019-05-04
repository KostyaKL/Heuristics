# input will be a table using dictionary
# each row is a ranker
# each column is a candidate
# copy each row as a dictionary and sort it by rank, you get the score for each candidate from currant ranker
# add result to score count
# return score result

from time import gmtime, strftime, time


class Borda:
    @staticmethod
    def borda(table, candidates_num, rankers_num):
        start_time = int(round(time() * 1000))
        score_res = []
        for candidate in range(0, candidates_num):
            score_res.append(0)

        for ranker in range(0, rankers_num):
            tmp_ranker = []
            for candidate in range(0, candidates_num):
                tmp_ranker.append([candidate, table[ranker][candidate]])
            tmp_ranker.sort(key=lambda x: x[1], reverse=True)
            score = candidates_num - 1
            for candidate in range(0, candidates_num):
                score_res[0] += score
                score -= 1

        total_time = int(round(time() * 1000)) - start_time

        return {"result": score_res, "time": total_time}


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

table2 = [[1.9, 2.6, 1.8, 2.4, 2.2],
          [2.4, 2.6, 3.4, 3.5, 2.9],
          [1.2, 1.2, 1.7, 1.6, 1.5],
          [6.4, 7.1, 7.3, 7.3, 7.3],
          [5.3, 5.2, 6.1, 5.9, 5.4],
          [3.2, 4.2, 6.1, 6.4, 4.5],
          [5.1, 6.1, 8.5, 8.3, 6.3]
          ]

candidates = {0: "a",
              1: "b",
              2: "c",
              3: "d",
              4: "e"
              }

test1 = Borda.borda(table, 3, 21)
print(test1["result"], "in", strftime("%H:%M:%S:{}".format(test1["time"]%1000), gmtime(test1["time"]/1000.0)))
test2 = Borda.borda(table2, 5, 7)
print(test1["result"], "in", strftime("%H:%M:%S:{}".format(test2["time"]%1000), gmtime(test2["time"]/1000.0)))
