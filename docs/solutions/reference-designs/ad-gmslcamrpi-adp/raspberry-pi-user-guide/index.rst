.. _ad-gmslcamrpi-adp raspberry-pi-user-guide:

Using with Raspberry Pi
=======================

Required Hardware
-----------------

**Development Kits**

- :adi:`AD-GMSLCAMRPI-ADP# GMSL EV Kit Adapter Board <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-gmslcamrpi-adp.html>`
- `Raspberry Pi 4 Model B <https://www.raspberrypi.com/products/raspberry-pi-4-model-b>`__ *(2GB of RAM or more preferred)* or `Raspberry Pi 5 <https://www.raspberrypi.com/products/raspberry-pi-5>`__ *(2GB of RAM or more preferred)*

**Supported Image Sensors & Cameras**

- `IMX219 Raspberry Pi Camera Module 2 <https://www.raspberrypi.com/products/camera-module-v2/>`__
- `Digilent Pcam 5C (OV5640) <https://digilent.com/shop/pcam-5c-5-mp-fixed-focus-color-camera-module/>`__

**Cables**

.. warning::

   Do not use the 15-pin ribbon cable included with the Raspberry Pi camera since that is an opposite sided cable.

*Raspberry Pi 4:*

- 15-Pin Type A (**same side**) Flexible Ribbon Cable, P/N: MP-FFCA10152003A or `similar <https://www.amazon.com/dp/B07RVD2MZV>`__
- 22-Pin Type B (**opposite side**) Flexible Ribbon Cable, P/N: MP-FFCA05222002B or `similar <https://www.amazon.com/dp/B07S1BSPYD>`__
- FAKRA Jack to FAKRA Jack coaxial cable, provided in EV kits

.. figure:: RPI4/adaptor_block_diagram.png

   GMSL Signal Chain - Raspberry Pi 4

*Raspberry Pi 5:*

- 15-Pin Type A (**same side**) Flexible Ribbon Cable, P/N: MP-FFCA10152003A or `similar <https://www.amazon.com/dp/B07RVD2MZV>`__
- 22-Pin Type B (**opposite side**) Flexible Ribbon Cable, P/N: MP-FFCA05222002B or `similar <https://www.amazon.com/dp/B07S1BSPYD>`__
- 22-Pin Type A (**same side**) Flexible Ribbon Cable, P/N: MP-FFCA05222002A or `similar <https://www.amazon.com/dp/B07RVD2GBP>`__
- FAKRA Jack to FAKRA Jack coaxial cable, provided in EV kits

.. figure:: RPI5/adaptor_block_diagram.png

   GMSL Signal Chain - Raspberry Pi 5

Board Modifications
-------------------

Using the procedure to :dokuwiki:`Set CFG Pin Levels <products/gmsl/gui/tools/set_cfg_pin_levels>`, configure the SerDes
pair as follows:

**Serializer CFG Pins**

======== ============================= ============================= =============================
**Pin**   **MAX96717**                  **MAX9295A**                   **MAX96793**
CFG0      **0** – I2C, ROR, 0x80        **0** – I2C, 0x80              **2** – I2C, XTAL, 0x80
CFG1      **7** – Coax, 6 Gbps, Pixel   **0** – Coax, 6 Gbps, GMSL2    **7** – CX, 6 Gbps, Pixel   
======== ============================= ============================= =============================


**Deserializer CFG Pins**

======== ============================= ============================= ============================= ============================= =============================
**Pin**   **MAX96724**                  **MAX96716**                   **MAX96714**                   **MAX96712**                **MAX96792**
CFG0      **0** – I2C, 0x4E             **1** – I2C, 0x54              **2** – I2C, 0x98              **0** – I2C, 0x52           **2** – I2C, 0x54
CFG1      **0** – Coax, 6 Gbps, GMSL    **7** – Coax, 6 Gbps, Pixel    **7** – CX, 6 Gbps, Pixel      **0** – CXTP, GMSL1/2       **5** – CX, 12Gbps, Tunnel
======== ============================= ============================= ============================= ============================= =============================


.. important::

   It is required to set the CFG pins to the indicated levels for this setup.

For more information about the default CFG configuration of each evaluation
board, please visit the respective datasheet documentation:

