from Score.abs_score import AbsScore
from Configuration.project_consts import *

# Tradiontal Tennis scoring with deuces
# First to 6 games wins set
# In case of 5-5 can win by 7-5 or going to tiebreaker
class StandardScore(AbsScore):

    def __init__(self): 
        super().__init__()

        # Points conversion dictionary
        self.points_conversion = {0: "0", 1: "15", 2: "30", 3: "40"}

    def get_game_score(self, player) -> str:
        rtn = ""

        other_player = PLAYER1
        if player == PLAYER1:
            other_player = PLAYER2

        match_score = self.match_score[MATCH]
        game_score = self.match_score[GAME]

        requested_score = game_score[player]

        if (match_score[player][-1] == 6 and match_score[other_player][-1] == 6):
            # Tiebreak situation, just return the game score
            rtn = str(game_score[player])
        elif game_score[player] >= 3 and game_score[other_player] >= 3:
            # This is an Ad situation
            other_score = game_score[other_player]

            if requested_score >= 3 and other_score >= 3:
                if requested_score == other_score:
                    rtn = self.points_conversion[3]
                elif requested_score - other_score == 1:
                    rtn = "Ad"
                elif requested_score - other_score == -1:
                    rtn = "-"
        elif requested_score in self.points_conversion:
            return self.points_conversion[requested_score]
        
        return rtn

    def update_game_score(self, player):
        other_player = PLAYER1
        if player == PLAYER1:
            other_player = PLAYER2

        match_score = self.match_score[MATCH]
        game_score = self.match_score[GAME]

        game_score[player] += 1

        # Check if we are in a tiebreaker by checking the active match score
        if match_score[player][-1] == 6 and match_score[other_player][-1] == 6:
            if (game_score[player] >= 7) and ((game_score[player] - game_score[other_player]) > 1):
                self.update_match_score(player)
                game_score[player] = 0
                game_score[other_player] = 0
        else:
            if game_score[player] > 3 and (game_score[player] - game_score[other_player] > 1):
                self.update_match_score(player)
                game_score[player] = 0
                game_score[other_player] = 0
    
    def update_match_score(self, player):
        other_player = PLAYER1
        if player == PLAYER1:
            other_player = PLAYER2

        match_score = self.match_score[MATCH]
        match_score[player][-1] += 1

        if ((match_score[player][-1] == 6) and (match_score[other_player][-1] < 5)) or match_score[player][-1] == 7:
            # The set is complete. Close out the set and start a new one
            match_score[player].append(0)
            match_score[other_player].append(0)