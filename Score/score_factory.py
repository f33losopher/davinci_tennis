from Configuration.project_consts import GAME_TYPE, CONFIG
from Score.game_types import GameTypes
from Score.standard import StandardScore
# from tiebreak_score import TiebreakScore

def createTennisScore():
    if (CONFIG[GAME_TYPE] == GameTypes.STANDARD):
        return StandardScore()
    # elif (CONFIG[GAME_TYPE] == 'Tiebreak'):
    #     return TiebreakScore(7)