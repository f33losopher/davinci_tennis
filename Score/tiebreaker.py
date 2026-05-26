from Score.abs_score import AbsScore
from Configuration.project_consts import *
 
# Tracks the tiebreak points, can go to 7 or 10
# First to reach the target (7 or 10) wins, must win by 2
class TiebreakScore(AbsScore):
 
    def __init__(self, target_points):
        super().__init__()
 
        # 7 for a standard tiebreaker, 10 for a match tiebreaker (super tiebreak)
        self.target_points = target_points
 
        # Points conversion dictionary — tiebreak scores are just raw numbers
        self.points_conversion = {i: str(i) for i in range(target_points + 10)}
 
    def get_game_score(self, player) -> str:
        game_score = self.match_score[GAME]
        requested_score = game_score[player]
 
        if requested_score in self.points_conversion:
            return self.points_conversion[requested_score]
 
        return str(requested_score)
 
    def update_game_score(self, player):
        other_player = PLAYER1
        if player == PLAYER1:
            other_player = PLAYER2
 
        game_score = self.match_score[GAME]
        game_score[player] += 1
 
        # Player wins the tiebreak if they reach the target and are ahead by at least 2
        if (game_score[player] >= self.target_points) and \
           (game_score[player] - game_score[other_player] > 1):
            self.update_match_score(player)
            game_score[player] = 0
            game_score[other_player] = 0
 
    def update_match_score(self, player):
        other_player = PLAYER1
        if player == PLAYER1:
            other_player = PLAYER2
 
        match_score = self.match_score[MATCH]
        match_score[player][-1] += 1
 
        # Tiebreak winning a set — close it out and start a new one
        match_score[player].append(0)
        match_score[other_player].append(0)