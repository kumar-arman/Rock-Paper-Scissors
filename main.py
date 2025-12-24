from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Uncomment below to run tests
from test_module import test_player
test_player()

print(play(player, abbey, 1000))
