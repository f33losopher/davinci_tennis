import pytest
from Configuration.project_consts import *
from ProcessVideos.update_scoreboard import UpdateScoreboard
from Score.abs_score import AbsScore
from Score.standard import StandardScore
import os

def test_draw_scoreboard():
    score = StandardScore()

    update_scoreboard = UpdateScoreboard()
    update_scoreboard.update_scoreboard(score)

# Should only be one file to remove
def test_cleanup_artifacts():
    # Check if a file exists, if it does delete it
    rm_file = CONFIG[ROOT_MEDIA_FOLDER] + '\\scoreboard_clipNo_0.jpg'
    if os.path.exists(rm_file):
        os.remove(rm_file)