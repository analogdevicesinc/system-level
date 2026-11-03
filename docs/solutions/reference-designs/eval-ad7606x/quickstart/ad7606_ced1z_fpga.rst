.. _ad7606_ced1z_fpga:

CED1Z FPGA Project for AD7606 with Nios II
===========================================

Supported Devices
-----------------

- :adi:`AD7605`
- :adi:`AD7605-4`
- :adi:`AD7606`
- :adi:`AD7606-6`
- :adi:`AD7606-4`

Evaluation Boards
-----------------

- :adi:`EVAL-AD7605EDZ <EVAL-AD7605-4>`
- :adi:`EVAL-AD7605-4`
- :adi:`EVAL-AD7606EDZ`
- :adi:`EVAL-AD7606-6EDZ`
- :adi:`EVAL-AD7606-4EDZ`

Overview
--------

This document presents the steps to set up an environment for evaluating the
:adi:`EVAL-AD7606EDZ`, :adi:`EVAL-AD7606-6EDZ`, or :adi:`EVAL-AD7606-4EDZ`
evaluation board together with the :adi:`EVAL-CED Converter Evaluation and
Development (CED) Board` and the Nios II Embedded Development Suite (EDS).

.. image:: ../images/ced1z_ad7606.png
   :align: center
   :width: 600

The CED1Z board is intended for use in evaluation, demonstration, and
development of systems using Analog Devices precision converters. It provides
the necessary communications between the converter and the PC: programming or
controlling the device, transmitting or receiving data over a USB link.

The :adi:`AD7606`, :adi:`AD7606-6`, and :adi:`AD7606-4` are 16-bit, 8/6/4
channel, simultaneous sampling Analog-to-Digital Data Acquisition systems
(DAS). They contain analog input clamp protection, a second-order anti-alias
filter (22 kHz, 3 dB cutoff), track-and-hold amplifier, 16-bit charge
redistribution successive approximation ADC, flexible digital filter, 2.5 V
reference and reference buffer, and high-speed serial and parallel interfaces.

These devices operate from a single 5 V supply and can accommodate ±10 V and
±5 V true bipolar input signals while sampling at throughput rates up to
200 kSPS for all channels. The input clamp protection circuitry can tolerate
voltages up to ±16.5 V. The AD7606 has 1 MΩ analog input impedance
regardless of sampling frequency. Single supply operation, on-chip filtering,
and high input impedance eliminate the need for driver op-amps and external
bipolar supplies.

The AD7606 anti-alias filter has a 3 dB cut-off frequency of 22 kHz and
provides 40 dB anti-alias rejection when sampling at 200 kSPS. The flexible
digital filter is pin-driven, yields improvements in SNR, and reduces the
3 dB bandwidth.

More Information
~~~~~~~~~~~~~~~~

- :adi:`AD7605 Product Info <AD7605>` — pricing, samples, datasheet
- :adi:`AD7605-4 Product Info <AD7605-4>` — pricing, samples, datasheet
- :adi:`AD7606 Product Info <AD7606>` — pricing, samples, datasheet
- :adi:`AD7606-6 Product Info <AD7606-6>` — pricing, samples, datasheet
- :adi:`AD7606-4 Product Info <AD7606-4>` — pricing, samples, datasheet
- `Nios II Embedded Development Suite (EDS)
  <https://community.altera.com/kb/knowledge-base/how-can-i-install-nios-ii-embedded-design-suite-legacy-tools/342234>`_

Getting Started
---------------

Hardware Items
~~~~~~~~~~~~~~

The following hardware items are required:

- Analog Devices :adi:`EVAL-CED Converter Evaluation and Development (CED)
  Board`
