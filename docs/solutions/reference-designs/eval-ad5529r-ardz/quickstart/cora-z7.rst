.. _eval-ad5529r-ardz quickstart cora-z7:

Cora Z7-07S Quickstart
======================

This guide walks through setting up the :adi:`EVAL-AD5529R-ARDZ` with the
Cora Z7-07S carrier board running ADI Kuiper Linux.

Necessary Files
---------------

**Option A: Kuiper Linux SD Card Image (Recommended)**

Download the ADI Kuiper Linux image:

- :external+kuiper:doc:`ADI Kuiper Linux Downloads <index>`

.. TODO:: Add direct link to Kuiper image with AD5529R support

**Option B: Individual Boot Files**

If building from source, you need:

.. list-table:: Required Boot Files
   :header-rows: 1
   :widths: 30 70

   * - File
     - Description
   * - ``BOOT.BIN``
     - First Stage Boot Loader (FSBL) + FPGA bitstream
   * - ``uImage``
     - Linux kernel image
   * - ``devicetree.dtb``
     - Device tree blob for AD5529R + Cora Z7

.. TODO:: Add links to pre-built boot files

Required Hardware
-----------------

- :adi:`EVAL-AD5529R-ARDZ` evaluation board
- `Cora Z7-07S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`_ carrier board
- MicroSD card (8 GB+, Class 10)
- Micro-USB cable for UART console
- 5V/2A power supply (optional, for standalone operation)
- Host PC with terminal software (PuTTY, minicom, etc.)

Creating the Setup
------------------

.. TODO:: Add hardware setup photo (cora-z7-setup.png)

.. code-block:: rst

   .. figure:: ../images/cora-z7-setup.png
      :align: center
      :width: 600

      Hardware Setup: EVAL-AD5529R-ARDZ on Cora Z7-07S

**Step 1: Prepare the SD Card**

For Kuiper Linux image:

1. Download the Kuiper Linux image
2. Write the image to the SD card using Balena Etcher or ``dd``
3. Copy the AD5529R-specific boot files to the boot partition (if required)

For individual boot files:

1. Format the SD card with a FAT32 partition
2. Copy ``BOOT.BIN``, ``uImage``, and ``devicetree.dtb`` to the partition

**Step 2: Connect the Hardware**

1. Ensure power is OFF
2. Align the EVAL-AD5529R-ARDZ with the Cora Z7 Arduino headers
3. Press firmly to seat the board on all header pins
4. Connect the Micro-USB cable to the Cora Z7 USB port (J6)

**Step 3: Configure the Terminal**

Open a serial terminal with these settings:

.. code-block:: text

   Port: /dev/ttyUSB0 (Linux) or COMx (Windows)
   Baud rate: 115200
   Data bits: 8
   Stop bits: 1
   Parity: None
   Flow control: None

**Step 4: Power On and Boot**

1. Insert the SD card into the Cora Z7
2. Connect power (USB or external 5V)
3. Observe the boot messages in the terminal

Boot Messages
-------------

Expected console output during boot:

.. code-block:: console

   U-Boot 2022.01-xilinx-v2022.1 (Jan 01 2023)

   Model: Digilent Cora Z7
   DRAM:  512 MiB
   ...
   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.15.0-xilinx (...)
   ...
   [    1.234567] ad5529r spi0.0: AD5529R DAC initialized
   [    1.234890] iio iio:device0: ad5529r

   analog login:

.. TODO:: Update with actual boot log from hardware

Default login credentials:

- **Username:** ``analog`` or ``root``
- **Password:** ``analog``

Verifying the Device
--------------------

**Using iio_info**

List available IIO devices:

.. code-block:: console

   root@analog:~# iio_info
   Library version: 0.24
   ...
   IIO context has 1 devices:
       iio:device0: ad5529r
           16 channels found:
               voltage0: (output)
               voltage1: (output)
               ...
               voltage15: (output)

