.. _ad719x_mbed_iio_application:

AD719x IIO Application
======================

Introduction
------------

This page gives an overview of using the ARM platforms supported
(default is Mbed) firmware example with Analog Devices AD719x
Evaluation board and SDP-K1 controller board. This example code
leverages the ADI developed IIO (Industrial Input Output) ecosystem to
evaluate the AD719x device by providing device debug and data capture
support.

.. image:: images/app_interface.png
   :align: center
   :width: 400

.. image:: images/evb_connection_diagram.png
   :align: center
   :width: 400

IIO Oscilloscope is used as a client application running on Windows,
which is an ADI-developed GUI for ADC data visualization and device
debug. The interface used for communicating the client application with
the firmware application (IIO device) is UART. The firmware application
communicates with the IIO device using ADI No-OS drivers and platform
drivers low level software layers. SDP-K1 is used as the controller
board, on which the IIO firmware application runs.

.. note::

   SDP-K1 can also support high speed VirtualCOM port at 1 Mbps or
   higher for faster data transmission.

This code has been developed and tested on the SDP-K1 Controller Board
using the on-board SDP-120 Headers. However, the same code can be used
without or with little modification on any Mbed enabled board which has
Arduino Header support, such as STM32-Discovery, STM32-Nucleo, etc.

Useful links
~~~~~~~~~~~~

- :git-no-OS:`AD719x No-OS drivers <drivers/adc/ad719x>`
- :adi:`AD7190 Product Page <ad7190>`
- :adi:`AD7192 Product Page <ad7192>`
- :adi:`AD7193 Product Page <ad7193>`
- :adi:`AD7194 Product Page <ad7194>`
- :adi:`AD7195 Product Page <ad7195>`

Hardware Connections
--------------------

**Jumper Settings**

SDP-K1: Connect the VIO_ADJUST jumper on the SDP-K1 board to the 3.3 V
position to drive SDP-K1 GPIOs at 3.3 V.

EVAL-AD719X:

- Stack the EVAL-AD719X-ASDZ on the Arduino connectors of the SDP-K1
  board.
- Connect a male-to-male jumper wire between D8 and D12 on the
  Arduino connectors.
- Set the LK7 and LK8 jumper headers to 3.3 V.
- Set LK12 jumper header to position A.

.. image:: images/ad719x_hardware_connection.png
   :align: center
   :width: 600

**UART Connections**

For data transmission to the IIO client, VirtualCOM or UART serial
communication is used. SDP-K1 by default uses the VCOM serial interface
for higher speed data transmission.

SDP-K1 is powered through USB connections from the computer. SDP-K1 acts
as a serial device when connected to a PC, which creates a COM port to
connect to IIO Oscilloscope GUI running on Windows. The COM port
assigned to a device can be seen through the Device Manager.

.. image:: images/ad719x_assigned_com_port.png
   :align: center
   :width: 600

SDP-K1 can support high speed VirtualCOM port USB interface, so by
default VCOM is configured as the default interface in the firmware. The
interface can be set to UART by defining the macro
``USE_PHY_COM_PORT`` in the ``app_config.h`` file.

.. image:: images/ad719x_phy_and_virtual_com.png
   :align: center
   :width: 600

.. image:: images/ad719x_vir_com_port.png
   :align: center
   :width: 600

.. note::

   The actual COM port number for your device may not be the same as
   shown above. Always check your SDP-K1 serial COM port number before
   connecting to the IIO client.

Software Downloads
------------------

MBED Firmware
~~~~~~~~~~~~~

Source code is hosted in the
`precision-converters-firmware <https://github.com/analogdevicesinc/precision-converters-firmware>`__
repository.

Build guide:
:external+precision-converters-firmware:doc:`Precision Converters MBED Firmware <source/build/project_build>`

Libiio: IIO Library
~~~~~~~~~~~~~~~~~~~~

This library provides an abstracted interface to communicate between the
IIO device and the IIO client application (IIO Oscilloscope) without
worrying about the low level hardware details.

- :git-libiio:`Libiio releases <releases>`

IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a GUI-based IIO client application for data visualization and
device configuration/debugging. The data from IIO devices (ADCs/DACs)
is transmitted over Serial/Ethernet/USB link to IIO Oscilloscope through
the abstracted layer of libiio.

- :git-iio-oscilloscope:`IIO Oscilloscope releases <releases>`

Evaluating AD719x Using IIO Ecosystem
--------------------------------------

Ensure that the hardware connection has been made properly between the
Controller Board (SDP-K1) and the ADC Eval board. Also ensure all
software (IIO firmware, libiio, and IIO Oscilloscope) is downloaded and
installed on your computer before trying to communicate with the device.

Running IIO Oscilloscope (Client)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the IIO Oscilloscope application from the start menu and configure
the serial (UART) settings as shown below. Click the refresh button and
the AD719x device should appear in the IIO devices list.

.. image:: images/ad719x_iio_osc_new.png
   :align: center
   :width: 600

Click "Connect" and it should by default open the data "Capture" window.
You can drag aside or close this window to see the main "Debug and DMM"
tab window.

.. image:: images/ad719x_iio_osc_windows.jpg
   :align: center
   :width: 600

