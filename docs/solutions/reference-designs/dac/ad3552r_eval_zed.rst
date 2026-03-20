EVAL-AD3552R Evaluation Board on ZedBoard User Guide
====================================================

**Evaluation Board for the AD3552R, 16-Bit, 2-Channel, Current Output DAC**

|eval-ad3552rfmcxztop-web.gif|

Features
--------

-  Full featured evaluation board for the :adi:`AD3552R`
-  Available in two transimpedance amplifier options
-  Selectable transimpedance gain
-  On-board or external power supply
-  On-board or external voltage reference
-  Clock and trigger inputs for external synchronization
-  Is supported on `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_

Evaluation Kit Contents
-----------------------

-  :adi:`EVAL-AD3552R`

Hardware Required
-----------------

-  16GB (or larger) Class 10 (or faster) micro-SD card
-  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_ Rev D or later board
-  12Vdc, 3A power supply
-  Micro-USB cable
-  Ethernet cable
-  An oscilloscope( In this demo ADALM 2000 is used)
-  User interface setup (choose one):

   -  HDMI monitor, keyboard, and mouse plugged directly into the Zedboard
   -  Host Windows/Linux/Mac computer on the same network as the Zedboard

Software Required
-----------------

-  You need a Host PC (Windows or Linux)
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
-  IIO Scope Download
-  `Kuiper Linux Image <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

General Description
-------------------

The EVAL-AD3552RFMCxZ is an evaluation board for the AD3552R ultrafast 16-bit
precision DAC. The board is available in two variants: EVAL-AD3552RFMC1Z is
optimized for high speed, intended to reproduce dynamic specifications shown in
the datasheet; EVAL-AD3552RFMC2Z is optimized for DC precision and has a much
lower bandwidth, intended to reproduce DC electrical specifications shown in the
datasheet. The difference between these boards is the transimpedance amplifier
and its corresponding feedback capacitor.

.. tip::

   For more informations about hardware specifications, see the :doc:`EVAL-AD3552R Evaluation Board User Guide </solutions/reference-designs/dac/eval-ad3552r>` page.

Quick Start Guide
-----------------

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

To boot the Zedboard and control the :adi:`EVAL-AD3552R`, you will need to install ADI Kuiper Linux on an SD card. Complete instructions, including where to download the SD card image, how to write it to the SD card, and how to configure the system are provided on the `Kuiper Linux page <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for FPGA Projects** on the `Kuiper Linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_ page. Copy the following files onto the boot directory to configure the SD card:

-  **uImage** file for Zynq
-  **BOOT.BIN** specific to your :adi:`EVAL-AD3552R` + ZedBoard
-  **devicetree.dtb** for Zynq specific to your :adi:`EVAL-AD3552R` + ZedBoard

.. important::

   At the moment the AD3552R-EVB is not yet supported in the latest Kuiper Image so these `boot files <resources/ad3552r-boot-files-2025-02-27.zip>`_ should be used.

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

You will need to:

-  Get the `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`_.

|zedboard.png|

-  Insert the SD-CARD into the SD Card Interface Connector (J12).
-  Connect the :adi:`EVAL-AD3552R` board into the ZedBoard FMC connector.
-  Connect USB UART J14 (Micro USB) to your host PC.
-  Plug your ethernet cable into the RJ45 ethernet connector(J11).
-  Plug the Power Supply into the 12V Power input connector (J20) (DO NOT turn the device on).
-  Set the jumpers as seen in the below picture:

.. image:: images/jumpers_boot_sd_zedboard.jpg
   :alt: jumpers_boot_sd_zedboard.jpg
   :align: center
   :width: 400

.. tip::

   Before executing the below steps, make sure that VADJ jumper is set to 1.8V.

-  Connect the oscilloscope probes to the SMB connectors.
-  Turn it on.
-  Wait ~30 seconds for the “DONE” LED to turn blue. This is near the DISP1.

::

   .. image:: images/setup_diagram_eval_ad3552r.jpg

.. esd-warning::

Application Software (both locally and remotely on the FPGA)
------------------------------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The Libiio is a library used for interfacing with IIO devices and is required to
be installed on your computer.

.. admonition:: Download
   :class: download

   Download and Install the latest `Libiio package <https://github.com/analogdevicesinc/libiio/releases>`_ on your machine.

To be able to connect your device, the software must be able to create a context. The context creation in the software depends on the backend used to connect to the device as well as the platform where the :adi:`EVAL-AD3552R` is attached. The Zedboard running ADI Kuiper Linux is currently the only platform supported for the :adi:`EVAL-AD3552R`. The user needs to supply a **URI** which will be used in the context creation.

