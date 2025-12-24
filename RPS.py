import random

def player(prev_play, opponent_history=[], my_history=[], round_count=[0]):
    # Detect new match (important!)
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        round_count[0] = 0
        return "R"

    round_count[0] += 1
    opponent_history.append(prev_play)

    beats = {"R": "P", "P": "S", "S": "R"}

    # -------------------------------------------------
    # Phase 1: Bait Abbey with a fixed pattern (first 5)
    # -------------------------------------------------
    if round_count[0] <= 5:
        move = ["R", "P", "S", "R", "P"][round_count[0] - 1]
        my_history.append(move)
        return move

    # -------------------------------------------------
    # Phase 2: Predict Abbey's prediction (reverse Markov)
    # -------------------------------------------------
    if len(opponent_history) >= 3:
        patterns = {}
        for i in range(len(opponent_history) - 2):
            pair = "".join(opponent_history[i:i+2])
            nxt = opponent_history[i+2]
            patterns.setdefault(pair, {"R": 0, "P": 0, "S": 0})
            patterns[pair][nxt] += 1

        last_pair = "".join(opponent_history[-2:])
        if last_pair in patterns:
            abbey_guess = max(patterns[last_pair], key=patterns[last_pair].get)
            move = beats[abbey_guess]
            my_history.append(move)
            return move

    # -------------------------------------------------
    # Phase 3: Controlled randomness (anti-Kris fallback)
    # -------------------------------------------------
    move = random.choice(["R", "P", "S"])
    my_history.append(move)
    return move
