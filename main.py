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

# Map clip name to the clip object to create subclips
# {clip name, clip object}
# The clip object is required for appending to timeline
clips = dict(map(lambda x: (x.GetName(), x), rootFolder.GetClipList()))

subclip_list = ProcessTimeline(project.GetCurrentTimeline(), clips)

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