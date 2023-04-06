from PIL import Image, ImageDraw, ImageFont
from Configuration.project_consts import *
from Score.abs_score import AbsScore

class UpdateScoreboard:
    def __init__(self):
        self.clip_no = 0

    # Updates the scoreboard by drawing current score on BASE_SCOREBOARD
    def update_scoreboard(self, score: AbsScore):
        sb_font = ImageFont.truetype(DRAFT, 25)
        img = Image.open(BASE_SCOREBOARD)
        clear = img.copy()
        draw = ImageDraw.Draw(clear)
    
        draw.text((10, 18), self.get_name_and_match_score(score, PLAYER1), anchor="lm", font=sb_font)
        draw.text((385, 18), score.get_game_score(PLAYER1), anchor="rm", font=sb_font)
    
        draw.text((10, 53), self.get_name_and_match_score(score, PLAYER2), anchor="lm", font=sb_font)
        draw.text((385, 53), score.get_game_score(PLAYER2), anchor="rm", font=sb_font)
    
        # Use clip number twice otherwise when importing into DaVinci it'll
        # create a single clip because the filenames are same with sequential
        # numbering
        clear.save(CONFIG[ROOT_MEDIA_FOLDER] + '\\scoreboard_clipNo_' + str(self.clip_no) + '_' + str(self.clip_no) + '.jpg')

        self.clip_no += 1

    def get_name_and_match_score(self, score:AbsScore, player:str) -> str:
        rtn = PLAYERS[player]
        rtn = rtn + score.get_match_score(player)
        
        return rtn
    
    def get_clip_no(self) -> int:
        return self.clip_no
    



