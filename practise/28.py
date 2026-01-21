# 8 puzzle Problem


from collections import deque

# Goal state
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Moves: up, down, left, right
MOVES = {
    "U": -3,  # move blank up
    "D": 3,   # move blank down
    "L": -1,  # move blank left
    "R": 1    # move blank right
}

def is_valid_move(pos, move):
    # Check boundaries for left and right moves
    if move == "L" and pos % 3 == 0:
        return False
    if move == "R" and pos % 3 == 2:
        return False
    # Check boundaries for up and down moves
    if move == "U" and pos < 3:
        return False
    if move == "D" and pos > 5:
        return False
    return True

def swap(state, i, j):
    lst = list(state)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)

def bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))  # (state, moves_list)
    visited = set()
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()

        if state == GOAL_STATE:
            return path  # return list of moves

        zero_pos = state.index(0)

        for move, delta in MOVES.items():
            if is_valid_move(zero_pos, move):
                new_zero = zero_pos + delta
                new_state = swap(state, zero_pos, new_zero)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [move]))
    return None  # no solution

# ---------------- Input ----------------
# Enter initial state row-wise, use 0 for blank
print("Enter initial state row-wise (use 0 for blank):")
initial = []
for _ in range(3):
    initial += list(map(int, input().split()))

initial_state = tuple(initial)

# Solve
solution = bfs(initial_state)

if solution is None:
    print("No solution exists!")
else:
    print(f"Solution found in {len(solution)} moves:")
    print(" -> ".join(solution))
