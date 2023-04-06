from DaVinci.python_get_resolve import GetResolve
from timecode import Timecode
from Configuration.project_consts import *
import time

# TODO
# Manual step before running this script 
# Create another track for video

resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

timeline = project.GetCurrentTimeline()

tl_clip_list  = timeline.GetItemListInTrack('video', 1)

# Dictionary of {Jpeg Name, Jpeg MediaItem} for easy access
jpeg_dict = {}
for jpg in rootFolder.GetClipList():
    if jpg.GetName().endswith(".jpg"):
        jpeg_dict[jpg.GetName()] = jpg


# Loop over each timeline item, and update the corresponding scoreboard's
# Start TC to match up with the start of the point
i = 0
while i < len(tl_clip_list):
    filename = "scoreboard_clipNo_" + str(i) +  "_" + str(i) + ".jpg"
    frame_start = tl_clip_list[i].GetStart()
    media_item = jpeg_dict[filename]
    # Timecode initialize at 30fps and a start frame
    tc = Timecode('30', "00:00:00:00")
    tc += frame_start
    media_item.SetClipProperty("Start TC", str(tc))
    i += 1

    print(f"Set {filename} to start at " + str(tc))

