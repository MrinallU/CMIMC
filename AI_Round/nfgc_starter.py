import sys
import json

# INPUT FORMAT (per turn):
'''
    "yesterday": [] on first day, otherwise a 2D list, where each element is
        [c_1, c_2, ..., c_10] for a specific player.
        The order of the players remains consistent in this list.
    "scores": A list of all players’ current total money made.
        The order of the players here matches that of "yesterday".
    "my_index": Which index into the above lists you are.
'''
# OUTPUT FORMAT (per turn):
'''
    "buys": A list [c_1, c_2, ..., c_10] of how many of each coin
        you would like to purchase, which must be non-negative integers
        summing to at most 100.
'''
# Function for handling output
def output(buys):
    print(json.dumps({"buys": buys}))


# You can store globals outside of the main loop
cache = []
profits=  [0] * 10
day = 0

while True:
    # Fetches input from grader (no need to edit)
    _data = json.loads(input())
    yesterday = _data["yesterday"]
    scores = _data["scores"]
    my_index = _data["my_index"]
    buys = [0] * 10
    my_score = scores[my_index]

    profitToCoinMap = {}
    # End input


    ## REPLACE STRATEGY BELOW ##

    buys[0] = 0
    buys[1] = 0
    buys[2] = 0 
    buys[3] = 0


    if day == 0: 
      assert yesterday == [] # yesterday is empty on first day
      buys[4] = 12
      buys[5] = 14
      buys[6] = 16
      buys[7] = 18
      buys[8] = 19
      buys[9] = 21
    else:
      # Proportional
      buys[4] = 9
      buys[5] = 10
      buys[6] = 11
      buys[7] = 12
      buys[8] = 13
      buys[9] = 14

      # Interpolate

      # find top 6 profit
      for i in range(len(yesterday)):
        for j in range(len(yesterday[i])):
          if yesterday[i][j] != 0:
            profits[j] += (j+1) / yesterday[i][j];

      for i in range(len(profits)):
        profitToCoinMap[profits[i]] = i

      profits.sort()

      buys[profitToCoinMap[profits[9]]] += 10
      buys[profitToCoinMap[profits[8]]] += 8
      buys[profitToCoinMap[profits[7]]] += 6
      buys[profitToCoinMap[profits[6]]] += 4
      buys[profitToCoinMap[profits[5]]] += 2
      buys[profitToCoinMap[profits[4]]] += 1


    output(buys)
    day += 1 
