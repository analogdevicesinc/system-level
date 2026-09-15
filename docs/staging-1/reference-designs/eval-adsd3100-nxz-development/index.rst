.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-development

.. _eval-adsd3100-nxz-development:

EVAL-ADSD3175D Development
==========================

GitHub repo for SDK source code: :git-ToF:`ToF </>`

Doxygen documentation (via the GitHub ToF repo):
https://analogdevicesinc.github.io/ToF/

The SDK API is used to control the setup the camera and SDK, control the camera
and get frames.

There are several examples provided with the SDK:
:git-ToF:`ToF/tree/master/examples <tree/master/examples+>`

The SDK uses the name space **aditof**.

Architecture
------------

Requirements:

- The SDK is put forward as a reference design for customers. Note, the SDK is
  under MIT license.
- The SDK is also used in the EVAL-ADTF3175D evaluation platform.
- Evaluation on Windows and Linux.
- Run without the host on Linux embedded systems.

Case 1: SDK for use in EVAL-ADTF3175D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Device
     - Embedded Linux
     - Channel
     - Host (Windows or Linux)
   * - ADSD3500
     - ucv-app linked with SDK w/Adsd3500Sensorclass and partial depth compute
       **stubs**
     - USB 3.0 UVC
       \* Protobuf is used for commands.
     - User app linked with SDK w/UVC enabled and partial depth compute

Case 2: SDK for use in Embedded Linux SoC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Device
     - Embedded Linux
   * - ADSD3500
     - User app linked with SDK w/Adsd3500Sensorclass and partial depth compute

SDK Version
^^^^^^^^^^^

The following APIs can be used to retrieve version and Git details on the SDK in
use.

- aditof::getApiVersion(): The API version of the SDK.
- aditof::getBranchVersion(): The branch name from which the SDK was built.
- aditof::getCommitVersion(): The commit hash for the SDK.

Return Codes
^^^^^^^^^^^^

The SDK uses the **Status** enum for return codes. See
https://analogdevicesinc.github.io/ToF/namespaceaditof.html#a44f136ae2a9a546362d75a5d73443da9.

--------------

Dissecting the first-frame C++ Example
--------------------------------------

Note, it is expected the following example runs on the NXP directly - and not
the host, being Windows or Desktop Linux.

Source code: :git-ToF?master/examples/first-frame/main.cpp:`/`

Let"s start by looking at some of the basic classes that are needed.

- `System <https://analogdevicesinc.github.io/ToF/classaditof_1_1_system.html>`__
- `Camera <https://analogdevicesinc.github.io/ToF/classaditof_1_1_camera.html>`__
- `CameraDetails <https://analogdevicesinc.github.io/ToF/structaditof_1_1_camera_details.html>`__
- `DepthSensorInterface <https://analogdevicesinc.github.io/ToF/classaditof_1_1_depth_sensor_interface.html>`__
- `Frame <https://analogdevicesinc.github.io/ToF/classaditof_1_1_frame.html>`__
- `FrameDataDetails <https://analogdevicesinc.github.io/ToF/structaditof_1_1_frame_data_details.html>`__

Step 1: Get List of Available Cameras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code block reads a list of cameras discovered by the SDK.

The **System** class is used to obtain the camera list by passing which results
in a vector of **Camera** class objects.

::

   System system;

   std::vector<std::shared_ptr<Camera>> cameras;
   system.getCameraList(cameras);
   if (cameras.empty()) {
       LOG(WARNING) << "No cameras found";
       return 0;
   }

   auto camera = cameras.front();

Step 2: Apply SDK Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this step we specify the SDK configuration JSON file.

::

   status = camera->setControl("initialization_config", configFile);
   if(status != Status::OK){
       LOG(ERROR) << "Failed to set control!";
       return 0;
   }

An example of the JSON file.

::

   {
   "skip_network_cameras": "off",
   "DEPTH_INI": "../config/RawToDepthAdsd3500_lrqmp.ini;../config/RawToDepthAdsd3500_lrmp.ini;../config/RawToDepthAdsd3500_srqmp.ini;../config/RawToDepthAdsd3500_srmp.ini",
   "FPS": "10",
   "FSYNC_MODE": "1"
   }

