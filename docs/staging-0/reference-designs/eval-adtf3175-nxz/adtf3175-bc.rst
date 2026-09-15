.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175-bc

.. _eval-adtf3175-nxz adtf3175-bc:

EVAL-ADTF3175-NXZ Block Diagram
===============================

This page provides a high level overview of the
:dokuwiki:`EVAL-ADTF3175-NXZ </resources/eval/user-guides/eval-adtf3175-nxz>`
evaluation platform. This system is showcases the ADTF3175 ToF module.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/crosbyonly.png

ADTF3175
--------

The ADTF3175 is a complete Time-Of-Flight (ToF) module for high resolution 3D
depth sensing and vision systems. Using the ADSD3100 ToF image sensor, the
ADTF3175 also integrates the lens and optical band-pass filter for the imager,
an infrared illumination source containing optics, laser diode driver and
photodetector, a flash memory, and power regulators to generate local supply
voltages.

**Product Page**

**IMAGE OF CROSBY**

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/adtf3175_simplified.png

For full block diagram please refer to datasheet

\* Link to ADSD3100 datasheet \* Link to NVM

NVM Contents
~~~~~~~~~~~~

- ADSD3100 FW (Not used for EVAL-ADTF3175-NXZ)
- ADTF3175 module calibration
- ADSD3500 FW (Only needed by ADSD3500)

`Click here NVM structure details <https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175-nxz/nvm>`__

EVAL-ADTF3175-NXZ Usecase
~~~~~~~~~~~~~~~~~~~~~~~~~

The ADTF3175 is powered up and programmed by a configuration file provided by
the host (PC). The calibration data stored on its NVM are read by the
application processor (SPI) and reprogrammed on the ADSD3100.

Once the ADSD3100 on the module is configured, FSYNC can by provided to start
the capture of data. The imager outputs data via MIPI (4-Lane upto 1.464 Gbps
per lane).

NXP i.IMX8M SOM + Carrier Board
-------------------------------

An NXP i.MX8M SOM is used as the embedded devkit for this evaluation platform. A
carrier board attached to the SOM generates supply rails for ADTF3175 and SOM,
and provides IO ports.

- :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/carrier-schematic.pdf`

- :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/som_carrier-datasheet.pdf`

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/nxp_carrier.png

NXP i.MX8M reference drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Custom V4L2 Camera Sensor Driver
- USB Video Driver (UVC)

EVAL-ADTF3175-NXZ Usecase
~~~~~~~~~~~~~~~~~~~~~~~~~

Reference image for the NXP SOM is provided on the ADI ToF github page (links
below). The SOM is used as a passthrough between the PC and the ADTF3175. It
generates FSYNC and handles raw data via MIPI. The data can then be converted to
any of the IO ports provided on the carrier board (List of reference drivers
provided above).

Host PC
-------

The Host PC captures data provided by the SOM through network or USB 3.0
(USB-C), and also provides power to the evaluation platform via Power Delivery
2.0 (USB-C).

Once raw data is received by the SDK, the data run through a depth compute
library to generate radial depth, active brightness and confidence data. XYZ
data can also be generated using the lens calibration parameters stored on the
ADTF3175 NVM.

Simplified Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/hostpc.png

SDK
~~~

An open source SDK for this evaluation platform is provided on
:git-ToF:`ToF </>`. The SDK also requires the depth compute libraries which are
provided as binaries in the installer @ :git-ToF:`ToF/releases/ <releases/+>`.

The SDK comes with a GUI and first frame examples. As well as bindings for
Python, OpenCV, ROS and Open3D.

EVAL-ADTF3175-NXZ Usecase
~~~~~~~~~~~~~~~~~~~~~~~~~

The PC is used to provide the ADSD3100 FW to the ToF module, as well as convert
incoming raw data to depth.

Data generated from depth compute:

- Radial Depth : Distance from the center of the lens to the scene
- Active Brightness : IR image
- Confidence : byproduct of depth computation, used to invalidate unreliable
  data
- XYZ : Point cloud data
