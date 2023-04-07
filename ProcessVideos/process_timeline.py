#!/usr/bin/env python

# Sort imports alphabeticaly
from Score.score_factory import createTennisScore
from Configuration.project_consts import PLAYER1, PLAYER2
from ProcessVideos.update_scoreboard import UpdateScoreboard
import sys
import json

# Marker colors of end frame to determine who won the point
# The colors are defined in DaVinci Resolve
PLAYER1_PT = 'Cyan'
PLAYER2_PT = 'Green'

DEBUG_FLAG = True

# Object to hold the tennis score based on GAME_TYPE
score = createTennisScore()

# Object to create the JPEG scoreboards to embed in the videos
update_scoreboard = UpdateScoreboard()

# TODO this needs to move to something global
def debug_print(*args, **kwargs):
    if DEBUG_FLAG:
        print(*args, file=sys.stdout, **kwargs)

# Takes the original timeline with markers, creates the subclip info items
# and returns an array of subclips that includes the MediaPool Items
# The actual MediaPoolItem is required for DaVinci to efficiently make
# subclips
def ProcessTimeline(timeline, clips):
    # Holds subclips across ALL clips in the timeline. Object definition
    # found on google...
    #{
    #    "mediaPoolItem": MediaPoolItem,
    #    "startFrame": start frame
    #    "endFrame": end frame
    #}
    subclip_list = []

    # Create empty scoreboard at the beginning of the match
    update_scoreboard.update_scoreboard(score)

    # Assume markers are created on Video Track 1
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

# The initial set of markers can have consecutive BLUE (Start point) markers
# (Bad Tosses, faults, let's, etc...)
# We want to keep the immediate parirs of markers and remove earlier BLUE markers
# {BLUE, CYAN} or {BLUE, GREEN} markers. This becomes each subclip
# EX: {BLUE1, BLUE2, BLUE3, CYAN} ->  {BLUE3, CYAN}
def filter_markers(markers):
    # markers.keys() returns frame numbers. We need to check the actual
    # color of those frames
    sorted_frames = sorted(markers.keys())

    i = 0
    while i < len(sorted_frames) - 1:
        frame1_color = markers[sorted_frames[i]]['color']
        frame2_color = markers[sorted_frames[i+1]]['color']
        if frame1_color == frame2_color:
            sorted_frames.pop(i)
        else:
            i += 1

    return sorted_frames
