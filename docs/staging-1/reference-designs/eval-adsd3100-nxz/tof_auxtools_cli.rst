.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz/tof_auxtools_cli

.. _eval-adsd3100-nxz tof_auxtools_cli:

Time-of-Flight Python Tools
===========================

5.0.0 or Newer
--------------

See **TOF_Evaluation_ADTF3175D-Rel5.0.0\\bin\\Python-setup\\readme.md**

Setting Up Python
~~~~~~~~~~~~~~~~~

Required: Python 3.10

Windows
^^^^^^^

Installation
''''''''''''

- Install the latest version Python 3.10 64-bit
- In a command-line prompt execute
  TOF_Evaluation_ADTF3175D-Rel5.0.0\\bin\\Python-setup\\aditofpython_env.bat

Usage
'''''

- In a command-line prompt execute
  TOF_Evaluation_ADTF3175D-Rel5.0.0\\bin\\Python-setup\\Activate.bat

Linux
^^^^^

Installation
''''''''''''

- Install the latest version of Python 3.10 64-bit
- Install pyenv

  - sudo apt update
  - sudo apt upgrade
  - sudo apt install python3.10-venv -y

- python3 -m venv py_bindings_env
- source py_bindings_env/bin/activate
- python3 -m pip install –upgrade pip
- python3 -m pip install -r ./requirements.txt

Usage
'''''

- source py_bindings_env/bin/activate

Example: first_frame.py
~~~~~~~~~~~~~~~~~~~~~~~

This is a basic example that shows how to get a single frame from the camera.

Usage:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python first_frame.py
   first_frame.py usage:
   USB: first_frame.py <mode name> <config>
   Network connection: first_frame.py <mode name> <ip> <config>

   Mode names:
   lr-native: 1024 x 1024
   lr-qnative: 512 x 512
   lr-mixed: 512 x 512
   sr-native: 1024 x 1024
   sr-qnative: 512 x 512
   sr-mixed: 512 x 512

   For example:
   python first_frame.py lr-qnative 10.43.0.1 config\config_adsd3500_adsd3100.json