Step 3: Initialize the Camera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialize the selected camera.

::

   status = camera->initialize();
   if (status != Status::OK) {
       LOG(ERROR) << "Could not initialize camera!";
       return 0;
   }

Step 4 (optional): Display Version Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This optional step returns and displays version details. These details are
populated based on the ADI ToF eval platform. The user may need to populate
these in a different manner in their platform. In which case investigate the
CameraDetails class further.

::

   aditof::CameraDetails cameraDetails;
   camera->getDetails(cameraDetails);

   LOG(INFO) << "SD card image version: " << cameraDetails.sdCardImageVersion;
   LOG(INFO) << "Kernel version: " << cameraDetails.kernelVersion;
   LOG(INFO) << "U-Boot version: " << cameraDetails.uBootVersion;

Step 5: Get Available Frame Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns details on the frame information available from the camera.

::

   std::vector<std::string> frameTypes;
   camera->getAvailableFrameTypes(frameTypes);
   if (frameTypes.empty()) {
       std::cout << "no frame type avaialble!";
       return 0;
   }

To understand what can be returned the please reference the definition of
**availableFrameTypes** in
:git-ToF?master/sdk/src/connections/target/adsd3500_sensor.h:`/`

For the Crosby, the frames are defined in the code block below. From this we can
see the attached camera provides the following modes: lrqm, srqmp, lrmp and
srmp. As well as the types of frames available for each mode and the sizes of
the frames.

::

   const std::vector<aditof::DepthSensorFrameType> availableFrameTypes = {
   {
       "sr-native",
       {{"raw", 1024, 4096},
        {"depth", 1024, 1024},
        {"ir", 1024, 1024},
        {"conf", 1024, 1024},
        {"xyz", 1024, 1024},
        {"metadata", 1, 128}},
       1024,
       4096,
   },
   {
       "lr-native",
       {{"raw", 1024, 4096},
        {"depth", 1024, 1024},
        {"ir", 1024, 1024},
        {"conf", 1024, 1024},
        {"xyz", 1024, 1024},
        {"metadata", 1, 128}},
       1024,
       4096,
   },
   {
       "sr-qnative",
       {{"raw", 2560, 512},
        {"depth", 512, 512},
        {"ir", 512, 512},
        {"conf", 512, 512},
        {"xyz", 512, 512},
        {"metadata", 1, 128}},
       2560,
       512,
   },
   {
       "lr-qnative",
       {{"raw", 2560, 512},
        {"depth", 512, 512},
        {"ir", 512, 512},
        {"conf", 512, 512},
        {"xyz", 512, 512},
        {"metadata", 1, 128}},
       2560,
       512,
   },
   {
       "pcm-native",
       {{"ir", 1024, 1024}},
       1024,
       1024,
   },
   {
       "sr-mixed",
       {{"raw", 2560, 512},
        {"depth", 512, 512},
        {"ir", 512, 512},
        {"conf", 512, 512},
        {"xyz", 512, 512},
        {"metadata", 1, 128}},
       2560,
       512,
   },
   {
       "lr-mixed",
       {{"raw", 2560, 512},
        {"depth", 512, 512},
        {"ir", 512, 512},
        {"conf", 512, 512},
        {"xyz", 512, 512},
        {"metadata", 1, 128}},
       2560,
       512,
   }

};

For the definition of **DepthSensorFrameType** and **DepthSensorFrameContent**,
see :git-ToF?master/sdk/include/aditof/sensor_definitions.h:`/`.

Step 6: Select the Mode/FrameType
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   status = camera->setFrameType("lr-qnative");
   if (status != Status::OK) {
       LOG(ERROR) << "Could not set camera frame type!";
       return 0;
   }

Step 7: Start the Camera
^^^^^^^^^^^^^^^^^^^^^^^^

::

   status = camera->start();
   if (status != Status::OK) {
       LOG(ERROR) << "Could not start the camera!";
       return 0;
   }

Step 8: Read a Frame from the Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   aditof::Frame frame;

   status = camera->requestFrame(&frame);
   if (status != Status::OK) {
       LOG(ERROR) << "Could not request frame!";
       return 0;
   } else {
       LOG(INFO) << "succesfully requested frame!";
   }

