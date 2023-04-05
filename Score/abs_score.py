from Configuration.project_consts import *

# Abstract Class for all Tennis Scores
class AbsScore:
    def __init__(self):
        self.match_score = {
            MATCH: {
                PLAYER1: [0],
                PLAYER2: [0]
            },
            GAME: {
                PLAYER1: 0,
                PLAYER2: 0
            }
        }

        if ('init_score' in globals() and init_score[MATCH]):
            self.match_score[MATCH][PLAYER1] = init_score[MATCH][PLAYER1]
            self.match_score[MATCH][PLAYER2] = init_score[MATCH][PLAYER2]
        if ('init_score'  in globals() and init_score[GAME]):
            self.match_score[GAME][PLAYER1] = init_score[GAME][PLAYER1]
            self.match_score[GAME][PLAYER2] = init_score[GAME][PLAYER2]
    
    def get_full_match_score(self) -> any:
        return self.match_score

    # Define a method and show it returns a string
    def get_match_score(self, player) -> str:
        score = ""
        for s in self.match_score[MATCH][player]:
            score = score + str(s) + " "

        return score.rstrip()
    
    # Let each scoring class define how to return the score
    def get_game_score(self, player) -> str:
        pass

    # Update game score after each point
    def update_game_score(self, player):
        pass

    # Update match score depending on game type
    def update_match_score(self, player):
        pass