Example:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python first_frame.py lr-qnative 10.43.0.1 config_adsd3500_adsd3100.json
   SDK version:  5.0.0  | branch:  HEAD  | commit:  4b1125e1
   Looking for camera on network @ 10.43.0.1. Will use config_adsd3500_adsd3100.json.
   WARNING: Logging before InitGoogleLogging() is written to STDERR
   I20240719 11:10:10.292093 32168 system_impl.cpp:88] SDK built with websockets version:3.1.0
   I20240719 11:10:10.292093 32168 network_sensor_enumerator.cpp:55] Looking for sensors over network: 10.43.0.1
   [2024/07/19 11:10:10:2941] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   Connection Closed
   I20240719 11:10:10.323288 32168 camera_itof.cpp:97] Sensor name = adsd3500
   system.getCameraList() Status.Ok
   I20240719 11:10:10.323288 32168 camera_itof.cpp:117] Initializing camera
   [2024/07/19 11:10:10:3262] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   Running the python callback for which the status of ADSD3500 has been forwarded. ADSD3500 status =  Adsd3500Status.OK
   Running the python callback for which the status of ADSD3500 has been forwarded. ADSD3500 status =  Adsd3500Status.OK
   I20240719 11:10:13.408497 32168 mode_info.cpp:131] Using new mixed modes table for ADSD3500 w/ADSD3100.
   I20240719 11:10:13.626964 32168 camera_itof.cpp:345] Current adsd3500 firmware version is: 5.1.0.0
   I20240719 11:10:13.627964 32168 camera_itof.cpp:347] Current adsd3500 firmware git hash is: 9f7346c7a973907089afb78234e60fae91da413d
   I20240719 11:10:13.628968 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-qnative.ini
   I20240719 11:10:13.628968 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-native.ini
   I20240719 11:10:13.628968 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-qnative.ini
   I20240719 11:10:13.628968 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-native.ini
   I20240719 11:10:13.628968 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-mixed.ini
   I20240719 11:10:13.628968 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-mixed.ini
   I20240719 11:10:13.629971 32168 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd_pcm-native.ini
   I20240719 11:10:13.629971 32168 camera_itof.cpp:1466] Current Depth ini file is: ./config/RawToDepthAdsd3500_lr-mixed.ini
   W20240719 11:10:13.634976 32168 camera_itof.cpp:385] mipiSpeed is not being set by SDK.
   W20240719 11:10:13.634976 32168 camera_itof.cpp:396] enableTempCompenstation is not being set by SDK.
   W20240719 11:10:13.634976 32168 camera_itof.cpp:406] enableEdgeConfidence is not being set by SDK.
   I20240719 11:10:13.651094 32168 camera_itof.cpp:412] Module serial number: Crosby_DV3_2_07D
   I20240719 11:10:13.651094 32168 camera_itof.cpp:420] Camera initialized
   camera1.initialize() Status.Ok
   camera1.getAvailableFrameTypes() Status.Ok
   ['sr-native', 'lr-native', 'sr-qnative', 'lr-qnative', 'pcm-native', 'sr-mixed', 'lr-mixed']
   camera1.getDetails() Status.Ok
   camera1 details: id: 10.43.0.1 connection: ConnectionType.Network
   I20240719 11:10:13.679083 32168 camera_itof.cpp:1686] Camera FPS set from Ini file at: 16
   W20240719 11:10:13.679083 32168 camera_itof.cpp:1894] vcselDelay was not found in .ini file, not setting.
   W20240719 11:10:13.694092 32168 camera_itof.cpp:1932] enablePhaseInvalidation was not found in .ini file, not setting.
   I20240719 11:10:13.718091 32168 camera_itof.cpp:450] Chosen mode: lr-qnative
   I20240719 11:10:13.722692 32168 camera_itof.cpp:512] Metadata in AB is enabled and it is stored in the first 128 bytes.
   I20240719 11:10:13.722692 32168 camera_itof.cpp:534] Using ini file: ./config/RawToDepthAdsd3500_lr-qnative.ini
   camera1.setFrameType() Status.Ok
   Chosen mode: lr-qnative
   camera1.start() Status.Ok
   camera1.requestFrame() Status.Ok
   frame.getDataDetails() Status.Ok
   depth frame details: width: 512 height: 512 type: depth
   I20240719 11:10:14.536296 32168 network_depth_sensor.cpp:353] Stopping device
   camera1.stop() Status.Ok
   Sensor temperature from metadata:  50
   Laser temperature from metadata:  40
   Frame number from metadata:  0
   Mode from metadata:  3
   Connection Closed

If you see the following error:

::

   C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin\first_frame.py:164: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
     plt.show()

Try saving the file instead, you can do so by changing the last line from:

::

   plt.show()

to

::

   plt.savefig('plot.png')

Example: depth-image-animation-pygame.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example using the Python PyGame engine to demonstrate streaming and
visualization of ToF depth frames.

Usage:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python depth-image-animation-pygame.py
   pygame 2.6.0 (SDL 2.28.4, Python 3.10.11)
   Hello from the pygame community. https://www.pygame.org/contribute.html
   depth-image-animation-pygame.py usage:
   USB: depth-image-animation-pygame.py <mode name> <config>
   Network connection: depth-image-animation-pygame.py <mode name> <ip> <config>

   Mode names:
   lr-native: 1024 x 1024
   lr-qnative: 512 x 512
   sr-native: 1024 x 1024
   sr-qnative: 512 x 512

   For example:
   python depth-image-animation-pygame.py lr-qnative 10.43.0.1 config\config_adsd3500_adsd3100.json