.. grid::
   :widths: 50% 50%

   .. container::

      - :adi:`MAX96717EVKIT Data Sheet <media/en/technical-documentation/data-sheets/max96717ev.pdf>`
      - :adi:`MAX9295AEVKIT Data Sheet <media/en/technical-documentation/data-sheets/max9295devkit.pdf>`
      - :adi:`MAX96793EVKIT Data Sheet <media/en/technical-documentation/data-sheets/max96717ev.pdf>`

   .. container::

      - :adi:`MAX96724EVKIT Data Sheet <media/en/technical-documentation/data-sheets/max96724-bak-evk-max96724r-bak-evk.pdf>`
      - :adi:`MAX96714EVKIT Data Sheet <media/en/technical-documentation/data-sheets/max96714evkit.pdf>`
      - :adi:`MAX96716EVKIT Data Sheet <media/en/technical-documentation/data-sheets/max96716evkit.pdf>`
      - :adi:`MAX96792AEVKIT Data Sheet <media/en/technical-documentation/data-sheets/max96716evkit.pdf>`

**GMSL Deserializer Evaluation Kit - MAX96724**

- Slide the **SW5** switches to the ON position to enable I2C communication over the CSI bus

  .. figure:: gmsl_deserializer_sw5.jpg
     :width: 200 px

     SW5 Switch for Enabling I2C

- Remove the **J18** and **J19** jumpers to allow the RPi to become the Main host controller for the I2C lines
- Make sure the **J3** is set as default **2-3** position to enable POC


- Bridge **R88** - provides VDDIO to the adapter

  .. figure:: deserializer_resistors.jpg
     :width: 200 px

     R88 for VDDIO Provision

**GMSL Serializer Evaluation Kit - MAX96717**

- Place a jumper on the **J10** connector to enable power over the coaxial cable

  .. figure:: serializer_mods_j10.png
     :width: 200 px

     J10 for Power over Coax

- Bridge **R70** - provides 12V to the adapter
- Bridge **R80** - connects MFP2 to the adapter for camera module (**IMX219**)
- Bridge **R66** - provides VDDIO to the adapter

  .. figure:: serializer_mods_samtec_res.png
     :width: 200 px

     Serializer Resistors

.. important::

   - The board modifications shown above (switches, jumpers and resistor bridges) are specific to the **MAX96724** and **MAX96717** evaluation kits.
   - If using a different SerDes evaluation board, refer to the table below for the correct resistors and consult the board's schematic for the equivalent switch and jumper settings.

**Required Resistor Bridges**

============================== ========================= ===================== ========================
**Serializers**                **12V to Adapter**        **MFP2 to Adapter**   **VDDIO to Adapter**
MAX96717/MAX96793/MAX9295A       R70                      R80                   R66
\
**Deserializers**               **12V to Adapter**        \                    **VDDIO to Adapter**  
MAX96724                         R88                      \                     R98
MAX96716                         R79                      \                     R75
MAX96714                         R98                      \                     R94
MAX96712                         R9                       \                     R1
MAX96792                         R79                      \                     R75
============================== ========================= ===================== ========================

**AD-GMSLCAMRPI-ADP# Adapter**

**Serializer Adapter**

- Configure the switch **S2** on the GMSL Serializer adapter for CAM1 on
  connector **P9**

.. figure:: serializer_interposer_cfg.png
   :width: 300 px

   Serializer Adapter Camera Switches

**Deserializer Adapter**

- Configure the switch **S1** on the GMSL Deserializer adapter for CAM2 on
  connector **P6** and slide switch **S3** towards connector **P6**

.. figure:: deserializer_interposer_cfg.png
   :width: 300 px

   Deserializer Adapter Camera Switches

System Setup
------------

MAX96717 Serializer EV Kit Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the following setup, please ensure ribbon cables and boards are oriented to
match the diagrams.

Connect the 15-pin ribbon cable to the camera board.

.. figure:: step0.png
   :width: 200 px

   Connect the 15-pin Ribbon Cable to Camera Board

Connect the other end of the 15-pin ribbon cable into the 15- to 22-pin adapter
board.

.. figure:: step1.png
   :width: 300 px

   Connect the 15-pin Ribbon Cable to the GMSL Adapter Board (opposite side)

