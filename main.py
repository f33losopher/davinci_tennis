from DaVinci.python_get_resolve import GetResolve
from timecode import Timecode
from ProcessVideos.process_timeline import ProcessTimeline

resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

# Need to create a map of {clip name, clip object}
clips = dict(map(lambda x: (x.GetName(), x), rootFolder.GetClipList()))

subclip_list = ProcessTimeline(project.GetCurrentTimeline(), clips)

# Create a new timeline and add the subclips
mediaPool.CreateEmptyTimeline("Processed Clips")
mediaPool.AppendToTimeline(subclip_list)