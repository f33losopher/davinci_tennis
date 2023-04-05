import pytest

from Score.abs_score import AbsScore
from Score.standard import StandardScore
from Configuration.project_consts import *

def test_init():
    score = StandardScore()
    assert 0 == score.get_full_match_score()[MATCH][PLAYER1][0]
    assert 0 == score.get_full_match_score()[MATCH][PLAYER2][0]
    assert 0 == score.get_full_match_score()[GAME][PLAYER1]
    assert 0 == score.get_full_match_score()[GAME][PLAYER2]

def test_basic_increment_game_score():
    score = StandardScore()

    # Increment PLAYER1 scores
    score.update_game_score(PLAYER1, PLAYER2)
    assert "15" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "30" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "40" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)
    assert "1" == score.get_match_score(PLAYER1).rstrip()
    assert "0" == score.get_match_score(PLAYER2).rstrip()

    # Increment PLAYER2 scores
    score.update_game_score(PLAYER2, PLAYER1)
    assert "15" == score.get_game_score(PLAYER2)
    assert "0" == score.get_game_score(PLAYER1)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "30" == score.get_game_score(PLAYER2)
    assert "0" == score.get_game_score(PLAYER1)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)
    assert "0" == score.get_game_score(PLAYER1)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)
    assert "1" == score.get_match_score(PLAYER1).rstrip()
    assert "1" == score.get_match_score(PLAYER2).rstrip()

def test_complete_normal_set():
    score = StandardScore()

    match_score = score.get_full_match_score()[MATCH]
    game_score = score.get_full_match_score()[GAME]

    # Set the score for PLAYER1 to be Match {5, 0} and Game {40, 0}
    match_score[PLAYER1] = [5]
    game_score[PLAYER1] = 3
    assert "5" == score.get_match_score(PLAYER1).rstrip()
    assert "40" == score.get_game_score(PLAYER1)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)
    assert "6 0" == score.get_match_score(PLAYER1).rstrip()
    assert "0 0" == score.get_match_score(PLAYER2).rstrip()

def test_ad_scenarios():
    score = StandardScore()

    # Set the score at Deuce
    game_score = score.get_full_match_score()[GAME]
    game_score[PLAYER1] = 3
    game_score[PLAYER2] = 3

    assert "40" == score.get_game_score(PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "Ad" == score.get_game_score(PLAYER1)
    assert "-" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "40" == score.get_game_score(PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "-" == score.get_game_score(PLAYER1)
    assert "Ad" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "40" == score.get_game_score(PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)