.. TODO:: Verify actual iio_info output

**Using iio_attr**

Read and write DAC channel values:

.. code-block:: console

   # Read current value of channel 0
   root@analog:~# iio_attr -c ad5529r voltage0 raw
   32768

   # Set channel 0 to mid-scale (32768 = 50% of full scale)
   root@analog:~# iio_attr -c ad5529r voltage0 raw 32768

   # Set channel 0 to full scale
   root@analog:~# iio_attr -c ad5529r voltage0 raw 65535

IIO Oscilloscope Usage
----------------------

**Connecting to the Device**

1. Launch IIO Oscilloscope on your host PC
2. Click **Connect** and select the connection method:

   - **IP**: Enter the board's IP address (e.g., ``192.168.1.100``)
   - **USB**: Select the USB backend if using USB OTG

.. TODO:: Add IIO Oscilloscope connect screenshot (iio-connect.png)

.. code-block:: rst

   .. figure:: ../images/iio-connect.png
      :align: center
      :width: 500

      IIO Oscilloscope Connection Dialog

**Debug Panel**

The Debug panel shows device and channel attributes:

.. TODO:: Add IIO Oscilloscope debug panel screenshot (iio-debug.png)

.. code-block:: rst

   .. figure:: ../images/iio-debug.png
      :align: center
      :width: 600

      IIO Oscilloscope Debug Panel for AD5529R

- View/modify channel raw values
- Read device status registers
- Configure operational parameters

**DMM Panel**

The DMM (Digital Multimeter) panel provides real-time DAC control:

.. TODO:: Add IIO Oscilloscope DMM panel screenshot (iio-dmm.png)

.. code-block:: rst

   .. figure:: ../images/iio-dmm.png
      :align: center
      :width: 500

      IIO Oscilloscope DMM Panel for DAC Control

- Slider control for each DAC channel
- Numeric input for precise values
- Real-time output voltage display

PyADI-IIO Example
-----------------

Control the DAC from Python:

.. code-block:: python

   import adi

   # Connect to the DAC
   dac = adi.ad5529r(uri="ip:192.168.1.100")

   # Set channel 0 to mid-scale
   dac.channel[0].raw = 32768

   # Set all channels to different values
   for i in range(16):
       dac.channel[i].raw = i * 4096  # Staircase pattern

   # Read back channel values
   for i in range(16):
       print(f"Channel {i}: {dac.channel[i].raw}")

.. TODO:: Verify PyADI-IIO API matches actual implementation

**Sample Output:**

.. code-block:: console

   $ python3 dac_example.py
   Channel 0: 0
   Channel 1: 4096
   Channel 2: 8192
   ...
   Channel 15: 61440

Useful Commands
---------------

.. code-block:: console

   # Check network configuration
   root@analog:~# ifconfig

   # List IIO devices
   root@analog:~# iio_info

   # Read device attributes
   root@analog:~# iio_attr -d ad5529r

   # Shutdown the system
   root@analog:~# poweroff

Troubleshooting
---------------

**Device not detected**

1. Verify the SD card contains correct boot files
2. Check that the EVAL board is firmly seated on the Arduino headers
3. Verify the boot messages show successful driver loading

**IIO Oscilloscope cannot connect**

1. Ensure the board has network connectivity (check ``ifconfig``)
2. Verify firewall settings allow IIO connections (port 30431)
3. Try USB backend if IP connection fails

**DAC outputs incorrect voltage**

1. Verify power supply connections
2. Check jumper settings (VREF source, VDD_IO level)
3. Confirm the correct output range is selected

Next Steps
----------

- :ref:`eval-ad5529r-ardz user-guide` - Detailed hardware configuration
- :external+hdl:ref:`HDL Project Documentation <ad5529r_ardz>` - FPGA design details
- :git-pyadi-iio:`PyADI-IIO Examples </>` - More Python examples
