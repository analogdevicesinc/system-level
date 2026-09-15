.. imported from: https://wiki.analog.com/resources/eval/user-guide/adskpmb10-ev-fmcz/zedboard

.. _adskpmb10-ev-fmcz zedboard:

ADSKPMB10-EV-FMCZ Evaluation using ZedBoard™
============================================

General Setup
-------------

The following sections describe the steps for setting up the
:adi:`ADSKPMB10-EV-FMCZ` signal chain kit using ZedBoard™ and the
**PowerhouseApp**.

Evaluation Kit Contents
-----------------------

- Fully Isolated PMOD-to-FMC Board
- PGIA+ADAQ4003 Data Acquisition Board

Equipment
---------

-
  `Zedboard™ <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
  Rev 1.0 or later board
- DC/AC signal source (Audio Precision or similar high performance signal
  source)
- SMA cables
- XLR-SMA interposer board
- SD Card
- Ethernet cable
- Micro-USB to USB type A cable (optional)
- PC running Windows 7, 8, or 10 with Ethernet port

Software
--------

-  :adi:`PowerhouseApp installer <en/resources/evaluation-hardware-and-software/software/software-download.html?swpart=SD_PY3PYSU>`

General Description
-------------------

The :adi:`ADSKPMB10-EV-FMCZ` signal chain kit (Figure 1) is part of the
:adi:`Precision Medium Bandwidth <en/applications/technology/precision-technology/precision-medium-bandwidth.html>`
evaluation board plus series. It is a two-board solution consist of a Precision
Medium Bandwidth Data Acquisition Solution on a PMOD form factor and a Fully
Isolated PMOD-to-FMC interposer board.

The **PowerhouseApp** is a Python-based software that enables control and
evaluation of :adi:`ADSKPMB10-EV-FMCZ` through Zedboard™. The **PowerhouseApp**
showcases an easy-to-use GUI, including options for configuration of the board,
graphical results, and analysis on the common DC and AC parameters of the
:adi:`ADSKPMB10-EV-FMCZ` signal chain kit. Lastly, the **PowerhouseApp** adheres
to software compliance guidelines and licenses.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z01_board_photo.jpg

   Figure 1. ADSKPMB10-EV-FMCZ Evaluation Kit

Getting Started
---------------

The following section contains the installation instructions for the
**PowerhouseApp**, together with the drivers for the ZedBoard™ required for
operation of the software. The evaluation software provides a graphical user
interface (GUI) for quick evaluation of the :adi:`ADSKPMB10-EV-FMCZ`.

Software Installation Procedures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the **PowerhouseApp** installer from the :adi:`ADSKPMB10-EV-FMCZ`
evaluation board page on the Analog Devices website or through this
:adi:`link <en/resources/evaluation-hardware-and-software/software/software-download.html?swpart=SD_PY3PYSU>`

Warning
^^^^^^^

.. warning::

   To ensure that the evaluation system is correctly recognized when it is
   connected to the PC, install the evaluation software and drivers first before
   connecting the :adi:`ADSKPMB10-EV-FMCZ` and ZedBoard™ to the PC.

Installing the PowerhouseApp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

++++ Click here to see the complete installation instructions. \| To install the
**PowerhouseApp**, follow these steps:

#. Make sure you have Python installed in your PC.
#. Download and extract the wheel (.whl) file. Open Command Prompt and type in
   ``cd <directory of the wheel file>`` to go into the directory where the wheel
   (.whl) file is located.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i1aa_directory.png

      Figure 3. Command Prompt: Go into the directory of the installer (.whl
      file)

#. Install **PowerhouseApp** by typing in ``pip install
   powerhouse-1.15.0-py3-none-any.whl``.
   \ *Note: The wheel (.whl) file will find the installation path of the Python
   directory defined in the Windows environment variable path.*

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i1a_directory.png

      Figure 4. Command Prompt: Installing the .whl file

#. If the installation is successful, the user may now close the Command Prompt.

++++

Setting up the SD Card of the ZedBoard™
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

++++ Click here to see the complete setup instructions. \|

#. Mount the SD card into your PC or laptop.
#. Download, extract, and copy the following
   :download:`https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/adskpmb10-ev-fmcz_firmware.zip`
   to the SD card.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i2a_boot_images.png

      Figure 5. Boot Files

#. Eject the SD card and connect it to the Zedboard™.

++++

Configuring the IP Address of the Zedboard™
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

++++ Click here to see the complete configuration instructions. \| Connect the
Zedboard™ to the PC through the Ethernet cable and Micro USB before performing
the following steps:

#. Setup a UART serial communication between your PC and the Zedboard™ using the
   micro-USB cable to USB type A.
#. Using your **Device Manager**, locate the COM port assigned to the Zedboard™.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/fz_01_com_port.png

      Figure 6. Determining the COM Port

#. Open Putty, Tera Term, or other serial terminal program.
#. Setup the terminal between the COM port the Zedboard™ by typing in the
   **Speed** or **Baud rate** to **115200**. The serial terminal connection will
   default to auto login and will automatically go the root directory of the SD
   card.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/fz_02_putty.png

      Figure 7. Setting up the serial terminal connection

#. From here, it is a good idea to check if the connected device can be found
   using the command ``iio_info`` into the terminal, and hitting **Enter**. This
   should provide a list of devices along with their channels and attributes.
#. Type ``ifconfig`` into the terminal, then hit **Enter**. That should echo
   back some information where user can pull out the IP address of the
   Zedboard™. Take note of this information.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/fz_03a_ip.png

      Figure 8. Zedboard™ IP Address

#. In the **Control Panel**, open **Network Connections**. Right Click on the
   Ethernet connected and select **Properties**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i3_ethernet_settings.png

      Figure 9. Network Connections

#. Select the first driver and click **Configure**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i4a_ethernet_driver.png

      Figure 10. Ethernet Properties

#. Click **Use the following IP Address** and type in the following details:
   **IP Address:** change from ``192.168.1.101`` to ``192.168.1.254`` (except
   ``192.168.1.109``)
   **Subnet Mask:** ``255.255.255.0``
   **Default Gateway:** ``192.168.1.100``

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i6a_ethernet_ip.png

      Figure 11. Configuring the Static IP Address

#. See if the configuration is successful by entering ``ipconfig`` in the
   **Command Prompt**. Verify also the connection by doing a ping test. You may
   enter ``ping <IP Address of the Zedboard™>`` or in this case, ``ping
   192.168.1.109``.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/i7a_ethernet_ping.png

      Figure 12. Ping Test with Zedboard™

++++

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The :adi:`ADSKPMB10-EV-FMCZ` connects to the ZedBoard™. The ZedBoard™ board
serves as the communication link between the PC and :adi:`ADSKPMB10-EV-FMCZ`.
Figure 13 shows the connections between the :adi:`ADSKPMB10-EV-FMCZ` and the
ZedBoard™.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z02b_setup.png

   Figure 13. Signal Chain Kit Connection using ZedBoard™

#. Connect the :adi:`ADSKPMB10-EV-FMCZ` securely to the 160-way connector on the
   ZedBoard™. The :adi:`ADSKPMB10-EV-FMCZ` does not require an external power
   supply adapter.
#. Connect the ZedBoard™ to the PC through the Ethernet port. Power it up with
   the 12 V wall adapter included in the kit.

.. warning::

   Connecting through USB cable is for debug purposes only.

Software GUI Setup
------------------

Launching the Software
~~~~~~~~~~~~~~~~~~~~~~

After installing the **PowerhouseApp** (see the Software Installation Procedures
section), run the software with either of the following methods:

- Navigate to the destination folder of the // PowerhouseApp // installer
  selected during the installation procedure and run the powerhouseapp.exe file.
- Search for // PowerhouseApp // in the Start Menu and run the software.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z04_powerhouseappexe.png

   Figure 14. Launching the PowerhouseApp

Establishing Hardware Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the **PowerhouseApp** initializes, the software front panel appears, and
the software automatically connects to any :adi:`ADSKPMB10-EV-FMCZ` evaluation
board connected to the PC. The detected evaluation board"s status is displayed
on the indicator on the lower left front panel at the Graph Tab.

In case there is no hardware connected, a prompt will pop out display indicating
**``No Device Detected!``** (see Figure 15).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z05_connectivity_error.png

   Figure 15. Connectivity Check

Navigating the PowerhouseApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z06a_configuration.png

   Figure 16. PowerhouseApp: ADSKPMB10-EV-FMCZ GUI Software Front Panel
   (Configure Tab View)

Front Panel Overview
^^^^^^^^^^^^^^^^^^^^

The **PowerhouseApp** front panel is shown in Figure 16. The following sections
describe the various software controls accessible on the front panel.

**Graph**

Click **Graph** (Label 1 in Figure 16) to show the measured data and its
corresponding analysis, including the waveform, histogram, and FFT.

.. note::

   User may opt to hide the other displays by clicking on **Analysis** and/or
   the **yellow arrow** located on the lower left of the panel.

**Configuration**

Click **Configuration** (Label 1 in Figure 16) to have access on the controls of
the **PowerhouseApp**. See below **Configure Tab View** section for full details
on this menu.

**Run Once**

Click **Run Once** (Label 2 in Figure 16) to perform a single set of
conversions. The number of conversions performed is set with the **Samples**
dropdown list, which is located to the lower left of the control.

**Run Continuously**

Click **Run Continuously** (Label 2 in Figure 16) to perform repeated sets of
conversions. The number of conversions performed per set is set with the
**Samples** dropdown list.

**Clear Graph**

Selecting **Clear Graph** (Label 2 in Figure 16) removes any previously loaded
evaluation software session files (**.csv**) or data captures.

**Import**

Selecting **Import** (Label 2 in Figure 16) opens the **Load File** dialog box
and the user is prompted to load the previously saved evaluation software
session files (**.csv**).

**Export**

Selecting **Export** (Label 2 in Figure 16) saves the current session in a
**.csv** file. The user is prompted to either choose or enter the path of the
file in the **Save As** dialog box. This saved file can be loaded by the
software at a future time to display previously captured data.

--------------

Configure Tab View
^^^^^^^^^^^^^^^^^^

Figure 16 shows the **Configure** tab view. The **Configure** tab provides
controls for configuring the connected device and software settings. The
Configure tab view contains the following controls and indicators:

- Device (Label 3 in Figure 16): displays the data acquisition device connected.
- Front-End Gain (Label 3 in Figure 16): sets the PGIA Front-end Gain of the
  device. The user can choose from 1, 2, 5, or 10.
- Voltage Reference (VREF) (Label 3 in Figure 16): sets the VREF used in data
  analysis such as when calculating LSB Size, or measured voltage in the
  waveform graph (see the Waveform Tab View section). This control must be set
  to match the VREF used on the connected evaluation board.
- Number of Samples (Label 4 in Figure 16): sets the number of conversions that
  are performed when Single Capture or Continuous Capture is clicked. Adjust
  accordingly with the appropriate throughput.
- Throughput (kSPS) (Label 4 in Figure 16): sets the throughput of the connected
  device. The maximum value of this control is automatically set to reflect the
  maximum achievable throughput of the connected device, given the state of the
  Status Bits and Turbo Mode controls. See the relevant :adi:`ADAQ4003` device
  data sheet for more information on maximum achievable throughput.
- Oversampling Ratio (Label 4 in Figure 16): sets the oversampling ratio applied
  to the captured data. After this control is set to any value other than None ,
  the software sums up the consecutive conversion results together to increase
  effective resolution. The number of conversions summed together is set by the
  Oversampling Ratio control.
- Device Config Settings (Label 5 in Figure 16): configures the connected device
  user configuration register settings. See the relevant ADAQ4003 device data
  sheet for a detailed description of the user configuration register and the
  device features.

  - Status Bits: enables or disables the status bits for the connected device.
  - Span Compression: enables or disables span compression for the connected
    device.
  - High-Z Mode: enables or disables high-Z mode.
  - Turbo Mode: enables or disables turbo mode for the connected device.

- Device configuration settings display (Label 6 in Figure 16): displays the
  status of the user register when Read Register is clicked. Each of the
  following indicators displays the state of the corresponding settings:

  - Status Bits, Span Compression, High-Z Mode, and Turbo Mode status indicators
    indicate whether the corresponding device are reported as enabled or
    disabled in the user configuration register.
  - Overvoltage Clamp Flag: indicates the status of the OV clamp flag in the
    user configuration register of the connected device. When this indicator is
    red, the OV flag is low, indicating the presence of an overvoltage event.

- Read Register (Label 7 in Figure 16): reads the device user register. When
  Read Register is clicked, the contents of the connected device register are
  read to update the Device Config Settings items accordingly.
- Status (Label 8 in Figure 16): indicates information about the current process
  being completed by the evaluation software. The Status Bar includes a Busy
  indicator, which displays if the software is busy performing a task such as
  performing conversions, analyzing results, and so on.

--------------

Waveform Tab View
^^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z07_waveform.png

   Figure 17. Waveform Tab View

Figure 17 shows the **Waveform** tab view. The **Waveform** tab view shows the
time domain representation of the conversion results from the connected device,
as well as several analysis items. The **Waveform** tab view contains the
following controls and indicators:

- Waveform graph (Label 1 in Figure 17): displays the time domain plot of the
  most recently captured or loaded conversion results. The scale and range of
  the waveform graph can be set in the Waveform Analysis box by double clicking
  on the Minimum Value and Maximum Value fields and entering the desired values.
  The waveform graph also includes viewing tools that are described in Graph
  Viewing Controls section.
- Waveform Analysis (Label 2 in Figure 17): shows the following analysis items
  for the currently displayed data.
- Pk-Pk Amplitude: displays the peak-to-peak amplitude of the captured data (the
  difference between the Max Value and the Min Value ).
- Max Amplitude: displays the maximum value measured in the captured data.
- Min Amplitude: displays the minimum value measured in the captured data.
- Mean: displays the arithmetic mean of the captured data.
- Standard Deviation: displays the standard deviation of the captured data.
- Frequency: displays the frequency of the captured data.

--------------

FFT Tab View
^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z09_fft.png

   Figure 18. FFT Tab View

Figure 18 shows the **FFT** tab view. The **FFT** tab displays the calculated
FFT representation of the conversions results from the connected device and
common AC performance metrics. The **FFT** tab contains the following controls
and indicators:

- FFT graph (Label 1 in Figure 18): displays an FFT of the most recently
  captured or loaded conversion results. Set the scale and range of the FFT
  graph by double clicking on the minimum and maximum values along the x-axis
  and y-axis and entering the desired values. The FFT graph also includes
  viewing tools that described in Table 5.
- FFT Analysis (Label 2 in Figure 18): displays common ac performance metrics of
  the captured data. Results are calculated from the FFT spectrum, typically
  ignoring the first six frequency bins.

  - Max Amplitude: displays the maximum value measured in the captured data.
  - Min Amplitude: displays the minimum value measured in the captured data.
  - Pk-Pk Amplitude: displays the peak-to-peak amplitude of the captured data
    (the difference between the Maximum Value and the Minimum Value ).
  - DC: displays the DC value of the captured data.
  - Fund. Frequency: displays the frequency identified as fundamental, the
    frequency bin with the largest signal.
  - Fund. Amplitude: displays amplitude of the fundamental frequency, the
    frequency bin with the largest signal.
  - Dynamic Range: displays the calculated dynamic range.
  - RMS: displays the measured RMS voltage.
  - SNR: displays the calculated signal-to-noise ratio (SNR).
  - THD: displays calculated total harmonic distortion (THD), up to the fifth
    harmonic.
  - SINAD: displays the calculated single-to-noise and distortion ratio (SINAD).
  - Noise Floor: displays the average amplitude of noise frequency bins, more
    specifically, bins not identified as fundamental or harmonic.
  - Bin Width: displays the size of the frequency bins in the FFT graph x-axis.
    The bin width is a function of both the Throughput (kSPS) control (Label 8
    in Figure 16) and the number of samples in the captured data.
  - SFDR: displays the calculated spurious-free dynamic range (SFDR).

--------------

Histogram Tab View
^^^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z08_histogram.png

   Figure 19. Histogram Tab View

Figure 19 shows the **Histogram** tab view. The **Histogram** tab is useful for
performing statistical analysis of the device conversion results, especially
when measuring DC signals. The histogram graph shows the distribution of the
conversion results as well as various statistical analysis items. The
**Histogram** tab contains the following controls and indicators:

- Histogram graph (Label 1 in Figure 19): displays histogram of the most
  recently captured or loaded conversion results. The scale and range of the
  histogram graph can be set by double-clicking on the minimum and maximum axis
  values and entering the desired values. The histogram graph also includes
  viewing tools, described in Table 5.
- Histogram Analysis (Label 2 in Figure 19): shows the following analysis items
  for the currently displayed data.

  - Max Value: displays the maximum value measured in the captured data.
  - Min Value: displays the minimum value measured in the captured data.
  - DC Offset/Mean: displays the arithmetic mean of the captured data.
  - Transition Noise: displays the transition noise of the captured data.
  - Pk-Pk Amplitude: displays the peak-to-peak amplitude of the captured data
    (the difference between the Maximum Value and the Minimum Value ).
  - RMS: displays the measured RMS voltage.
  - LSB: displays the effective size (in μV) of each LSB given the resolution of
    the connected device, and the Voltage Reference (VREF) and Oversampling
    Ratio values selected in the Configure tab.
  - Histogram Width: displays the size of the bins in the histogram graph
    x-axis.

--------------

Summary Tab View
^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adskpmb10-ev-fmcz/z10_summary.png

   Figure 20. Summary Tab View

Figure 20 shows the Summary tab view. The Summary tab simultaneously displays
the waveform, histogram, and FFT graphs and analysis for the device conversion
results on the screen. The Summary tab contains the following controls and
indicators:

- Waveform graph (Label 1 in Figure 20): displays the time domain plot of the
  most recently captured or loaded conversion results. The scale and range of
  the waveform graph can be set by double-clicking on the minimum and maximum
  axis values along the x-axis and y-axis and entering the desired values. The
  waveform graph also includes viewing tools that are described in Graph Viewing
  Controls section.
- FFT graph (Label 2 in Figure 20): displays an FFT of the most recently
  captured or loaded conversion results. The scale and range of the FFT graph
  can be set by double clicking on the minimum and maximum axis values and
  entering the desired values. The FFT graph also includes viewing tools that
  are described in Graph Viewing Controls section.
- Histogram graph (Label 3 in Figure 20): displays the histogram of the most
  recently captured or loaded conversion results. The scale and range of the
  histogram graph can be set by double-clicking on the minimum and maximum
  values along the x-axis and y-axis and entering the desired values. The
  histogram graph also includes viewing tools that are described in Graph
  Viewing Controls section.

- Analysis Summary (Label 4 in Figure 20): shows the following analysis items
  for the currently displayed data.

  - Pk-Pk Amp: displays the peak-to-peak amplitude of the captured data.
  - DC Offset/Mean: displays the arithmetic mean of the captured data.
  - Transition Noise: displays the transition noise of the captured data.
  - Fund. Freq.: displays frequency identified as the fundamental (the frequency
    bin with the largest signal).
  - Fund. Amp.: displays the amplitude of the Fund. Freq.
  - RMS: displays the measured RMS voltage of the captured data.
  - Dynamic Range: displays the calculated dynamic range of the captured data.
  - SNR: displays the calculated SNR of the captured data.
  - THD: displays the calculated THD of the captured data (up to the fifth
    harmonic).
  - SINAD: displays the calculated SINAD of the captured data.
  - LSB: displays the effective size (in μV) of each LSB. The LSB size is a
    function of the resolution of the connected device, the Reference Voltage
    (VREF), and Oversampling Ratio values selected in the Configure tab.
  - SFDR: displays the calculated SFDR of the captured data.

*End of Document*
