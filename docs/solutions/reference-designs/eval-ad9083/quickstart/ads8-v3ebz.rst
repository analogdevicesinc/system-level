.. _eval-ad9083 quickstart ads8-v3ebz:

ADS8-V3EBZ Quick Start Guide
============================

Typical Setup
-------------

.. image:: ../images/ad9083ebz_ads8-v3ebz.jpg
   :width: 650

*Figure 1. AD9083EBZ Evaluation Board and ADS8-V3EBZ Data Capture Board*

Equipment Needed
----------------

- High Quality Analog Signal Source.
- Bandpass filter for the Analog Signal Source.
- The AD9083 PLL Reference Clock, FPGA Reference Clock and FPGA Global Clock
  are provided by the on-board AD9528 JESD204B Clock Generator.
- PC running Windows® with admin privileges and an available ethernet and USB
  port. Windows® 7 and Windows® 10 are currently supported by ACE.

Hardware Needed
---------------

- AD9083EBZ Evaluation Board
- :adi:`ADS8-V3EBZ` High Speed Carrier Card

Software Needed
---------------

- :dokuwiki:`ACE <resources/tools-software/ace>`

Helpful Documents
-----------------

- :adi:`AD9083 Data Sheet <AD9083>`
- `ACE Manual <https://swdownloads.analog.com/ACE/ACE_User_Manual_rev3.pdf>`_
- :adi:`Understanding High Speed ADC Testing and Evaluation - AN-835 <media/en/technical-documentation/application-notes/AN-835.pdf>`

Board Design and Integration Files
-----------------------------------

- `Schematics <https://wiki.analog.com/_media/resources/eval/ad9083/02_059760b.pdf>`_
- `Layout files <https://wiki.analog.com/_media/resources/eval/ad9083/ad9083ebz_revc.zip>`_
- `Bill of materials <https://wiki.analog.com/_media/resources/eval/ad9083/05-059760-01-c.zip>`_

Set Up MicroZed™ Connection
---------------------------

Before performing the evaluation of the AD9083, the Ethernet interface to the
MicroZed™ board must be set up by configuring the network interface between the
PC and the MicroZed™ board.

MicroSD Card for the MicroZed™ Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure proper connection between the microSD card and the MicroZed™ board,
follow these steps:

- Locate the microSD card labeled ADS8-HSx from the contents of ADS8-V3EBZ
  packaging.
- Connect the microSD card to the MicroZed™ board (the contacts of the microSD
  card are face up).
- As a precaution, ensure that the MicroZed™ board is seated properly on the
  ADS8-V3EBZ. Only a visual inspection is needed.

.. image:: ../images/sd-card_location.jpg
   :width: 400

*Figure 2. MicroSD Card Slot in MicroZed Board*

Configure the Network Interface to the MicroZed™ Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the network interface to the MicroZed™ board, follow these steps:

- Ensure that the connections to ADS8-V3EBZ are as shown in Figure 1. It is not
  necessary to connect the AD9083EBZ evaluation board.
- One end of the Ethernet cable can be connected directly to the PC Ethernet
  port or to a USB to Ethernet adapter, with the other end connected to the
  MicroZed™ board.
- Power on the ADS8-V3EBZ board. Allow up to 10 sec for the MicroZed™ board to
  boot up.
- Open the local area connection settings. On Windows 7: Start Menu > Control
  Panel > Network and Sharing Center > Change adapter settings. On Windows 10:
  Start Menu > Settings > Network & Internet > Change adapter options.
- If the Local Area Connection icon does not appear in the Network Connections
  window, unplug the Ethernet connection from the MicroZed™ board and then
  reconnect it.
- Double click the Local Area Connection icon that appears.
- Click Properties.
- Select Internet Protocol Version 4 (TCP/IPv4).
- Click Properties.
- Enter 192.168.0.1 in the IP address field.
- Ensure the Subnet mask field shows 255.255.255.0.
- Click OK.

Evaluation Software Configuration
-----------------------------------

Download and run the ACE installer from the :adi:`ACE web page <ace>`. After
the ACE software is installed, the user must install the plugin for the AD9083
evaluation board. There are two options for installing the plugin, as described
in the following sections.

Plugin Installation from ACE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installing plugins can be performed using the Plug-in Marketplace feature in the
ACE software as described in this section. Plugins can also be downloaded from
the ACE software page by searching for the relevant device number within the ACE
software.

To install a plugin from ACE, follow these steps:

- From the Start menu, click All Programs > Analog Devices > ACE to open the
  main ACE software window.
- In the left pane, click Plug-in Manager. The Manage Plug-ins window opens, as
  shown in Figure 3.
- Click the Available Packages dropdown menu on the left side of the software
  window.
- Enter the AD9083 in the search bar on the right side of the window to search
  for the device that is intended for evaluation and find the appropriate board
  plugin.
- Select the AD9083 plugin and click Install Selected.
- Click Close.

.. image:: ../images/ace_plug-ins.png
   :width: 600

*Figure 3. ACE Manage Plug-ins Window*

Plugin Installation from the Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the plugin from the web, follow these steps:

