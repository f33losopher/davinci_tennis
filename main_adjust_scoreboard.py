from DaVinci.python_get_resolve import GetResolve

# TODO: Figure out how to add cilps at a certain Time in Timeline
# main.py updates the timecodes of all the JPEGs
# Right click and add them by Timecode
# This script will set the zoom, opacity, and position in top left

resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
timeline = project.GetCurrentTimeline()

# Scoreboard Item List
sb_item_list = timeline.GetItemListInTrack('video', 2)
for sb in sb_item_list:
    sb.SetProperty('Opacity', 50.0)
    sb.SetProperty('ZoomX', 0.40)
    sb.SetProperty('ZoomY', 0.40)
    sb.SetProperty('AnchorPointX', -950)
    sb.SetProperty('AnchorPointY', 540)