On the other side of the 15- to 22-pin adapter board, connect the 22-pin opposite-sided ribbon
cable.

.. figure:: step2.png
   :width: 350 px

   Connect the 22-pin Opposite-Sided Ribbon Cable to the GMSL Adapter Board

Connect the other end of the 22-pin opposite-sided ribbon cable into the EV Kit adapter board
**P9** connector.

.. figure:: step3.png
   :width: 400 px

   Connect the 22-pin Opposite-Sided Ribbon Cable to the EV Kit Adapter Board (opposite side)

Lastly, connect the EV kit adapter board to the MAX96717 EV Kit.

.. figure:: step4.png
   :width: 400 px

   Connect the EV Kit Adapter Board to the MAX96717 Serializer EV Kit

MAX96724 Deserializer EV Kit Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Raspberry Pi 4**

Starting with the Raspberry Pi 4B, connect the 15-pin ribbon cable to the CSI
input connector.

.. figure:: RPI4/step5.png
   :width: 200 px

   Connect the 15-pin Ribbon Cable to the Raspberry Pi

Connect the other end of the 15-pin ribbon cable into the 15- to 22-pin adapter
board.

.. figure:: RPI4/step6.png
   :width: 300 px

   Connect the 15-pin ribbon cable into the GMSL Adapter Board (opposite side)

On the other side of the 15-to-22 pin adapter board, connect the 22-pin opposite-sided ribbon
cable.

.. figure:: RPI4/step7.png
   :width: 350 px

   Connect the 22-pin Opposite-Sided Ribbon Cable to the GMSL Adapter Board

Connect the other end of the 22-pin opposite-sided ribbon cable into the EV kit adapter board
**P6** connector.

.. figure:: RPI4/step8.png
   :width: 400 px

   Connect the 22-pin Opposite-Sided Ribbon Cable to the EV Kit Adapter Board

Lastly, connect the EV kit adapter board to the MAX96724 EV kit.

.. figure:: RPI4/step9.png
   :width: 600 px

   Connect the EV Kit Adapter Board to the MAX96724 Deserializer EV Kit

With both sides of the SerDes devices connected up, the last step is to connect
the two sides together with the coax cable. The MAX96717 serializer only has one
connection. The MAX96724 deserializer has 4 inputs so connect the coax cable to
link A (INA) on **J7**.

.. figure:: RPI4/gmsl_full_system_config.png
   :width: 600 px

   Full GMSL System Setup

Connect power to the 12V barrel jack **J1** of the MAX96724 deserializer. If
utilizing the GMSL GUI, also connect the micro USB cable to **J6** of the
MAX96724 deserializer EV kit.

**Raspberry Pi 5**

Starting with the Raspberry Pi 5, connect the 22-pin same-sided ribbon cable to the CSI
input connector on **J3**.

.. figure:: RPI5/step5.png
   :width: 200 px

   Connect the 22-pin Same-Sided Ribbon Cable to the Raspberry Pi

Connect the other end of the 22-pin same-sided ribbon cable into the EV kit adapter board
**P6** connector.

.. figure:: RPI5/step6.png
   :width: 400 px

   Connect the 22-pin Same-Sided Ribbon Cable to the EV Kit Adapter Board

Lastly, connect the EV kit adapter board to the MAX96724 EV kit.

.. figure:: RPI5/step7.png
   :width: 600 px

   Connect the EV Kit Adapter Board to the MAX96724 Deserializer EV Kit

With both sides of the SerDes devices connected up, the last step is to connect
the two sides together with the coax cable. The MAX96717 serializer only has one
connection. The MAX96724 deserializer has 4 inputs so connect the coax cable to
link A (INA) on **J7**.

.. figure:: RPI5/gmsl_full_system_config.png
   :width: 600 px

   Full GMSL System Setup

Connect power to the 12V barrel jack **J1** of the MAX96724 deserializer. If
utilizing the GMSL GUI, also connect the micro USB cable to **J6** of the
MAX96724 deserializer EV kit.

