import sys
import json
import random

# INPUT FORMAT (per turn):
'''
    "arena": A 2D (25 x 25) list of integers representing the current
        arena state, 1 for a present tile and 0 for empty.
        Can be indexed via arena[i][j].
    "players": For every player, a dict containing
        "alive": whether they are alive or dead.
        "i", "j": their zero-indexed coordinates.
        The order of the players remains consistent in this list.
    "my_index": Which index into the "players" list you are.
    "grace_moves_left": How many grace moves are remaining (if any),
        i.e. if this is 1, then on your next move, the ground currently
        underneath you does not disappear, but if this is 0 it does.
'''
# OUTPUT FORMAT (per turn):
'''
    "i", "j": Your destination coordinates. Each coordinate can differ by
        at most 2 from your previous coordinates.
'''

global curr_size
def floodfill(r: int, c: int, color: int):
    global curr_size
    if (r < 0 or r >= size or c < 0 or c >= size) or arena[r][c] != 1 or visited[r][c]:
        return

    pExists = False
    for j in range(len(players)):
        if players[j]["i"] == (r) and players[j]["j"] == (c) and j != my_index:
            pExists = True
    if pExists == True:
        return
    visited[r][c] = True  # mark current square as visited
    curr_size += 1  # increment the size for each square we visit

    # recursively call flood fill for neighboring squares
    for i in range(len(dx)):
        floodfill(r + dx[i], c + dy[i], color)


# Function for handling output
def output(i, j):
    print(json.dumps({"i": i, "j": j}))



my_history = []
size = 25

visited = [[False for _ in range(size)] for _ in range(size)]
dx_og = [0, 1, 2, 0, 1, 2, 1, 2, -2, -2, -2, -1, -1, -1, 2, 1, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2,
      2, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2]
dy_og = [2, 2, 2, 1, 1, 1, 0, 0, 2, 1, 0, 2, 1, 0, -2, -2, -2, -1, -1, -1, 2, 2, 2, 1, 2, -1, -2, 0, 1, 2, -1, -2, 0, 1, 2,
      -1, -2, 0, 1, 2, -1, -2, 0, 1, 2, -1, -2]



dx = []
dy = []

dx_1 = [-2, -2, -1, -2, 0, -1, 0, -1, 0, 1, 2, 0, 1, 2, 1, 2, -2, -2, -2, -1, -1, -1, 2, 1, 0, 2, 1,]
dy_1 = [-2, -1, -2, 0, -2, -1, -1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 1, 0, 2, 1, 0, -2, -2, -2, -1, -1]

dx_2 = [2, 2, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 1, 2, -2, -2, -2, -1, -1, -1, 2, 1, 0, 2, 1]
dy_2 = [-2, -1, -2, 0, -2, -1, -1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 1, 0, 2, 1, 0, -2, -2, -2, -1, -1]

dx_3 = [2, 2, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 1, 2, -2, -2, -2, -1, -1, -1, 2, 1, 0, 2, 1]
dy_3 = [2, 1, 2, 0, 2, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 1, 0, 2, 1, 0, -2, -2, -2, -1, -1]

dx_4 = [-2, -2, -1, -2, 0, -1, 0, -1, 0, 1, 2, 0, 1, 2, 1, 2, -2, -2, -2, -1, -1, -1, 2, 1, 0, 2, 1]
dy_4 = [2, 1, 2, 0, 2, 1, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 2, 1, 0, 2, 1, 0, -2, -2, -2, -1, -1]

for u in range(len(dx_og)):
  dx_1.append(dx_og[u])
  dx_2.append(dx_og[u])
  dx_3.append(dx_og[u])
  dx_4.append(dx_og[u])
  dy_1.append(dy_og[u])
  dy_2.append(dy_og[u])
  dy_3.append(dy_og[u])
  dy_4.append(dy_og[u])

while True:
    # Fetches input from grader (no need to edit)
    _data = json.loads(input())
    arena = _data["arena"]
    players = _data["players"]
    my_index = _data["my_index"]
    grace_moves_left = _data["grace_moves_left"]
    # End input

    # Sample strategy (random)
    me = players[my_index]
    me_i, me_j = me["i"], me["j"]
    my_history.append((me_i, me_j))

    if grace_moves_left > 0:
        # me_i += dx[0]
        # me_j += dy[0]
        output(me_i, me_j)
    else:
        rand = random.randint(1, 4)
        if(rand == 1):
          dx = dx_1
          dy = dy_1
        elif(rand == 2):
          dx = dx_2
          dy = dy_2
        elif(rand == 3):
          dx = dx_3
          dy = dy_3
        else:
          dx = dx_4
          dy = dy_4
        assert len(dx_4) == len(dy_4)
        bestSize = -1
        bestInd = -1
        for i in range(len(dx)):
            if 0 <= me_i + dx[i] < size and 0 <= me_j + dy[i] < size:
                skipped = False
                for j in range(len(players)):
                    if players[j]["i"] == (me_i + dx[i]) and players[j]["j"] == (me_j + dy[i]):
                        skipped = True
                if arena[me_i + dx[i]][me_j + dy[i]] != 0 and skipped == False:
                    curr_size = 0
                    floodfill(me_i + dx[i], me_j + dy[i], 1)
                    if curr_size > bestSize:
                        bestSize = curr_size
                        bestInd = i
        me_i += dx[bestInd]
        me_j += dy[bestInd]
        output(me_i, me_j)
