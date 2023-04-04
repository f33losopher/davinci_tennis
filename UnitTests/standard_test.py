import pytest

from Score.abs_score import AbsScore
from Score.standard import StandardScore
from Configuration.project_consts import *

def test_init():
    std_score = StandardScore()
    assert 0 == std_score.get_full_match_score()[MATCH][PLAYER1][0]
    assert 0 == std_score.get_full_match_score()[MATCH][PLAYER2][0]
    assert 0 == std_score.get_full_match_score()[GAME][PLAYER1]
    assert 0 == std_score.get_full_match_score()[GAME][PLAYER2]

def test_basic_increment_game_score():
    std_score = StandardScore()

    std_score.update_game_score(PLAYER1, PLAYER2)
    assert "15" == std_score.get_game_score(PLAYER1)
    assert "0" == std_score.get_game_score(PLAYER2)

