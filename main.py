from DaVinci.python_get_resolve import GetResolve
from ProcessVideos.process_timeline import ProcessTimeline
from timecode import Timecode

# This works only if launched from within DaVinci Resolve
resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

# Map clip name to the clip object to create subclips
# {clip name, clip object}
clips = dict(map(lambda x: (x.GetName(), x), rootFolder.GetClipList()))

subclip_list = ProcessTimeline(project.GetCurrentTimeline(), clips)

# Create a new timeline and add the subclips
mediaPool.CreateEmptyTimeline("Processed Clips")
mediaPool.AppendToTimeline(subclip_list)