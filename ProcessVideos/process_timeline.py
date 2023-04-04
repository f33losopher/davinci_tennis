#!/usr/bin/env python

import sys
import json

# Takes the original timeline with markers, creates the subclip info items
# and creates a new timeline of the new clips

# Use markers trim unwanted video clips
START_PT = 'Blue'
END_PLAYER1_PT = 'Cyan'
END_PLAYER2_PT = 'Green'

DEBUG_FLAG = False

def debug_print(*args, **kwargs):
    if DEBUG_FLAG:
        print(*args, file=sys.stdout, **kwargs)

def ProcessTimeline(timeline, clips):
    # This holds subclips across all clips in the timeline
    subclip_list = []

    timelineItems = timeline.GetItemListInTrack('video', 1)
    for timelineItem in timelineItems:
        markers = timelineItem.GetMarkers()
        debug_print("timlineItem name: " + timelineItem.GetName())
        debug_print("Markers: ")
        debug_print(json.dumps(markers, indent=2))
        sorted_frames = filter_markers(markers)

        debug_print("Sorted and filtered frames: ")
        debug_print(sorted_frames)

        frm_start = 0
        frm_end = 0
        
        # At this point, assume sorted_frames is a pair of either
        # {BLUE, CYAN} or {BLUE, GREEN}
        for i in range(0, len(sorted_frames), 2):
            frm_start = sorted_frames[i]
            frm_end = sorted_frames[i+1] if i < len(sorted_frames)-1 else None

            if frm_end != None:
                subClip = {
                    "mediaPoolItem": clips[timelineItem.GetName()],
                    "startFrame": frm_start,
                    "endFrame": frm_end
                }

                subclip_list.append(subClip);
    
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
            sorted_frames.pop(i+1)
        else:
            i += 1

    return sorted_frames