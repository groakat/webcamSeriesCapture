# About
This provides a simple graphical user interface to use `SimpleCV` to capture images from a webcam.

Further this script uses a serial connection to control the `quanti-fly`/ `egg-counter`. More information here

https://github.com/dwaithe/quantifly

http://eggcounter.polygonaltree.co.uk/



# Dependencies
- it only work in Linux
- PySide `conda install PySide`
- SimpleCV `pip install simplecv`
- qimage2ndarray (`pip install https://github.com/hmeine/qimage2ndarray/archive/master.zip`)
- pyserial (comes with anaconda)

# Installation guide

# Software

## Preparation

### Install Anaconda
- Download and install Anaconda https://www.continuum.io/downloads (make sure to use version 2.7 and not the 3.x version)
- During installation, install for User only and leave all standard settings like the are

### Install further dependencies
- open `anaconda prompt` 
- type: `pip   install simplecv`, `conda install pyside` (confirm by pressing y) and ` pip install https://github.com/hmeine/qimage2ndarray/archive/master.zip`, `conda install -c menpo opencv3`, `conda install pyserial`

### Install Arduino software/driver
Download the windows installer from http://www.arduino.org/downloads and install it keeping all the standard settings. (a couple of drivers will be installed as well, including the Atmel drivers)


### Install `webcamSeriesCapture`
- type `pip install https://github.com/groakat/webcamSeriesCapture/archive/master.zip`