Example:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python depth-image-animation-pygame.py lr-qnative 10.43.0.1 config\config_adsd3500_adsd3100.json
   pygame 2.6.0 (SDL 2.28.4, Python 3.10.11)
   Hello from the pygame community. https://www.pygame.org/contribute.html
   SDK version:  5.0.0  | branch:  HEAD  | commit:  4b1125e1
   Looking for camera on network @ 10.43.0.1. Will use config\config_adsd3500_adsd3100.json.
   WARNING: Logging before InitGoogleLogging() is written to STDERR
   I20240719 11:05:12.387691 37860 system_impl.cpp:88] SDK built with websockets version:3.1.0
   I20240719 11:05:12.387691 37860 network_sensor_enumerator.cpp:55] Looking for sensors over network: 10.43.0.1
   [2024/07/19 11:05:12:3906] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   Connection Closed
   I20240719 11:05:12.419135 37860 camera_itof.cpp:97] Sensor name = adsd3500
   system.getCameraList() Status.Ok
   I20240719 11:05:12.419135 37860 camera_itof.cpp:117] Initializing camera
   [2024/07/19 11:05:12:4221] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   I20240719 11:05:15.501899 37860 mode_info.cpp:131] Using new mixed modes table for ADSD3500 w/ADSD3100.
   I20240719 11:05:15.806041 37860 camera_itof.cpp:345] Current adsd3500 firmware version is: 5.1.0.0
   I20240719 11:05:15.806041 37860 camera_itof.cpp:347] Current adsd3500 firmware git hash is: 9f7346c7a973907089afb78234e60fae91da413d
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-qnative.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-native.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-qnative.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-native.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-mixed.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-mixed.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd_pcm-native.ini
   I20240719 11:05:15.813040 37860 camera_itof.cpp:1466] Current Depth ini file is: ./config/RawToDepthAdsd3500_lr-mixed.ini
   W20240719 11:05:15.853596 37860 camera_itof.cpp:385] mipiSpeed is not being set by SDK.
   W20240719 11:05:15.853596 37860 camera_itof.cpp:396] enableTempCompenstation is not being set by SDK.
   W20240719 11:05:15.854598 37860 camera_itof.cpp:406] enableEdgeConfidence is not being set by SDK.
   I20240719 11:05:15.887208 37860 camera_itof.cpp:412] Module serial number: Crosby_DV3_2_07D
   I20240719 11:05:15.887208 37860 camera_itof.cpp:420] Camera initialized
   camera1.initialize() Status.Ok
   camera1.getAvailableFrameTypes() Status.Ok
   ['sr-native', 'lr-native', 'sr-qnative', 'lr-qnative', 'pcm-native', 'sr-mixed', 'lr-mixed']
   camera1.getDetails() Status.Ok
   camera1 details: id: 10.43.0.1 connection: ConnectionType.Network
   I20240719 11:05:15.917215 37860 camera_itof.cpp:1686] Camera FPS set from Ini file at: 16
   W20240719 11:05:15.917215 37860 camera_itof.cpp:1894] vcselDelay was not found in .ini file, not setting.
   W20240719 11:05:15.932221 37860 camera_itof.cpp:1932] enablePhaseInvalidation was not found in .ini file, not setting.
   I20240719 11:05:15.955276 37860 camera_itof.cpp:450] Chosen mode: lr-qnative
   I20240719 11:05:15.960276 37860 camera_itof.cpp:512] Metadata in AB is enabled and it is stored in the first 128 bytes.
   I20240719 11:05:15.960276 37860 camera_itof.cpp:534] Using ini file: ./config/RawToDepthAdsd3500_lr-qnative.ini
   camera1.setFrameType() Status.Ok
   camera1.start() Status.Ok

At this point a PyGame window will show.

Example: skeletal_tracking.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage:

::

   python skeletal_tracking.py

Example:

