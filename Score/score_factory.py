from Configuration.project_consts import GAME_TYPE, CONFIG
from Score.game_types import GameTypes
from Score.standard import StandardScore
from Score.tiebreaker import TiebreakScore
# from tiebreak_score import TiebreakScore

def createTennisScore():
    if (CONFIG[GAME_TYPE] == GameTypes.STANDARD):
        return StandardScore()
    elif (CONFIG[GAME_TYPE] == GameTypes.TIEBREAK_7):
        return TiebreakScore(7)
    elif (CONFIG[GAME_TYPE] == GameTypes.TIEBREAK_10):
        return TiebreakScore(10)