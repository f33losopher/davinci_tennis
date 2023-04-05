import pytest

from Score.abs_score import AbsScore
from Score.standard import StandardScore
from Configuration.project_consts import *

def create_score():
    score = StandardScore()
    score.get_full_match_score()[MATCH][PLAYER1] = [0]
    score.get_full_match_score()[MATCH][PLAYER2] = [0]
    score.get_full_match_score()[GAME][PLAYER1] = 0
    score.get_full_match_score()[GAME][PLAYER2] = 0

    return score

def isInit(score):
    return (
        (0 == score.get_full_match_score()[MATCH][PLAYER1][0]) and
        (0 == score.get_full_match_score()[MATCH][PLAYER2][0]) and
        (0 == score.get_full_match_score()[GAME][PLAYER1]) and
        (0 == score.get_full_match_score()[GAME][PLAYER2])
    )

def test_init():
    score = create_score()
    assert True == isInit(score)

def test_basic_increment_game_score():
    score = create_score()
    assert True == isInit(score)

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
    score = create_score()
    assert True == isInit(score)

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
    score = create_score()
    assert True == isInit(score)

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

    # This should end the game, games scores go back to zero
    # Increment set score
    score.update_game_score(PLAYER1, PLAYER2)
    score.update_game_score(PLAYER1, PLAYER2)
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)
    assert "1" == score.get_match_score(PLAYER1).rstrip()
    assert "0" == score.get_match_score(PLAYER2).rstrip()

    # Set the game score at deuce and repeat for PLAYER2
    game_score = score.get_full_match_score()[GAME]
    game_score[PLAYER1] = 3
    game_score[PLAYER2] = 3

    assert "40" == score.get_game_score(PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "-" == score.get_game_score(PLAYER1)
    assert "Ad" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "40" == score.get_game_score(PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    assert "Ad" == score.get_game_score(PLAYER1)
    assert "-" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER2, PLAYER1)
    assert "40" == score.get_game_score(PLAYER1)
    assert "40" == score.get_game_score(PLAYER2)

    # This should end the game, games scores go back to zero
    # Increment set score
    score.update_game_score(PLAYER2, PLAYER1)
    score.update_game_score(PLAYER2, PLAYER1)
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)
    assert "1" == score.get_match_score(PLAYER1).rstrip()
    assert "1" == score.get_match_score(PLAYER2).rstrip()

def test_5_7_scenario():
    score = create_score()
    assert True == isInit(score)

    score.get_full_match_score()[MATCH][PLAYER1] = [5]
    score.get_full_match_score()[MATCH][PLAYER2] = [5]

    score.get_full_match_score()[GAME][PLAYER1] = 3

    score.update_game_score(PLAYER1, PLAYER2)

    assert "6" == score.get_match_score(PLAYER1).rstrip()
    assert "5" == score.get_match_score(PLAYER2).rstrip()
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)

    score.update_game_score(PLAYER1, PLAYER2)
    score.update_game_score(PLAYER1, PLAYER2)
    score.update_game_score(PLAYER1, PLAYER2)
    score.update_game_score(PLAYER1, PLAYER2)

    assert "7 0" == score.get_match_score(PLAYER1).rstrip()
    assert "5 0" == score.get_match_score(PLAYER2).rstrip()
    assert "0" == score.get_game_score(PLAYER1)
    assert "0" == score.get_game_score(PLAYER2)