::

   (aditofpython_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python skeletal_tracking.py
   WARNING: Logging before InitGoogleLogging() is written to STDERR
   I20240729 15:03:45.976827 20132 system_impl.cpp:88] SDK built with websockets version:3.1.0
   I20240729 15:03:45.976827 20132 network_sensor_enumerator.cpp:55] Looking for sensors over network: 10.43.0.1
   INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
   [2024/07/29 15:03:45:9798] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
   W0000 00:00:1722279825.995760   42780 inference_feedback_manager.cc:114] Feedback manager requires a model with a single signature inference. Disabling support for feedback tensors.
   Connection Closed
   I20240729 15:03:46.007612 20132 camera_itof.cpp:97] Sensor name = adsd3500
   I20240729 15:03:46.008894 20132 camera_itof.cpp:117] Initializing camera
   [2024/07/29 15:03:46:0109] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   W0000 00:00:1722279826.015702   42780 inference_feedback_manager.cc:114] Feedback manager requires a model with a single signature inference. Disabling support for feedback tensors.
   W0000 00:00:1722279826.082868   44924 inference_feedback_manager.cc:114] Feedback manager requires a model with a single signature inference. Disabling support for feedback tensors.
   W0000 00:00:1722279826.102796   44924 inference_feedback_manager.cc:114] Feedback manager requires a model with a single signature inference. Disabling support for feedback tensors.
   I20240729 15:03:49.098778 20132 mode_info.cpp:131] Using new mixed modes table for ADSD3500 w/ADSD3100.
   I20240729 15:03:49.315691 20132 camera_itof.cpp:345] Current adsd3500 firmware version is: 5.1.0.0
   I20240729 15:03:49.315691 20132 camera_itof.cpp:347] Current adsd3500 firmware git hash is: 9f7346c7a973907089afb78234e60fae91da413d
   I20240729 15:03:49.315691 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-qnative.ini
   I20240729 15:03:49.315691 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-native.ini
   I20240729 15:03:49.315691 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-qnative.ini
   I20240729 15:03:49.316612 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-native.ini
   I20240729 15:03:49.316612 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_sr-mixed.ini
   I20240729 15:03:49.316612 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd3500_lr-mixed.ini
   I20240729 15:03:49.316612 20132 camera_itof.cpp:1455] Found Depth ini file: ./config/RawToDepthAdsd_pcm-native.ini
   I20240729 15:03:49.316612 20132 camera_itof.cpp:1466] Current Depth ini file is: ./config/RawToDepthAdsd3500_lr-mixed.ini
   W20240729 15:03:49.318612 20132 camera_itof.cpp:385] mipiSpeed is not being set by SDK.
   W20240729 15:03:49.318612 20132 camera_itof.cpp:396] enableTempCompenstation is not being set by SDK.
   W20240729 15:03:49.318612 20132 camera_itof.cpp:406] enableEdgeConfidence is not being set by SDK.
   I20240729 15:03:49.335511 20132 camera_itof.cpp:412] Module serial number: Crosby_DV3_2_07D
   I20240729 15:03:49.335511 20132 camera_itof.cpp:420] Camera initialized
   I20240729 15:03:49.362991 20132 camera_itof.cpp:1686] Camera FPS set from Ini file at: 16
   W20240729 15:03:49.363996 20132 camera_itof.cpp:1894] vcselDelay was not found in .ini file, not setting.
   W20240729 15:03:49.378095 20132 camera_itof.cpp:1932] enablePhaseInvalidation was not found in .ini file, not setting.
   I20240729 15:03:49.401332 20132 camera_itof.cpp:450] Chosen mode: sr-qnative
   I20240729 15:03:49.406076 20132 camera_itof.cpp:512] Metadata in AB is enabled and it is stored in the first 128 bytes.
   I20240729 15:03:49.407073 20132 camera_itof.cpp:534] Using ini file: ./config/RawToDepthAdsd3500_Traceback (most recent call last):
     File "C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin\skeletal_tracking.py", line 114, in <module>
       status = camera1.requestFrame(frame)

Tool: rawparser.py
~~~~~~~~~~~~~~~~~~

Parses the raw data of frame. This python tool takes the recorded raw frames and
extracts the depth, AB confidence and point cloud data.

Depth frame, AB frame and confidence frame (if qmp mode) are saved as ``.png``
while point cloud data is saved as ``.ply``.

