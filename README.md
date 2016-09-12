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
- type: `pip   install simplecv`, 
- `conda install pyside` (confirm by pressing y) and 
- ` pip install https://github.com/hmeine/qimage2ndarray/archive/master.zip`, 
- `conda install -c menpo opencv3`, 
- `conda install pyserial`

### Install Arduino software/driver
Download the windows installer from http://www.arduino.org/downloads and install it keeping all the standard settings. (a couple of drivers will be installed as well, including the Atmel drivers)


### Install `webcamSeriesCapture`
- type `pip install https://github.com/groakat/webcamSeriesCapture/archive/master.zip`

### Setup Shortcut
- right-click on Desktop
- new -> shortcut
- set as location: `python.exe C:\Users\XXXXX\Anaconda2\Lib\site-packages\webcamSeriesCapture\acquisition\acquisition.py` (replace `XXXXX` with the name of the `C:\Users\` folder of the active user)

## Camera Configuration
### Logitech webcam driver
Download logitech driver from http://support.logitech.com/en_us/product/hd-pro-webcam-c920#download

## Example Camera configuration

- In the system tray (bottom right next to the clock) click on the small webcam icon (right click) -> Logitech Webcam Controller.
- Click `Webcam options` (make sure it is expanded)
- Click `Advanced Settings` at the bottom
- Make sure that all checkboxes are unticked (RightLight, Auto) to be able to move all sliders
- Change settings so that the live image looks like the reference image
- also: **make sure to switch auto-focus off!** (in the small window)

![exmaple camera](https://github.com/groakat/webcamSeriesCapture/raw/master/camera_reference.png)