Raspberry Pi Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the USB-C power supply to the Raspberry Pi connector
- Connect the HDMI cable from the monitor to the Raspberry Pi micro HDMI connector
- Write the Raspberry Pi latest SD card image on an 8 GB (or more) SD card
- Plug the SD card into the Raspberry Pi SD card slot
- Connect a USB mouse and keyboard to the Raspberry Pi (it is possible to use either a mouse & keyboard combo or a separate mouse and keyboard)

Running the Evaluation Application
----------------------------------

Once Linux boots, you will see the Linux desktop on the HDMI monitor.

**1. Configuring Cameras**

You can either run the configuration command directly (option a) or create a
reusable script (option b).

**a) Running the configuration command directly**

Double-click the **Home** icon and navigate to the
**Workspace/pyv4l2/utils/cam** folder. Right-click inside this folder and
select the **Open Terminal Here** option. Inside the terminal, type the
following command and hit Enter. Make sure to change the command parameters 
according to your setup:

   - ``RPI_MODEL`` (specifies the model of the Raspberry Pi):
                                                            - ``rpi4``
                                                            - ``rpi5``
   - ``CAM_MODEL`` (specifies the model of the camera):
                                                      - ``imx219``
                                                      - ``ov5640``
   - ``CAM_LIST`` (specifies the list of cameras in the setup):
                                                              - ``cam0``
                                                              - ``cam0,cam1``
                                                              - ``cam0,cam1,cam2``
                                                              - ``cam0,cam1,cam2,cam3``
                                                              - ``cam1,cam2``
                                                              - ``cam0,cam3``

.. shell::
   
   $ ./cam.py -p -c <RPI_MODEL>-gmsl-<CAM_MODEL>:<CAM_LIST>

.. figure:: rpi_cam_config.png

   Camera Configuration Command

**b) Creating a video configuration script**

Alternatively, you can create a reusable script. Double-click the **Home** icon
and navigate to the **Workspace** folder. Create a new file named
``video_cfg.sh`` and copy-paste the following content into the file:

.. code-block:: bash

   #!/bin/bash

   CAM_LIST="cam0"
   CAM_MODEL="imx219"
   PYV4L2_PATH="/home/analog/Workspace/pyv4l2"
   DT_MODEL_PATH="/proc/device-tree/model"

   if [[ $(cat $DT_MODEL_PATH | tr -d '\0') =~ "Raspberry Pi 4" ]]; then
      echo "Running on RPI4"
      RPI_MODEL="rpi4"
   elif [[ $(cat $DT_MODEL_PATH | tr -d '\0') =~ "Raspberry Pi 5" ]]; then
      echo "Running on RPI5"
      RPI_MODEL="rpi5"
   else
      echo "Unknown platform"
      exit 0
   fi

   $PYV4L2_PATH/utils/cam.py -c -p "$RPI_MODEL"-gmsl-"$CAM_MODEL":$CAM_LIST

This script configures the Linux V4L2 (Video4Linux2) media pipeline for a GMSL
multi-camera system on a Raspberry Pi. It detects the Raspberry Pi model, sets
the camera configuration, and runs a Python script to apply the settings.

The following variables can be changed (if needed) inside the script:

   - ``CAM_LIST`` (specifies the list of cameras in the setup): 
                                                              - ``cam0`` (default)
                                                              - ``cam0,cam1``
                                                              - ``cam0,cam1,cam2``
                                                              - ``cam0,cam1,cam2,cam3``
                                                              - ``cam1,cam2``
                                                              - ``cam0,cam3``
   - ``CAM_MODEL`` (specifies the model of the camera): 
                                                      - ``imx219`` (default)
                                                      - ``ov5640``
                                                      
The model of the Raspberry Pi does not need to be explicitly specified because the script detects it automatically.

Make sure to change the permissions of the file to make it executable. To do
this, right-click inside this folder and select the **Open Terminal Here**
option. Inside the terminal, type the following command and hit Enter:

.. shell::

   $ chmod +x ./video_cfg.sh

To run the script, type the following command in the terminal and hit Enter:

.. shell::

   $ ./video_cfg.sh

.. figure:: rpi_video_cfg.png

   Raspberry Pi Video Configuration Script

**2. Starting Video Capture**

After the camera configuration is done, click on **Applications** (found in the
top left corner), which will open a dropdown list of items. From this list,
select **Multimedia** and then **Qt V4L2 test Utility** in order to start the
video capture application. After the application opens, press the green play
button to start capturing video.