An ``.mp4`` file is also generated to show both AB and depth frames. Metadata of
the recording is saved as a text file.

Usage:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin> python .\rawparser.py
   usage: rawparser.py [-h] [--filename FILENAME]

   Script to parse a raw file and extract different frame data

   optional arguments:
     -h, --help           show this help message and exit
     --filename FILENAME  filename to parse

Example:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin> python .\rawparser.py --filename .\mode_6_frames202407261827.bin

   rawparser version:  1.0.0
   TOF SDK Version:  5.0.0
   filename: .\mode_6_frames202407261827.bin
   The directory .\mode_6_frames202407261827_parsed was created.
   width: 512 height: 512
   file size: 18350720
   frame size: 3670144
   number of frames: 5

Tool: saveCCBToFile.py
~~~~~~~~~~~~~~~~~~~~~~

Saves the Camera configuration file to the local PC.

Usage:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python saveCCBToFile.py
   save_ccb.py usage:
   USB / Local connection: save_ccb.py <config>
   Network connection: save_ccb.py <ip> <config>

Example:

::

   (py_bindings_env) C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin>python saveCCBToFile.py 10.43.0.1 test.ccb
   Looking for camera on network @ 10.43.0.1. Will use test.ccb.
   The directory C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin\ccb_directory was created.
   SDK version:  5.0.0  | branch:  HEAD  | commit:  4b1125e1
   WARNING: Logging before InitGoogleLogging() is written to STDERR
   I20240719 11:20:03.866204 45448 system_impl.cpp:88] SDK built with websockets version:3.1.0
   I20240719 11:20:03.866204 45448 network_sensor_enumerator.cpp:55] Looking for sensors over network: 10.43.0.1
   [2024/07/19 11:20:03:8694] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   Connection Closed
   I20240719 11:20:03.909190 45448 camera_itof.cpp:97] Sensor name = adsd3500
   system.getCameraList() Status.Ok
   I20240719 11:20:03.910121 45448 camera_itof.cpp:117] Initializing camera
   [2024/07/19 11:20:03:9131] NOTICE: Creating Vhost 'default' (serving disabled), 1 protocols, IPv6 off
   Conn established
   I20240719 11:20:07.040855 45448 mode_info.cpp:131] Using new mixed modes table for ADSD3500 w/ADSD3100.
   I20240719 11:20:07.289825 45448 camera_itof.cpp:345] Current adsd3500 firmware version is: 5.1.0.0
   I20240719 11:20:07.289825 45448 camera_itof.cpp:347] Current adsd3500 firmware git hash is: 9f7346c7a973907089afb78234e60fae91da413d
   E20240719 11:20:07.289825 45448 camera_itof.cpp:1483] Couldn't parse config file: test.ccb
   E20240719 11:20:07.290825 45448 camera_itof.cpp:356] Failed to parse Json file!
   camera1.initialize(test.ccb) Status.GenericError
   Module serial number is: Crosby_DV3_2_07D
   camera1.getDetails() Status.Ok
   camera1 details: id: 10.43.0.1
   connection:  ConnectionType.Network
   mode:  sr-native
   mindepth:  67
   maxdepth:  0
   Intrinsic Parameters:
   fx:  776.3651123046875
   fy:  776.4164428710938
   cx:  515.8291625976562
   cy:  517.8092651367188
   codx:  0.0
   cody:  0.0
   k1:  -0.10390078276395798
   k2:  0.08169630914926529
   k3:  0.0799761712551117
   k4:  0.2407972365617752
   k5:  -0.05941573530435562
   k6:  0.16658420860767365
   p2:  7.916953472886235e-05
   p1:  0.00012120820611016825
   I20240719 11:20:07.763866 45448 camera_itof.cpp:1209] Succesfully read chunk number 0 out of 119 chunks for adsd3500!
   I20240719 11:20:13.354241 45448 camera_itof.cpp:1209] Succesfully read chunk number 20 out of 119 chunks for adsd3500!
   I20240719 11:20:18.468591 45448 camera_itof.cpp:1209] Succesfully read chunk number 40 out of 119 chunks for adsd3500!
   I20240719 11:20:23.442203 45448 camera_itof.cpp:1209] Succesfully read chunk number 60 out of 119 chunks for adsd3500!
   I20240719 11:20:28.420989 45448 camera_itof.cpp:1209] Succesfully read chunk number 80 out of 119 chunks for adsd3500!
   I20240719 11:20:33.558063 45448 camera_itof.cpp:1209] Succesfully read chunk number 100 out of 119 chunks for adsd3500!
   I20240719 11:20:38.162081 45448 camera_itof.cpp:1236] Succesfully read ccb from adsd3500. Checking crc...
   I20240719 11:20:38.166188 45448 camera_itof.cpp:1245] Crc of ccb is valid.
   camera1.saveModuleCCB() Status.Ok
   ccb_Crosby_DV3_2_07D_2407191120.ccb saved in C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel5.0.0\bin\ccb_directory
   Connection Closed