Configure/Access Device Attributes (Parameters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope allows the user to access and configure different
device parameters, called "Device Attributes". There are 2 types of
attributes:

- **Device Attributes (Global):** Access/Configure common device
  parameters.
- **Channel Attributes (Specific to channels):** Access/Configure
  channel specific device parameters.

How to read and write an attribute:

- To **read** an attribute, simply select the attribute from the list
  or press the "Read" button on the left side.
- To **write** an attribute, select the attribute value in the "value
  field" and press the "Write" button.

Using DMM Tab to Read DC Voltage on Input Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DMM tab can be used to read the instantaneous voltage applied on
analog input channels. Simply select the device and channels to read
and press the start button.

.. note::

   The voltage is just instantaneous, so it is not possible to get RMS
   AC voltage or averaged DC voltage. Also, when using the DMM tab, do
   not access/use the Data Capture or Debug tab as this could impact
   data capturing. Both DMM scan and data capture use different methods
   of conversion. The DMM data is read using single conversion, while
   data capture uses continuous conversion mode of operation.

.. image:: images/ad719x_iio_osc_dmm.png
   :align: center
   :width: 600

Data Capture from IIO Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To capture data from the AD719x IIO device, simply select the device
and channels to read/capture data. The data is plotted as "ADC Raw
Value" vs "Number of Samples" and is used for visualization. The data
is read as-is from the device without any processing. If the user wants
to process the data, it must be done externally by capturing data from
the serial link on the controller board.

.. note::

   The DMM or Debug tab should not be accessed when capturing data as
   this would impact data capturing. Both DMM scan and data capture use
   different methods of conversion. The DMM data is read using single
   conversion, while data capture uses continuous conversion mode of
   operation.

**Time Domain Plot**

.. note::

   When enabling more than 4 channels, the number of samples should be
   decreased to 200 to avoid timeout in the IIO Oscilloscope.

.. image:: images/ad719x_iio_osc_plot.png
   :align: center
   :width: 600

**Frequency Domain Plot**

.. note::

   Max 4096 samples can be selected for plotting frequency domain
   response due to limited buffer size in the firmware.

.. image:: images/ad719x_iio_osc_fft.png
   :align: center
   :width: 600

Python Environment and Scripts
------------------------------

Data capture, device calibration, etc. can be achieved with Python-based
IIO clients, using the pyadi-iio library. A possible option using ADI's
pyadi-iio library in Python has been demonstrated in the following
sections. The Python scripts are provided along with the firmware
package.

Setting-up Python Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Install Python on your local machine. The scripts are developed and
  tested using Python 3.8.0; version 3.8.0 or newer is recommended.
- Once Python is installed, make sure the environment path (on Windows)
  is set properly. Verify by running ``python --version`` on a command
  line tool such as Git Bash, Command Prompt, or PowerShell.
- Install the pyadi-iio package by running
  ``python -m pip install pyadi-iio``.
- Install additional support packages by running
  ``python -m pip install -r requirements.txt`` from the ``scripts/``
  directory.

.. image:: images/ad719x_iio_python_requirement.png
   :align: center
   :width: 600

Modifying/Running Python Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- All Python scripts specific to the AD719x IIO firmware are stored in
  the ``scripts`` folder in the project directory.
- Ensure that the firmware is compiled with the noise testing mode,
  using the macros in the ``app_config.h`` file.

.. image:: images/ad719x_iio_python_config.png
   :align: center
   :width: 400

- Update the ``uri`` interface in the script according to the COM port
  assigned to your device (SDP-K1). Default COM port is set to COM16 in
  all scripts.
- Update the ``device_name`` variable to match the device name in the
  compiled firmware.

.. image:: images/ad719x_iio_python_com.png
   :align: center
   :width: 600

- Enable the channel and set the size of the sample block for noise
  analysis.

.. image:: images/ad719x_iio_python_samples.png
   :align: center
   :width: 600

**Output Obtained from the Python Script**

While executing ``ad719x_rms_50hz_test.py``, the command prompt requests
the number of samples to be entered by the user. This should be a
multiple of the defined sample block size. On successful completion of
capturing *n* samples, the noise data is displayed on the screen and
the data points are stored in a CSV file as ``adc_data_capture.csv`` in
the folder where the script is located.

.. image:: images/ad719x_iio_python_output.png
   :align: center
   :width: 600

AD719x Firmware Structure
-------------------------

.. image:: images/ad719x_firmware_structure.png
   :align: center
   :width: 600

app_config.h
~~~~~~~~~~~~

This file can be used to:

- Select the active platform using the macro ``ACTIVE_PLATFORM_MBED``
  (only Mbed is supported).
- Select UART baud rate (for physical UART port) using the
  ``IIO_UART_BAUD_RATE`` macro. Default is 230400.
- Select burst capture mode or continuous capture mode using the
  ``DATA_CAPTURE_MODE`` macro.
- Select the active device by defining ``DEV_AD7193``. Default is
  AD7193.
- Uncomment the ``BIPOLAR_MODE`` macro to enable bipolar mode. Default
  is unipolar mode.
- Uncomment the ``DIFFERENTIAL_INPUT`` macro to enable differential
  input. Default is pseudo differential input.

ad719x_user_config.c/.h
~~~~~~~~~~~~~~~~~~~~~~~

These files define the user configurations for the AD719x, such as SPI
parameters (frequency, mode, etc.) and other init parameters used by
No-OS drivers to initialize the AD719x device (gain, data output rate,
reference voltage, etc.).

ad719x_data_capture.c
~~~~~~~~~~~~~~~~~~~~~

This file implements the data capturing logic for the AD719x device.
The data capturing can be done using normal burst mode or continuous
mode.

ad719x_iio.c
~~~~~~~~~~~~~

This file defines getter/setter functions for all the device and channel
specific attributes (related to AD719x devices) to read/write the device
parameters. The majority of device specific functionality is present in
this module.

No-OS Drivers for AD719x
~~~~~~~~~~~~~~~~~~~~~~~~~

The No-OS drivers provide the high level abstracted layer for the
digital interface of AD719x devices. The complete digital interface (to
access the memory map and perform data read) is done in integration with
platform drivers. The functionality related to No-OS drivers is covered
in the following files:

- ``ad719x.c``
- ``ad719x.h``
