# DaVinci Resolve Python API
## Version 1.18

This project takes a Timeline with markers to indicate when points start and who won a point. This program will
- Parse markers in a timeline
- Tally up points as they progress
- Create scoreboard images of each point to embed in video
- Creates a new timeline with subclips of points marked
- Update the Timecode of Scoreboard images to start at corresponding points

## How to Use the program
### In DaVinci Resolve
Mark the clip itself **not the Timeline**  for start/end points
 - Blue - Start of point
 - Cyan - End of point for player/team 1
 - Green - End of point for player/team 2

 **NOTE** Marker colors are selected in DaVinci Resolve. You can set shortcut keys for each color

After markers are inserted, in the menu bar select: Workspace -> Scripts -> Comp -> main

 You will see a new Timeline "Processed Clips" and JPEGs corresponding to the points. After all the Start TC updates complete on each JPEG, select all the scoreboard images in the Media Pool, Right Click, Select "Insert Selected Clips to Timeline using Timecode"

There is a second process to change the size/opacity of the scoreboard
In the menu bar select: Workspace -> Scripts -> Comp -> main_adjust_scoreboard 

Stil have to manually position the scoreboard in the desired position. You can select ALL the clips in the timeline and move all scoreboards at one time

### Setup
Requires Python 3.6 or greater

Clone the repository into the following location and DaVinci Resolve will see the scripts
- %APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Comp