The `iio_info <https://wiki.analog.com/resources/tools-software/linux-software/libiio/iio_info>`_ command is a part of the libIIO package that reports all IIO attributes.

Upon installation, simply enter the command on the terminal command line to
access it.

For FPGA(Zedboard) Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info

For Windows machine connected to an FPGA(Zedboard):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info -u ip:<ip address of your ip>

Example:

-  If your Zedboard has the IP address 169.254.92.202, you have to use *iio_info -u ip::169.254.92.202* as your URI

.. note::

   Do note that the Windows machine and the FPGA board should be connected to
   the same network for the machine to detect the device.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found on this link\ https://github.com/analogdevicesinc/iio-oscilloscope/releases

-  Once done with the installation or an update of the latest IIO-Oscilloscope, open the application. The user needs to supply a URI which will be used in the context creation of the IIO Oscilloscope and the instructions can be seen in the previous section.
-  Press refresh to display available IIO Devices and press connect.

.. image:: images/iio_connect.png
   :alt: iio_connect.png
   :align: center
   :width: 700

-  Once connected it is possible to set voltage raw values as below:

.. image:: images/output_raw_1_.png
   :alt: output_raw_1\_.png
   :align: center
   :width: 700

PyADI-IIO
~~~~~~~~~

`PyADI-IIO <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_ is a Python abstraction module for ADI hardware with IIO drivers to make them easier to use. This module provides device-specific APIs built on top of the current libIIO Python bindings. These interfaces try to match the driver naming as much as possible without the need to understand the complexities of libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set up PYADI-IIO and install the necessary packages/modules needed by referring to this `link <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_.

Running the example
^^^^^^^^^^^^^^^^^^^

.. admonition:: Download
   :class: download

   Github link for the Python sample script: `AD3552R-EVAL Python Example <https://github.com/analogdevicesinc/pyadi-iio/blob/cn0585_v1/examples/ad3552r_example.py>`_

After installing and configuring PYADI-IIO on your machine, you are now ready to run Python script examples. In our case, run the **ad3552r_example.py** found in the examples folder.

.. important::

   Cyclic mode is actually not enabled by defualt, please edit the file
   examples/ad3552r_example.py and set:

   
   ::
   
       dev.tx_cyclic_buffer = True
   

::

   D:\pyadi-iio>export PYTHONPATH=D:/pyadi-iio/
   D:\pyadi-iio>python examples/ad3552r_example.py ip:your_board_ip

Press enter and you will get these readings:

::

   $ python examples/ad3552r_example.py ip:your_board_ip
   uri: ip:your_board_ip
   sample rate: 33333333
   Sample data min: 1
   Sample data max: 65534

The following window will pop up:

.. image:: images/python_plot_ad3552r.jpg
   :alt: python_plot_ad3552r.jpg
   :align: center
   :width: 700

Schematic, PCB Layout, Bill of Materials
========================================

.. admonition:: Download
   :class: download

   
   -  `EVAL-AD3552RFMC1Z <resources/eval-ad3552rfmc1z.pdf>`_
   -  `EVAL-AD3552RFMC2Z <resources/eval-ad3552rfmc2z.pdf>`_
   -  `EVAL-AD3552RFMCxZ Gerber Files <resources/eval_ad3552rfmcxz_gerber_files.zip>`_
   -  `EVAL-AD3552RFMC1Z Bill of Materials <images/eval-ad3552rfmc1z.xlsx>`_
   -  `EVAL-AD3552RFMC2Z Bill of Materials <images/eval-ad3552rfmc2z.xlsx>`_
   

Reference Demos & Software
--------------------------

-  `PyADI-IIO sources for the EVAL-AD3552R board. <https://github.com/analogdevicesinc/pyadi-iio/blob/cn0585_v1/examples/ad3552r_example.py>`_
-  `Dual Channel, 16-Bit, 33 MUPS, Multispan, Multi-IO SPI DAC Linux device driver. <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dac/axi-ad3552r>`_
-  `AXI-AD3552R HDL IP. <https://wiki.analog.com/resources/fpga/docs/axi_ad3552r>`_
-  `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_
-  `PyADI-IIO Installation Guide <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_
-  `IIO Oscilloscope Installation Guide <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
-  `Kuiper Linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

.. |eval-ad3552rfmcxztop-web.gif| image:: images/eval-ad3552rfmcxztop-web.gif
   :width: 400
.. |zedboard.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad777x-ardz/zedboard.png
   :width: 600
