from python_get_resolve import GetResolve
import json

def print_obj(text, obj):
    file = open("C:\\Users\\fluuc\\api.md", "a")
    file.write("# " + text + "\n")
    file.write((json.dumps(dir(obj), indent=4)) + "\n")
    file.close()

resolve = app.GetResolve()
print_obj('Resolve', resolve)

pm = resolve.GetProjectManager()
print_obj('Project Manager', pm)

project = pm.GetCurrentProject()
print_obj('Project', project)

mp = project.GetMediaPool()
print_obj('Media Pool', mp)

timeline = project.GetCurrentTimeline()
print_obj('Timeline', timeline)

timelineItems = timeline.GetItemListInTrack('video',1)
timelineItem = timelineItems[0]
print_obj('Timeline Item', timelineItem)

currentVideoIteam = timeline.GetCurrentVideoItem()
print_obj('Current Video Item', currentVideoIteam)