- `Terasic USB Blaster <http://www.terasic.com.tw/>`_
- One of the following evaluation boards:

  - :adi:`EVAL-AD7605EDZ evaluation board <EVAL-AD7605-4>`
  - :adi:`EVAL-AD7605-4EDZ evaluation board <EVAL-AD7605-4>`
  - :adi:`EVAL-AD7606EDZ evaluation board`
  - :adi:`EVAL-AD7606-6EDZ evaluation board`
  - :adi:`EVAL-AD7606-4EDZ evaluation board`

- Intel Pentium III or compatible Windows PC running at 866 MHz or faster,
  with a minimum of 512 MB of system memory

Software Tools
~~~~~~~~~~~~~~

The following software tools are required:

- `Quartus II Web Edition <https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html>`_
  design software v11.0
- `Nios II EDS <https://community.altera.com/kb/knowledge-base/how-can-i-install-nios-ii-embedded-design-suite-legacy-tools/342234>`_ v11.0

The Quartus II design software and the Nios II EDS are available via the
Altera Complete Design Suite DVD or by downloading from the web.

.. TODO: uncomment when ad7606_evalboard.zip is available
.. .. admonition:: Downloads
..    :class: download
..
..    - :download:`Evaluation Project Files <../images/ad7606_evalboard.zip>`

.. TODO: uncomment when ad7606_evalboard.zip is available
.. Extract the Lab Files
.. ~~~~~~~~~~~~~~~~~~~~~
..
.. Create a folder called ``ADIEvalBoard`` on your PC and extract the
.. ``ad7606_evalboard.zip`` archive to this folder. Make sure that there are
.. **NO SPACES** in the directory path. After extracting the archive, the
.. following folders should be present in the ``ADIEvalBoard`` folder:
..
.. .. list-table::
..    :header-rows: 1
..
..    * - Folder
..      - Description
..    * - FPGA
..      - Contains all files necessary to program the CED1Z board to evaluate
..        the ADC. Running the script ``program_fpga.bat`` will program the FPGA
..        with the evaluation project. New Nios II applications can be created
..        using files from this folder. The ``ip`` subfolder contains the HDL
..        core for connecting the evaluation board to the CED1Z board, software
..        drivers for HAL in ``hdl/src/HAL``, and AD7606 registers in
..        ``hdl/src/inc``
..    * - Hdl
..      - Contains source files for the AD7606 HDL driver:
..
..        - The ``doc`` subfolder contains brief documentation for the core
..        - The ``src`` subfolder contains the HDL source files
..        - The ``tb`` subfolder contains the core's testbench sources
..    * - NiosCpu
..      - Contains the CED1Z Quartus evaluation project source files. The ``ip``
..        subfolder contains the AD7606 QSYS component
..    * - Software
..      - Contains source files of the Nios II SBT evaluation project
..    * - DataCapture
..      - Contains script files used for data acquisition

Install the USB-Blaster Device Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Terasic USB-Blaster is used to program the CED1Z FPGA and connect to
the Nios II JTAG debug port. Follow these steps to install the Windows device
driver:

1. Plug the USB-Blaster into a free USB port on your PC. Windows will
   detect the new device.

   .. image:: ../images/usb_blaster_device_detected.png
      :align: center

2. Open Device Manager. The USB-Blaster will appear as an unrecognized
   device under "Other devices".

   .. image:: ../images/usb_blaster_device_manager.png
      :align: center

3. Right-click the device and select "Update Driver Software". Choose
   "Browse my computer for driver software".

   .. image:: ../images/usb_blaster_driver_browse.png
      :align: center

4. Browse to the Quartus II installation directory:
   ``altera\11.0\quartus\drivers\usb-blaster``

   .. image:: ../images/usb_blaster_driver_location.png
      :align: center

5. Click Next to proceed with the installation. Windows may warn about an
   unsigned driver — click "Install this driver software anyway".

   .. image:: ../images/usb_blaster_install_complete.png
      :align: center

6. The USB-Blaster driver is now installed successfully.

   .. image:: ../images/usb_blaster_install_success.jpg
      :align: center

AD7606 Evaluation Project Overview
-----------------------------------

