from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

def test_player():
    assert play(player, quincy, 1000) >= 0.6
    assert play(player, abbey, 1000) >= 0.6
    assert play(player, kris, 1000) >= 0.6
    assert play(player, mrugesh, 1000) >= 0.6
    print("All tests passed!")
