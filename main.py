from DaVinci.python_get_resolve import GetResolve
from timecode import Timecode

resolve = app.GetResolve()

# Python DaVinci Resolve blade cut a segment in timeline

# Get the current timeline
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

timeline = project.GetCurrentTimeline()

# # Get the current timecode position
timecode = timeline.GetCurrentTimecode()
print(timecode)
print(dir(timecode))

# # Define the start and end timecode for the segment to be cut
# start_timecode = Timecode(10)
# end_timecode = Timecode(20)

# # Cut the segment at the specified timecode range
# Python if else statment
if timeline:
    print("timeline exists")
else:
    print("timeline don't exist")
timelineItems = timeline.GetItemListInTrack('video', 1)
print(timelineItems)

# Python print methods available to an object
print("timeline dir")
print(dir(timeline))
timeline.CreateCompoundClip()

for item in timelineItems:
    print("timelineItem")
    print(dir(item))