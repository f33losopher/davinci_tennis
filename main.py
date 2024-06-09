from DaVinci.python_get_resolve import GetResolve
from ProcessVideos.process_timeline import ProcessTimeline
from timecode import Timecode
from Configuration.project_consts import *

import os

# This works only if launched from within DaVinci Resolve
resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

subclip_list = ProcessTimeline(project.GetCurrentTimeline())

# Create a new timeline and add the subclips
mediaPool.CreateEmptyTimeline("Processed Clips")
mediaPool.AppendToTimeline(subclip_list)

# Gather created Scoreboard JPEGs and add them to the media pool
jpgDir = CONFIG[ROOT_MEDIA_FOLDER]
jpgList = []

for filename in os.listdir(jpgDir):
    if filename.endswith('.jpg'):
        jpgList.append(jpgDir + "\\" + filename)
        print("Added: " + filename)

mediaPool.ImportMedia(jpgList)

# Update the property of each JPEG to start at corresponding points
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
    # Timecode initialize at 60fps and a start frame
    tc = Timecode('60', "00:00:00:00")
    tc += frame_start
    media_item.SetClipProperty("Start TC", str(tc))
    print(f"Set {filename} to start at " + str(tc))

    i += 1