4.3.0 or Older
--------------

.. important::

   These tools has been removed from the host starting with Eval Kit version
   5.0.0.

The ADI Time-of-Flight Evaluation package provides additional tools for the
user. These tools are generally secondary software that provide analysis of data
generated by the Time-of-Flight signal chain.

These tools are in the *bin\\tools* folder of the installed software.

In general the auxiliary tools require Python.

.. warning::

   These tools have been only tested on Windows 10 64-bit

Setting up Python
~~~~~~~~~~~~~~~~~

#. Install Miniconda (64-bit): https://docs.conda.io/en/latest/miniconda.html
#. Open the ``Anaconda prompt (Miniconda3)``
#. In the Miniconda prompt, create the virtual environment via environment.yaml

   #. cd <TOF installation folder>\\bin\\tools
   #. conda env create –file environment.yaml –name tof-tools-py39

Using Python
^^^^^^^^^^^^

#. Open the ``Anaconda prompt (Miniconda3)``
#. In the Miniconda prompt, create the virtual environment via environment.yaml

   #. cd <TOF installation folder>\\bin\\tools
   #. conda activate tof-tools-py39

--------------

Depth Compute
~~~~~~~~~~~~~

.. important::

   IMPORTANT: before using, activate the Conda environment as described in
   *Setting up Python*.

**Overview**

tofi_compute_depth application processes the input raw files captured using ADI
ToF system and generates Radial-Depth/AB/XYZ output images.

**Getting Python ready:**

#. Open the ``Anaconda prompt (Miniconda3)``
#. In the Miniconda prompt, create the virtual environment via environment.yaml

   #. cd <TOF installation folder>\\bin\\tools
   #. conda activate tof-tools-py39

**Tool help**

::

   tofi_compute_depth --I=<input_fsf_or_raw_file> --O=<output_path> --CCB=<calibration> --MODE=<mode>
   tofi_compute_depth (-h | --help)
   tofi_compute_depth --version

   Command Line Parameters:
     -h --help      Show this screen
     --version      Show version
     --I=<s>        Input file or folder
     --O=<s>        Output folder
     --CCB=<s>      Calibration Binary [default: 0]
     --MODE=<n>     mode of operation(Mode=10 for 1MP)
     --INI=<s>      INI File (optional)

   Unit Testing Command Line Parameters:
     --CONFIG=<s>   Configuration File [default: 0]
     --b=<s>        Benchmark enable. [default: 0]
     --iterate=<n>  Benchmark number of iterations [default: 1]

**Example Usage**

::

   tofi_compute_depth.exe --I=input_raw_file_folder --CCB=cal_file --MODE=mode --O=output_path

Note: The "mode" setting much match the capture mode of the data in the .bin or
.fsf file(s) and the calibration file (.ccb) should be the corresponding
calibration file used for data capture.

**Example for processing single raw file**