.. TODO: uncomment when ad7606_evalboard.zip is available
.. The evaluation project contains all source files needed to build a system
.. that can configure the AD7606 and capture data from it. The system consists
.. of a Nios II softcore processor implemented in the FPGA on the CED1Z board
.. and a PC application. The softcore controls communication with the Device
.. Under Test (DUT) and the data capture process. Captured data is saved into
.. the SRAM of the CED1Z board and afterward is read by the PC application and
.. saved into a comma-separated values (.csv) file for further data analysis.

The following sections describe the CED1Z FPGA design and the AD7606
peripheral interface implemented in the evaluation project.

CED1Z FPGA Design
~~~~~~~~~~~~~~~~~

The following components are implemented in the FPGA design:

.. list-table::
   :header-rows: 1

   * - Name
     - Address
     - IRQ
   * - CPU
     - 0x00000800
     - \-
   * - PLL
     - 0x00000000
     - \-
   * - ONCHIP_MEM
     - 0x00002000
     - \-
   * - LEDS
     - 0x00000010
     - \-
   * - SYSID
     - 0x00000020
     - \-
   * - SRAM
     - 0x00200000
     - \-
   * - TRISTATE_BRIDGE_0
     - \-
     - \-
   * - JTAG_UART_0
     - 0x00000030
     - 1
   * - SYS_TIMER
     - 0x00000040
     - 2
   * - MM_CONSOLE_MASTER
     - \-
     - \-
   * - PWR_DATA
     - 0x00000060
     - \-
   * - I2C_INT
     - 0x00000080
     - \-
   * - PWR_EN_CLK
     - 0x000000a0
     - \-
   * - AD7606_0
     - 0x000000c0
     - \-

The Nios II processor contains a peripheral that implements the communication
protocol with the DUT. The peripheral is divided into three logical modules:
a module which implements the interface with the Avalon bus and communication
with the SRAM, a module which implements an Avalon master interface used to
write data directly to the SRAM, and a module which communicates with the
AD7606.

AD7606 Peripheral Port Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../images/ad7606_driver_pinout.png
   :align: center

.. list-table::
   :header-rows: 1

   * - Port
     - Direction
     - Width
     - Description
   * - **Generic pins**
     -
     -
     -
   * - CLK_I
     - IN
     - 1
     - System clock. Designed with a 98 MHz clock
   * - RESET_I
     - IN
     - 1
     - System reset
   * - **Avalon Slave Interface**
     -
     -
     -
   * - AVALON_WRITEDATA_I
     - IN
     - 32
     - Slave write data bus
   * - AVALON_WRITE_I
     - IN
     - 1
     - Slave write data request
   * - AVALON_READ_I
     - IN
     - 1
     - Slave read data request
   * - AVALON_ADDRESS_I
     - IN
     - 3
     - Slave address bus
   * - AVALON_READDATA_O
     - OUT
     - 32
     - Slave read data bus
   * - **Avalon Master Interface**
     -
     -
     -
   * - AVALON_MASTER_WAITREQUEST
     - IN
     - 1
     - Master wait request signal
   * - AVALON_MASTER_ADDRESS_O
     - OUT
     - 32
     - Master address bus
   * - AVALON_MASTER_WRITE_O
     - OUT
     - 1
     - Master write signal
   * - AVALON_MASTER_BYTEENABLE_O
     - OUT
     - 2
     - Master byte enable signals
   * - AVALON_MASTER_WRITEDATA_O
     - OUT
     - 16
     - Master write data bus
   * - **External connectors**
     -
     -
     -
   * - ADC_DB_I
     - IN
     - 16
     - ADC data bus used to read data from the AD7606
   * - ADC_BUSY_I
     - IN
     - 1
     - ADC Busy Output. Logic output that indicates conversion status. BUSY
       goes high after CONVST falling edge and stays high during conversion.
       Goes low when conversion is complete.
   * - ADC_OS_O
     - OUT
     - 3
     - Oversampling Mode Pins used to select the oversampling ratio
   * - ADC_RANGE_O
     - OUT
     - 1
     - Analog Input Range Selection. Logic high = ±10 V for all channels;
       logic low = ±5 V
   * - ADC_CS_N_O
     - OUT
     - 1
     - ADC Chip Select. Active low input used with RD to read conversion data
   * - ADC_RD_N_O
     - OUT
     - 1
     - ADC Read pin. Active low input used with CS to access conversion result
   * - ADC_RESET_O
     - OUT
     - 1
     - Reset pin. Rising edge on RESET resets the AD7606
   * - ADC_STDBY_O
     - OUT
     - 1
     - Standby Mode pin. Used to place AD7606 into power-down modes
   * - ADC_CONVST_N_O
     - OUT
     - 1
     - ADC Conversion Start Input. Falling edge on CONVST initiates
       conversion