- Ensure that the ACE software is installed.
- From the ACE software page on the Analog Devices, Inc.,
  :adi:`ACE web page <ace>`, navigate to the ACE Evaluation Board
  Plug-ins section and search for the device to evaluate.
- Click the AD9083 board plugin. The board plugin automatically downloads to the
  PC. When the download is complete, locate the downloaded file. Note that if
  the browser used for the plugin download is Internet Explorer, the file
  extension of the plugin file is .zip. If this occurs, right click the file and
  rename the file extension to .acezip.
- Double click the .acezip file to automatically install the plugin.
- The plugin installation process opens the ACE software. Close ACE after plugin
  installation completes.

Introduction to the AD9083 Plugin
-----------------------------------

The AD9083 plugin allows the user to evaluate the AD9083 chip via the AD9083EBZ
evaluation board. The AD9083EBZ provides the power and clocking necessary to
evaluate the AD9083 16-Channel ADC. The Power Delivery Network is powered by a
LTM8074 1.2A Silent Switcher µModule Regulator and clocking is provided by an
AD9528 JESD204B Clock Generator. The reference for the AD9528 is an on-board 100
MHz VCXO.

The AD9083EBZ Plugin will configure the AD9083 using the API. The Plugin
generates the API commands, which are then downloaded to the MicroZed™, which in
turn configures the AD9083.

The Plugin will also configure the AD9528 using the clocking requirements from
the Startup Wizard.

To start using the AD9083EBZ, first ensure the board is connected as shown in
Figure 1. Next, ensure that the ADS8-V3EBZ board is powered on before opening
ACE. When the user opens the ACE software, the plugin appears in the Attached
Hardware section of the ACE GUI (see Figure 4).

.. image:: ../images/ad9083ebz_ads8-v3ebz_data_capture.png
   :width: 600

*Figure 4. AD9083EBZ Evaluation Board and ADS8-V3EBZ Data Capture Board*

Board View
~~~~~~~~~~

Double clicking the board icon in the Attached Hardware section in ACE opens the
AD9083EBZ board view.

The board view tab enables the user to quickly set up the AD9083. Figure 5 shows
the STARTUP WIZARD pane within the AD9083EBZ board view. It may take several
moments for the board view to initialize.

.. image:: ../images/ad9083ebz_quick_configuration.png
   :width: 800

*Figure 5. AD9083EBZ Evaluation Board Quick Configuration*

Chip View
~~~~~~~~~~

Double clicking the AD9083 icon in the board view opens the chip view. The chip
view enables the user to customize the AD9083 beyond the functions available in
the board view.

.. image:: ../images/ad9083ebz_configuration.png
   :width: 600

*Figure 6. AD9083EBZ Chip View*

Evaluation
----------

The AD9083 can be configured in many different ways. We will provide examples
for several configurations here.

Wide Bandwidth Real Output Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameters:

- Sample rate = 2 GSPS.
- On-chip PLL reference = 250 MHz (Provided by the on-board AD9528).
- fINMAX = 100 MHz (sample rate/20).
- fC = 800 MHz.
- VMAX = 2.0 V.
- RTERM = 100 Ω.
- EN_HP = 0
- Backoff = 0
- CIC decimator = bypass.
- Use mixer? = No.
- Decimate by J = 8.
- Transport parameters L, M, F, S, N', K = 4, 16, 6, 1, 12, 32.
- 4 lanes at 15 Gbps each.

Steps:

- Configure the AD9083 and AD9528 using the AD9083EBZ STARTUP WIZARD using the
  parameters listed above.
- Click "Apply". It will take several moments for the configuration to complete.
- Navigate to Analysis.
- Click "Run Once".

You should see an FFT after setting up the board as shown and running the macro.

.. image:: ../images/ad9083ebz_FFT.png
   :width: 600

*Figure 7. AD9083EBZ Wide Bandwidth Real Output Mode Typical FFT*

Narrow Bandwidth Complex Output Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This configuration is suitable for applications such as phased-array radar. The
output bandwidth is ± 12.7187 MHz. This example uses an analog input frequency
of 70.5 MHz and the NCO frequency is 70.3125 MHz. Using the AD9083EBZ Startup
Wizard, configure the AD9083 using the parameters below.

Parameters:

- Sample rate = 2 GSPS.
- On-chip PLL reference = 250 MHz (Provided by the on-board AD9528).
- fINMAX = 100 MHz (sample rate/20).
- fC = 800 MHz.
- VMAX = 2.0 V.
- RTERM = 100 Ω.
- EN_HP = 0
- Backoff = 0
- NCO0/mixer (complex data), FTW = 70.3125 MHz.
- CIC decimator = 4.
- Decimate by J = 16.
- Transport parameters L, M, F, S, N', K = 2, 32, 32, 1, 16, 32.
- 2 lanes at 10 Gbps each.

Steps:

- Configure the AD9083 and AD9528 using the AD9083EBZ STARTUP WIZARD using the
  parameters listed above.
- Click "Apply". It will take several moments for the configuration to complete.
- Navigate to Analysis.
- Click "Run Once".

You should see an FFT after setting up the board as shown and running the macro.