Step 9: Get the Data from the Frame
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Stage 0

- Note, this is added for code simplification. Pay attention to Stages 1 and 2.

::

   save_frame(frame, "ir");

Stage 1

- Using the frame retrieved in step 8, request a specific type of data from the
  frame.
- Where the specific frame type data was seen in step 5: raw, ir, depth, …

::

   Status save_frame(aditof::Frame& frame, std::string frameType){

       ...
       uint16_t *data1;
       ....

       status = frame.getData(frameType, &data1);
       if (status != Status::OK) {
           LOG(ERROR) << "Could not get frame data " + frameType + "!";
           return status;
       }

       ...

Stage 2

- Extract details on the frame
- For the definition of FrameDataDetails , see
  :git-ToF?master/sdk/include/aditof/frame_definitions.h:`/`.

::

   ...
   FrameDataDetails fDetails;
   ...
   frame.getDataDetails(frameType, fDetails);
   g.write((char*)data1, fDetails.width* fDetails.height * sizeof(uint16_t));
   ...

first-frame.py
--------------

The following section goes through important chunks of the python example.

:git-ToF:`ToF/tree/master/bindings/python/examples/first_frame_network <tree/master/bindings/python/examples/first_frame_network+>`

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/example1.png
   :width: 400px

Specify IP of all connected cameras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add all of the camera IPs in the list below

::

   IP_addr = ['10.42.0.1']

Trigger mode
^^^^^^^^^^^^

::

   # FSYNC TOGGLE MODE
   # 0 - ADSD3500 Fsync toggled by host command (press enter for next frame)
   # 1 - ADSD3500 Fsync toggled at framerate specified in json file
   # 2 - ADSD3500 Fsync disabled, pin set to HiZ
   fsync_toggle = 1

Initialize Cameras
^^^^^^^^^^^^^^^^^^

Gets cameras based on specified IP

::

   # status = system.getCameraList(cameras)
   status = system.getCameraListAtIp(camera, IP_addr[i])
   print("system.getCameraListAtIp()", status)
   cameras.append(camera[0])

Initialize Cameras
^^^^^^^^^^^^^^^^^^

Initializes camera based on settings in user-defined json file.

::

   cameras[i].setControl("initialization_config", "tof-viewer_config.json")
   status = cameras[i].initialize()
   print("camera"+IP_addr[i]+".initialize()", status)
   cameras[i].setControl("loadModuleData", "call")

Set Frame Type and start camera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   status = cameras[i].setFrameType("lrqmp")
   print("IP_addr[i].setFrameType()", status)
   status = cameras[i].start()
   print("camera"+ IP_addr[i]+".start()", status)

Toggle mode write
^^^^^^^^^^^^^^^^^

::

   cameras[i].adsd3500_set_toggle_mode(fsync_toggle)
   print("camera"+ IP_addr[i]+".adsd3500_set_toggle_mode()", status)

Trigger FSYNC (toggle_mode = 0)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If toggle mode is zero, this requires the user to trigger fsync for each frame

::

   if fsync_toggle == 0:
      input('Press enter for next frame')
      status = cameras[i].adsd3500_toggle_fsync()
      print("camera"+ IP_addr[i]+".adsd3500_toggle_fsync()", status)

Capture frame
^^^^^^^^^^^^^

Call request frame by passing a tof.Frame object.

::

   frames.append(tof.Frame())
   status = camera.requestFrame(frames[i])
   print("camera"+str(i)+".requestFrame()", status)

Frame details
^^^^^^^^^^^^^

After first frame is captured, the frame details are available from the
tof.Frame() object

::

   frameDataDetails = tof.FrameDataDetails()
   status = frames[i].getDataDetails("depth", frameDataDetails)
   print("frame.getDataDetails()", status)
   print("depth frame details:", "width:", frameDataDetails.width, "height:", frameDataDetails.height, "type:", frameDataDetails.type)

Stop Cameras
^^^^^^^^^^^^

::

   for camera in cameras:
      status = camera.stop()
      print("camera"+ IP_addr[cameras.index(camera)]+".stop()", status)
