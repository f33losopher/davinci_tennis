#!/usr/bin/env python

from Score.score_factory import createTennisScore
from Configuration.project_consts import PLAYER1, PLAYER2
from ProcessVideos.update_scoreboard import UpdateScoreboard
import sys
import json

# Takes the original timeline with markers, creates the subclip info items
# and creates a new timeline of the new clips

# Marker colors of end frame to determine who won the point
PLAYER1_PT = 'Cyan'
PLAYER2_PT = 'Green'

DEBUG_FLAG = True

score = createTennisScore()
update_scoreboard = UpdateScoreboard()

def debug_print(*args, **kwargs):
    if DEBUG_FLAG:
        print(*args, file=sys.stdout, **kwargs)

def ProcessTimeline(timeline, clips):
    # This holds subclips across all clips in the timeline
    subclip_list = []

    # Create the scoreboard at the beginning of the match
    update_scoreboard.update_scoreboard(score)

    timelineItems = timeline.GetItemListInTrack('video', 1)
    for timelineItem in timelineItems:
        markers = timelineItem.GetMarkers()
        debug_print("timlineItem name: " + timelineItem.GetName())
        debug_print("Markers: ")
        debug_print(json.dumps(markers, indent=2))
        sorted_frames = filter_markers(markers)

        debug_print("Sorted and filtered frames: ")
        debug_print(sorted_frames)

        frame_start = 0
        frame_end = 0
        
        # At this point, assume sorted_frames is a pair of either
        # {BLUE, CYAN} or {BLUE, GREEN}
        for i in range(0, len(sorted_frames), 2):
            frame_start = sorted_frames[i]
            frame_end = sorted_frames[i+1] if i < len(sorted_frames)-1 else None

            # TODO Need to handle case where a point crosses timelineItem boundary
            if frame_end != None:
                subClip = {
                    "mediaPoolItem": clips[timelineItem.GetName()],
                    "startFrame": frame_start,
                    "endFrame": frame_end
                }

                subclip_list.append(subClip);

                # Update the score based on marker {CYAN, GREEN}
                if markers[frame_end]['color'] == PLAYER1_PT:
                    score.update_game_score(PLAYER1)
                elif markers[frame_end]['color'] == PLAYER2_PT:
                    score.update_game_score(PLAYER2)
                else:
                    # Must be hold over from the yellow markers
                    pass

                # Create the scoreboard jpeg for this subclip
                update_scoreboard.update_scoreboard(score)

    return subclip_list

# The initial set of markers can have consecutive BLUE markers.
# Remove all the duplicates so we only have pairs of
# {BLUE, CYAN} or {BLUE, GREEN} markers. This is essentially
# each subclip
def filter_markers(markers):
    sorted_frames = sorted(markers.keys())

    i = 0
    while i < len(sorted_frames) - 1:
        frame1 = markers[sorted_frames[i]]['color']
        frame2 = markers[sorted_frames[i+1]]['color']
        if frame1 == frame2:
            sorted_frames.pop(i)
        else:
            i += 1

    return sorted_frames