.. image:: ../images/ad9083ebz_narrow_bw_complex_output_mode_typicalFFT.png
   :width: 600

*Figure 8. AD9083EBZ Narrow Bandwidth Complex Output Mode Typical FFT*

Precision Time Domain Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameters:

- Sample rate = 1 GSPS.
- On-chip PLL reference = 125 MHz (Provided by the on-board AD9528).
- VMAX = 1.8 V.
- RTERM = 100 Ω.
- fC = 800 MHz.
- High Performance Mode = False.
- Fin Max = 50 MHz (sample rate/20).
- Backoff = 0.
- # ADC Channels = 16.
- Bypass CIC = False.
- CIC decimator = 8.
- Use Mixer? = False.
- Decimate by J = Bypass (Decimate by 1).
- jtx_subclasv_cfg = 0.
- Lanes (L) = 3.
- Virtual Converters (M) = 16.
- (Octets/Frame)/Lane (F) = 8.
- Bits Packed (NP) = 12.
- Resolution Bits (N) = 12.
- Frames in a multi-frame (K) = 32.
- 3 lanes at 10 Gbps each.

Steps:

- Configure the AD9083 and AD9528 using the AD9083EBZ STARTUP WIZARD using the
  parameters listed above.
- Click "Apply". It will take several moments for the configuration to complete.
- Navigate to Analysis.
- Click "Run Once".

You should see an FFT after setting up the board as shown and running the macro.

.. image:: ../images/ad9083ebz_precision_time_domain_typicalFFT.png
   :width: 600

*Figure 9. AD9083EBZ Precision Time Domain Mode Typical FFT*

External Trigger
----------------

SMA connector J2 on the ADS8-V3EBZ can be used as an optional trigger so that the
data capture start time can be controlled. The trigger requires a 1.8V active
high pulse width that is longer than the FPGA internal peripheral clock, which
has a frequency of 50 MHz. To enable the external trigger:

1. Click on "Navigate to FPGA SPI" on the block diagram of the AD9083 Chip View.

.. image:: ../images/navigate_to_fpga_spi.png
   :width: 600

2. Click on the "+" sign next to Address (Hex) 0106.

.. image:: ../images/0106.png
   :width: 600

3. Click on the "0" that is on the same row as "ext_trig_en". The 0 will change
   to a 1.

.. image:: ../images/ext_trig_en.png
   :width: 600

4. Click "Apply Changes".

.. image:: ../images/apply_changes.png
   :width: 100

SMA connector J3 is normally used as a system ready indicator. It indicates that
the FPGA is ready to accept an external trigger.

To capture data, click on "Run Once" as normal. Capture will begin once 1.8V is
detected on connector J2 of the ADS8-V3EBZ.

Troubleshooting Notes
---------------------

Evaluation Board is not Functioning Properly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible that a board component has been rendered inoperable by ESD,
removing a jumper during powered operation, accidental shorting while probing,
etc. Try checking the supply domain voltages of the power adapter board while it
is powered. They should be as follows:

====== ========== ===============
Domain Test Point Approx. Voltage
====== ========== ===============
12V_IN TP19       12V
V1P0V  TP6        1V
V1P8V  TP14       1.8V
====== ========== ===============

Evaluation Board is not Communicating with the ADS8-V3 / No SPI Communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Make sure the USB cable is making good connection on the ADS8-V3EBZ board and
  the PC. Try another USB port on the PC if needed. Some PCs work best with a
  SuperSpeed USB 3.0 port.

  - The ADS8-V3EBZ should show up on the PC Device Manager.

- Make sure that the FPGA on the ADS8-V3 has been programmed — a lit FPGA_DONE
  LED DS15 on the top of the ADS8-V3 and a powered fan are good indicators of
  the FPGA being programmed.
- Check the common mode voltage on the JESD204B traces. On the evaluation board,
  the common mode voltage should be roughly 0.5V. On the ADS8-V3, the common
  mode voltage should be around 0.8V.
- To test SPI operation, attempt to both read and write to register 0x000A
  (Scratch Pad Register) using ACE's Register Debugger. If the register reads
  back the same value written to it, SPI is operational.

  - All registers reading back as either all ones or all zeros (i.e., 0xFF or
    0x00) may indicate no SPI communication.
  - Register 0x0000 (SPI Configuration A) reading back 0x81 in ACE may indicate
    no SPI communication as a result of the FPGA on the ADS8-V3 not being
    programmed.

Evaluation Board Fails to Capture Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Ensure that the board is functioning properly and that SPI communication is
  successful — see previous troubleshooting tips.
- Check the signal generator input on connector J20. Using SPI, read the On-Chip
  PLL lock Detect register 0xD44 to see if the on-chip PLL is locked. Try
  placing a differential oscilloscope probe on the clock pins to see if the
  clock signal is reaching the chip.
- Check the JESD204B PLL Locked indicator or register 0x301F (PLL Status). If
  the light in the plugin chip view is green / if the register reads back 0x80,
  the PLL is locked. If it is not locked:

  - Restart the evaluation board setup (power cycle FPGA, start a new session in
    ACE) by following the instructions from the start.
  - Make sure P3 (Power Down / Standby Jumper) is not jumped.