AD7606 Peripheral Registers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Name
     - Offset
     - Width
     - Access
     - Description
   * - CONTROL_REGISTER
     - 0
     - 32
     - RW
     - Bit 0: Start data acquisition; Bit 1: Initiate software reset;
       Bit 2: Configure Avalon write master to write to same location;
       Bit 3: Write data to :adi:`EVAL-AD7606` evaluation board
   * - ACQ_COUNT_REGISTER
     - 1
     - 32
     - RW
     - Register to configure number of samples to acquire
   * - BASE_REGISTER
     - 2
     - 32
     - RW
     - Register to configure base memory address for acquired data
   * - STATUS
     - 3
     - 32
     - R
     - Bit 0: Acquisition complete; Bit 1: Internal memory buffer overflow;
       Bit 2: Write to read-only register
   * - DUT_WRITE_REGISTER
     - 4
     - 32
     - W
     - Register to configure driver submodule

Nios II Read Timing Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../images/ad7606_read_timing.png
   :align: center

AD7606 Module
^^^^^^^^^^^^^

This module is the actual driver of the AD7606 data acquisition system.

.. list-table::
   :header-rows: 1

   * - Port
     - Direction
     - Width
     - Description
   * - **General Connectors**
     -
     -
     -
   * - FPGA_CLK_I
     - IN
     - 1
     - 48 MHz clock
   * - ADC_CLK_I
     - IN
     - 1
     - 20 MHz clock
   * - RESET_I
     - IN
     - 1
     - Module reset
   * - **CED1Z Interface connectors**
     -
     -
     -
   * - WR_DATA_N_I
     - IN
     - 1
     - Signal to write data in driver's internal registers
   * - DATA_I
     - IN
     - 16
     - Data bus to configure driver
   * - DATA_O
     - OUT
     - 16
     - Parallel bus to transfer data to upper module
   * - DATA_RD_READY_O
     - OUT
     - 1
     - Signals new data available at DATA_O port
   * - DATA_WR_READY_O
     - OUT
     - 1
     - Signals write from upper module has been performed
   * - SYNC_O
     - OUT
     - 1
     - Signals next data transfer corresponds to channel 1
   * - **AD7606 connectors**
     -
     -
     -
   * - ADC_DB_I
     - IN
     - 16
     - ADC data bus to read data from AD7606
   * - ADC_BUSY_I
     - IN
     - 1
     - ADC Busy Output indicating conversion status
   * - ADC_OS_O
     - OUT
     - 3
     - Oversampling Mode Pins to select oversampling ratio
   * - ADC_RANGE_O
     - OUT
     - 1
     - Analog Input Range Selection (high = ±10 V, low = ±5 V)
   * - ADC_CS_N_O
     - OUT
     - 1
     - ADC Chip Select (active low)
   * - ADC_RD_N_O
     - OUT
     - 1
     - ADC Read pin (active low)
   * - ADC_RESET_O
     - OUT
     - 1
     - Reset pin (active high)
   * - ADC_STDBY_O
     - OUT
     - 1
     - Standby Mode pin
   * - ADC_CONVST_N_O
     - OUT
     - 1
     - ADC Conversion Start Input (active low)