::

   tofi_compute_depth.exe --I=./test_data/MP/raw/frame_1001229429.bin --O=./test_data/MP/  --CCB=./test_data/MP/test_data_example_040638.ccb --MODE=10

Note: The filenames mentioned in the above example are for reference only, they
need to be replaced with correct input/output/calibration CCB filenames.
Microsoft power shell is used as command shell.

**Example for fsf file input with 1 or more frames**

::

   tofi_compute_depth.exe --I ./test_data/QMP/example_12230.fsf --O=./test_data/QMP/ --CCB ./test_data/QMP/fsf_test_12230.ccb --MODE=0

**Output**

\* The output files will be generated in <output_path> folder specified while
running the tofi_compute_depth.

**Visualize Depth Image**

\* Dependency : Requires Python 3.1(or later), numpy, and matplotlib libraries
for visualization. \* The output AB (active brightness) and Radial depth images
can be visualized using the python scripts "visualize_ab.py" and
"visualize_depth.py", with a specific filename.

::

   python visualize_ab.py <file> [width] [height]
   positional arguments:
     file     path to AB data file
   optional arguments:
     width      width of the image (default is 1024)
     height      height of the image (default is 1024)

   python visualize_depth.py <file> [width] [height]
   positional arguments:
     file     path to RadialDepth data file
   optional arguments:
     width      width of the image (default is 1024)
     height      height of the image (default is 1024)

**Example**

::

   python visualize_ab.py test_data\MP\AB\frame_1001229429_0.bin 1024 1024

**Example**

::

   python visualize_depth.py test_data\MP\RadialDepth\frame_1001229429_0.bin 1024 1024

**Visualize Point Cloud**

\* Dependency : Requires Python 3.1(or later) and Open3D library for
visualization. Open3D can be installed using python installer package as ``pip
install open3D``. \* The output XYZ image (point cloud) can be visualized using
the python script ``visualize_pointcloud.py``

::

   python visualize_pointcloud.py [-h] [--version] <width> <height> <xyz_file>

   positional arguments:
     width       width of the image
     height      height of the image
     xyz_file    path to xyz file

   optional arguments:
     -h, --help  show this help message and exit
     --version   show program's version number and exit

**Example**

::

   python .\visualize_pointcloud.py 1024 1024 .\test_data\MP\XYZ\frame_1001229429_0.bin

**Known Issues**

\* The application may crash if wrong calibartion/config data is used. \*
Frames/sec value may be reported incorrectly as "inf", define argument "–b=1" to
return a valid frames/sec estimate.

--------------

FSF Extraction
~~~~~~~~~~~~~~

.. important::

   IMPORTANT: before using, activate the Conda environment as described in
   *Setting up Python*.

FSF is a video file format that is used by Microsoft to store various video data
such as RAW, DEPTH, AB and XYZ. It supports the concept of streams for each of
the data type. This format allows us to capture all video information in a
single file or separate files per stream.

Run the python file to extract FSF information (AB, Depth, Point-Cloud), the
python file uses a JSON file *bound.json* to get the values of
depth_min/depth_max/ab_min/ab_max.

**Getting Python ready**

#. Open the ``Anaconda prompt (Miniconda3)``
#. In the Miniconda prompt, create the virtual environment via environment.yaml

   #. cd <TOF installation folder>\\bin\\tools
   #. conda activate tof-tools-py39

**Example usage with the example FSF file that is included**

*Extract all frames*

::

   python fsf_extract.py data/example_XYZ.fsf

*Extract frame 0 only*

::

   python fsf_extract.py data/example_XYZ.fsf 0 0

*Extract frame 1, 2, 3*

::

   python fsf_extract.py data/example_XYZ.fsf 1 3

**Output is placed into the output folder**

- frame_x_ab_lin.png
- frame_x_ab_log.png
- frame_x_depth_z.png
- frame_x_depth_z_gray16.png
- frame_x_depth_r.png
- frame_x_depth_r_gray16.png
- frame_x.ply

