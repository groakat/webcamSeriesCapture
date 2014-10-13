# About
This script uses the Python bindings of `gstreamer` and video4linux2 drivers to grab a H264 stream from a webcam like the Logitech C920 or C930.

At set intervals it will retarget the stream to another file. This can be used to save a very long video in 1 minute chunks.

# Dependencies
- it only work in Linux
- gstreamer
- PySide `conda install PySide`
- SimpleCV
- my fork of qimage2ndarray `pip install https://github.com/groakat/qimage2ndarray/archive/master.zip`
- pygame (http://stackoverflow.com/a/19875416)
- opencv `sudo apt-get install libopencv-dev`, `conda install opencv`
- pyserial