.. figure:: rpi_running_qv4l2.png

   Video Capture Utility

**3. Viewing the Capture**

The capture window will look as shown below.

.. figure:: rpi_qv4l2.png

   Sample Video Capture

.. note::

   Some displays may have vertical/horizontal lines.
   This is typically an artifact caused on HDMI monitors and unrelated to the
   evaluation setup.

Power-off Sequence
~~~~~~~~~~~~~~~~~~

- Open a terminal and type **sudo poweroff**. This will safely power off the Raspberry Pi and ensure that the SD card is properly unmounted
- Remove the power supply from the Raspberry Pi
- Remove the power supply from the MAX96724 EV kit

Getting the Software
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the
supported processing platforms, and software user guides can be found on the
:git-gmsl:`Analog Devices GMSL GitHub repository </>`.

Tips for Troubleshooting
------------------------

There are a few key commands in the Linux environment that can help identify if
the expected connections and communications have been made.

#. In the Linux environment, you can check to see if the RPi I2C is detecting
   the GMSL boards by sending an I2C detect command [#f1]_ as follows:

   .. shell::

      $sudo i2cdetect -y 10

   The result should look as follows in the terminal, if using the IMX camera:

   .. shell::
      :group: kuiper-gmsl
      :show-user:

      $sudo i2cdetect -y 10
      [sudo] password for analog:
            0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
       00:                         -- -- -- -- -- -- -- --
       10: UU -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       20: -- -- -- -- -- -- -- UU -- -- -- -- -- -- -- --
       30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       60: -- -- -- -- 64 -- -- -- -- -- -- -- -- -- -- --
       70: -- -- -- -- -- -- -- --

   Or, as follows, if using the Pcam camera:

   .. shell::
      :group: kuiper-gmsl
      :show-user:

      $sudo i2cdetect -y 10
      [sudo] password for analog:
            0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
       00:                         -- -- -- -- -- -- -- --
       10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       20: -- -- -- -- -- -- -- UU -- -- -- -- -- -- -- --
       30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
       40: 40 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       50: 50 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
       70: -- -- -- -- -- -- -- --

#. You can also confirm that the *Video for Linux* application is detecting the
   camera and GMSL devices by using the following command:

   .. shell::

      $v4l2-ctl --list-devices

   **Raspberry Pi 4**

   The response should look like the following:

   .. shell::

      $v4l2-ctl --list-devices
       bcm2835-codec-decode (platform:bcm2835-codec):
           /dev/video10
           /dev/video11
           /dev/video12
           /dev/video18
           /dev/video31
           /dev/media2

       bcm2835-isp (platform:bcm2835-isp):
           /dev/video13
           /dev/video14
           /dev/video15
           /dev/video16
           /dev/video20
           /dev/video21
           /dev/video22
           /dev/video23
           /dev/media1
           /dev/media3

       unicam (platform:fe801000.csi):
           /dev/video0
           /dev/video1
           /dev/media4

       rpivid (platform:rpivid):
           /dev/video19
           /dev/media0

   .. note::

      For Raspberry Pi 4, the key idea is to identify the **unicam** output, which corresponds to the Raspberry Pi
      camera setup.

   **Raspberry Pi 5**

   The response should look like the following:

   .. shell::

      $v4l2-ctl --list-devices
      pispbe (platform:1000880000.pisp_be):
            /dev/video20
            /dev/video21
            /dev/video22
            /dev/video23
            /dev/video24
            /dev/video25
            /dev/video26
            /dev/video27
            /dev/video28
            /dev/video29
            /dev/video30
            /dev/video31
            /dev/video32
            /dev/video33
            /dev/video34
            /dev/video35
            /dev/media0
            /dev/media1

      rp1-cfe (platform:1f00110000.csi):
            /dev/video0
            /dev/video1
            /dev/video2
            /dev/video3
            /dev/video4
            /dev/video5
            /dev/video6
            /dev/video7
            /dev/media3

      rpi-hevc-dec (platform:rpi-hevc-dec):
            /dev/video19
            /dev/media2

.. [#f1] More information about these commands found at `mankier.com/8/i2cdetect <https://www.mankier.com/8/i2cdetect>`__.