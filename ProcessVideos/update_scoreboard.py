from PIL import Image, ImageDraw, ImageFont
from Configuration.project_consts import *
from Score.abs_score import AbsScore

class UpdateScoreboard:
    def __init__(self):
        self.clip_no = 0

    # Updates the 
    def update_scoreboard(self, score: AbsScore):
        sb_font = ImageFont.truetype(DRAFT, 25)
        img = Image.open(BASE_SCOREBOARD)
        clear = img.copy()
        draw = ImageDraw.Draw(clear)
    
        draw.text((10, 5), score.get_match_score(PLAYER1), anchor="lm", font=sb_font)
        draw.text((340, 5), score.get_game_score(PLAYER1), anchor="rm", font=sb_font)
    
        draw.text((10, 40), score.get_match_score(PLAYER2), anchor="lm", font=sb_font)
        draw.text((340, 40), score.get_game_score(PLAYER2), anchor="rm", font=sb_font)
    
        clear.save(CONFIG[ROOT_MEDIA_FOLDER] + '\\scoreboard_clipNo_' + str(self.clip_no) + '.jpg')

        self.clip_no += 1
