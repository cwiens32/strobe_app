# Strobe_App
App to create strobe images and videos

## Download App
[Windows](https://drive.google.com/drive/folders/1dolt_Em15a8ZJ6j0nqrgrwboIZYZs0z4) <br/>
Mac (coming soon... :hourglass_flowing_sand: )

## Help Sections
Jump to: <br/>
[File Open](#File-Open) <br/>
[Video Info](#Video-Info) <br/>
[Search Area Options](#Search-Area-Options) <br/>
[Auto Select Frames Options](#Auto-Select-Frames-Options) <br/>
[Strobe Frames](#Strobe-Frames) <br/>
[Frame Comparison](#Frame-Comparison) <br/>
[Pixel Change Options](#Pixel-Change-Options) <br/>
[Create Strobe](#Create-Strobe) <br/>


### File Open
Click on the button [Select video file] to bring up a popup window to identify the video you want to use to create the strobe image/video. <br/>
The default location for the strobe image/video to be saved to is the folder containing the original video.
To change the destination folder for the strobe image/video, click [Select a directory to save to] to select the desired directory.

### Video Info
Insert the sampling rate (frames per second) of the original video.

### Search Area Options
This provides the option to select a specific area in the video frame to 'capture' the object(s) of interest. <br/>
The method do create the strobe image/video uses image subtraction (compares one image to another one and keeps the difference). <br/>
So this option is especially helpful when their is additional movement from frame to frame that you do not want captured in the strobe image/video.  <br/> <br/>
You can select only one of the following options:
* No search area:
  * Do not identify any specific area. Will keep all movements in the entire video frame.
  * This option is best used when the object(s) of interest is the only thing(s) moving from frame to frame. <br/>
* One general search area:
  * You identify one specific area that will be used for all strobe frames.
  * This option is best used when the object(s) of interest is the only thing(s) moving in that specified area.  <br/>
* Search area for each strobe frame:
  * You identify a specific area for EACH strobe frame.
  * This option is best used when there is a lot of extra movement in the video frame that you do not want 'captured.'
  * This option will create the 'cleanest' strobe image/video but also increases the manual effort time required.

### Auto Select Frames Options
Useful to find consistent number of strobe frames with consistent spacing between two events (example, flight phase in the long jump).
If this is what you want, you just need to identify the first strobe frame (ex long jump take-off) and the last strobe frame (ex long jump landing) and the code will auto select a consistent number of frames in between.
* Auto Frame Selection Threshold:
  * How many frames need to be between two manually identified strobe frames for the code to auto select strobe frame(s)?
    * Ex) You specify 5: strobe frames will be automatically identified whenever there are 5 or more frames between strobe frames you manually identified.
* Auto Frame Selection Number:
  * How many strobe frames do you want to automatically identify if the Auto Frame Selection Threshold is met?
    * Ex) You specify 2: 2 strobe frames will be added between each pair of strobe frames you manually identified (as long as the Auto Frame Selection Threshold is met)
        

### Strobe Frames
Click this button to manual identify the frames you want to be 'strobed'. <br/>
Other frames may be added depending on the Auto Frame Selection settings. <br/>
All manually and any automatically identified strobe frames will be displayed next to the button. <br/>
To select the frames, a new window will popup and you will manually search through the video to identify which frame(s) you want to keep.
* Below are the hot keys to operate the strobe frame selections:
  * you can advance using the trackbar but must click button after to update
  * 'k' = -100 frames
  * 'm' = -10 frames
  * ',' = -1 frame
  * '.' = +1 frame
  * '/' = +10 frames
  * ';' = +100 frames
  * click 'q' to select frame when identified in GUI
  * click 'esc' to exit out of GUI

### Frame Comparison
Sets the difference in number of frames that are used for the image subtraction technique. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Ex) If the current frame number is 20, and the 'Change in frame # comparison' number is set at 5, it will compare the current frame (20) to the 5th frame later (25). <br/><br/>
The faster the movement, the lower this number can be. If the object(s) of interest is not moving quickly, increase this number. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;The importance is that in order to create a 'clean' strobe image/video, there must be enough change in the image to pick up the movement.

### Pixel Change Options
Sets the threshold that must be met in order to 'capture' the movement. <br/>
&nbsp;&nbsp;&nbsp;&nbsp;Since this app uses image subtraction, this setting will define how much change in pixel color index must occur in order for the pixel to be 'captured'. <br/>
The lower this number, the less 'noise' there may be but you may possibly lose some of the object(s) of interest. <br/>
The higher this number, the more 'noise' there may be but you will likely capture all of your object(s) of interest. <br/>
With good image contrast in your original video and appropriate settings (search area and frame comparison number) you should be not have to lower this number too much.

### Create Strobe
These steps may take awhile! It depends on the length of your video, please be patient.
* Create Strobe Image:
  * Clicking this button will create the strobe image. You can adjust the settings and re-create the image by clicking the button again.
  * It is saved with the same name as the original video, just with '_strobe.jpg' at the end.
* Create Strobe Video:
  * Clicking this button will create the strobe video. You can adjust the settings and re-create the video by clicking the button again.
  * It is saved with the same name as the original video, just with '_strobe.mp4' at the end.
  