import random

def play(player1, player2, num_games, verbose=False):
    p1_score = 0
    p2_score = 0

    p1_prev_play = ""
    p2_prev_play = ""

    for i in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            winner = "Tie"
        elif (
            (p1_play == "R" and p2_play == "S") or
            (p1_play == "S" and p2_play == "P") or
            (p1_play == "P" and p2_play == "R")
        ):
            winner = "Player 1"
            p1_score += 1
        else:
            winner = "Player 2"
            p2_score += 1

        if verbose:
            print(f"Game {i+1}: Player 1: {p1_play} | Player 2: {p2_play} | Winner: {winner}")

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = p1_score + p2_score

    if games_won > 0:
        win_rate = p1_score / games_won
    else:
        win_rate = 0

    print("Final results:", p1_score, "wins,", p2_score, "losses")
    print("Win rate:", win_rate)

    return win_rate


def quincy(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    choices = ["R", "P", "S", "R", "P"]
    return choices[len(opponent_history) % len(choices)]


def mrugesh(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)
    if len(opponent_history) < 10:
        return random.choice(["R", "P", "S"])
    most_common = max(set(opponent_history[-10:]), key=opponent_history[-10:].count)
    return {"R": "P", "P": "S", "S": "R"}[most_common]


def abbey(prev_play, opponent_history=[], play_order=[{
        "RR": 0, "RP": 0, "RS": 0,
        "PR": 0, "PP": 0, "PS": 0,
        "SR": 0, "SP": 0, "SS": 0,
    }]):

    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 2:
        return random.choice(["R", "P", "S"])

    last_two = "".join(opponent_history[-2:])
    play_order[0][last_two] += 1

    last_play = opponent_history[-1]
    possible_plays = [
        last_play + "R",
        last_play + "P",
        last_play + "S"
    ]

    prediction = max(possible_plays, key=lambda x: play_order[0][x])[-1]

    return {"R": "P", "P": "S", "S": "R"}[prediction]

def kris(prev_play):
    return {"R": "P", "P": "S", "S": "R"}.get(prev_play, random.choice(["R", "P", "S"]))