.. TODO: uncomment when ad7606_evalboard.zip is available
.. Quick Evaluation
.. ----------------
..
.. The next sections present all steps needed to create a fully functional
.. project for evaluating the ADI platform. It is possible to skip these steps
.. and load into the FPGA an image that contains a fully functional system.
..
.. The first step of the quick evaluation process is to program the FPGA with
.. the image provided in the lab files. Before the image can be loaded, the
.. Quartus II Web Edition tool or the Quartus II Programmer must be installed on
.. your computer.
..
.. To load the FPGA image:
..
.. 1. Make sure the USB cable is **not** connected to the CED1Z board
.. 2. Connect the USB Blaster to the J6 connector of the CED1Z
.. 3. Power the board
.. 4. Run the ``program_fpga.bat`` batch file located in the
..    ``ADIEvalBoard/FPGA`` folder
..
.. After programming the FPGA, follow the instructions in the
.. `Evaluation Project Data Acquisition`_ section to acquire data.

.. TODO: uncomment when ad7606_evalboard.zip is available
.. Nios II Software Design
.. -----------------------
..
.. This section describes how to create, build, and run the Nios II software
.. project using the Eclipse-based Software Build Tools (SBT).
..
.. 1. From **Start → All Programs → Altera → Nios II EDS 11.0**, open
..    **Nios II 11.0 Software Build Tools for Eclipse**.
..
..    .. note::
..
..      On Windows 7, right-click the shortcut and select **Run as administrator**.
..
.. 2. Create a new folder named ``eclipse_workspace`` inside the
..    ``ADIEvalBoard`` directory. When Eclipse prompts for a workspace, browse
..    to this folder and click **OK**.
..
..    .. image:: ../images/eclipseworkspace.png
..       :align: center
..
.. 3. Select **File → New → Nios II Application and BSP from Template**.
..
..    .. image:: ../images/eclipse_new_nios_project.png
..       :align: center
..
.. 4. Browse to the ``uC.sopcinfo`` file located in the ``ADIEvalBoard/FPGA``
..    directory. Set the application project name to ``ADIEvalBoard`` and
..    select the **Blank Project** template. Click **Finish**.
..
..    .. image:: ../images/eclipseblankproject.png
..       :align: center
..
..    Eclipse creates two project directories: the application project
..    (``ADIEvalBoard``) and the Board Support Package project
..    (``ADIEvalBoard_bsp``).
..
..    .. image:: ../images/eclipseprojects.png
..       :align: center
..
.. 5. In the Project Explorer, right-click **ADIEvalBoard_bsp** and select
..    **Nios II → BSP Editor**.
..
..    .. image:: ../images/eclipsebspmenu.png
..       :align: center
..
.. 6. In the BSP Editor, under the **Common Settings** tab, configure the
..    following:
..
..    - Set **stdin**, **stdout**, and **stderr** to ``jtag_uart_0``
..    - Set **sys_clk_timer** to ``none``
..    - Set **timestamp_timer** to ``none``
..
..    .. image:: ../images/cedzmainsettings.png
..       :align: center
..
.. 7. Switch to the **Linker Script** tab and change the ``.text`` region from
..    ``onchip_mem`` to ``sram``.
..
..    .. image:: ../images/ced1zlinkersettings.png
..       :align: center
..
.. 8. Click **Generate** to apply the BSP settings, then close the BSP Editor.
..
.. 9. Right-click **ADIEvalBoard_bsp → Properties → Nios II BSP Properties**
..    and configure:
..
..    - **Optimization level:** Level 2
..    - Uncheck **Support C++**
..    - Check **Reduced device drivers**
..    - Check **Small C library**
..
..    .. image:: ../images/eclipsebspproperties.png
..       :align: center
..
.. 10. Open Windows Explorer and navigate to the ``Software`` folder inside
..     ``ADIEvalBoard``. Select all files and directories, then drag and drop
..     them into the **ADIEvalBoard** project in the Eclipse Project Explorer.
..     When prompted, select **Copy files and folders**.
..
..    .. image:: ../images/eclipsecopy.png
..       :align: center
..
.. 11. Right-click the **ADIEvalBoard** project → **Properties → Nios II
..     Application Properties**. Change **Optimization level** to **Level 2**
..     and click **Apply** then **OK**.
..
..    .. image:: ../images/eclipseprojproperties.png
..       :align: center
..
.. 12. Open ``my_include_paths.in`` from the project, select all (Ctrl+A) and
..     copy (Ctrl+C).
..
..    .. image:: ../images/eclipseinclude.png
..       :align: center
..
.. 13. Open the ``Makefile`` in the project and locate the line
..     ``APP_INCLUDE_DIRS :=``. Paste the copied content (Ctrl+V) and save the
..     file (Ctrl+S).
..
..    .. image:: ../images/eclipsemakefileinclude.png
..       :align: center
..
.. 14. Right-click **ADIEvalBoard_bsp** and select **Build Project**.
..
..    .. image:: ../images/eclipsebuildbsp.png
..       :align: center
..
.. 15. Right-click **ADIEvalBoard** and select **Build Project**. This creates
..     the ``ADIEvalBoard.elf`` executable file.
..
..    .. image:: ../images/eclipsebuildproj.png
..       :align: center
..
..    .. tip::
..
..       If you see the error "section .rodata ... overlaps section .text", open
..       the BSP Editor → **Main → Settings → Advanced → hal.linker** and uncheck
..       **enable_alt_load_copy_exceptions**, then rebuild the BSP.
..
.. 16. With the **ADIEvalBoard** project selected, go to **Run → Run
..     Configurations**. Select **Nios II Hardware** and press **New**.
..
..    .. image:: ../images/eclipserunconfig.png
..       :align: center
..
.. 17. Change the configuration name to ``CED1Z``. On the **Target Connection**
..     tab, press **Refresh Connections**.
..
..    .. image:: ../images/eclipse_run_target_connection.png
..       :align: center
..
.. 18. Select ``jtag_uart_0`` as the **Byte Stream Device for stdio**. Check
..     **Ignore mismatched system ID** and **Ignore mismatched system
..     timestamp**.
..
..    .. image:: ../images/ignoreid.png
..       :align: center
..
.. 19. Program the FPGA by running ``ADIEvalBoard/FPGA/program_fpga.bat``.
..
.. 20. Press **Run** in the Run Configurations window. The software downloads
..     and executes on the CED1Z hardware.
..
..    .. image:: ../images/eclipsestartprogram.png
..       :align: center

.. TODO: uncomment when ad7606_evalboard.zip is available
.. Evaluation Project Data Acquisition
.. -------------------------------------
..
.. After the FPGA is correctly programmed, data acquisition can start by
.. executing the ``data_capture.bat`` script. The ``data_capture.tcl`` file
.. can be modified to:
..
.. - Acquire a variable number of channels
.. - Change the oversampling signals
.. - Change the range signal
..
.. .. note::
..
..    If the number of channels specified is larger than available on the part,
..    the additional channels will be taken from channel 1. For example, with
..    AD7606-4, channel 5 will have the same data as channel 1, channel 6 will
..    have the same data as channel 2, and so on.
..
.. .. note::
..
..    The configuration from ``data_capture.tcl`` is applied the first time the
..    script is executed. If changes are made afterward, the system must be
..    reinitialized by reprogramming the FPGA.
..
.. The resulting CSV file can be opened with Microsoft Excel. Data will be
.. displayed in columns, with each column corresponding to a channel.

More Information
----------------

- :ez:`Ask questions about the FPGA reference design <community/fpga>`
