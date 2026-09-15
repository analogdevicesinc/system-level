.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-acevsecrdset-sl/software

.. _ad-acevsecrdset-sl software:

AD-ACEVSECRDSET-SL Software User Guide
======================================

The :adi:`AD-ACEVSECRDSET-SL` is an electric vehicle (EV) type 2 charging system
based on ADI"s microcontroller and energy metering technology. This solution is
designed for a Type 2 EVSE 3.6 kW EV charging cable, enabling easy integration
with standard EV systems. The :adi:`AD-ACEVSECRDSET-SL` is designed to meet
IEC61851 and IEC62752 standards and includes a Type A residual current device
(RCD) and a control pilot circuit.

--------------

The no-OS framework and the drivers for the main components
-----------------------------------------------------------

no-OS general description
~~~~~~~~~~~~~~~~~~~~~~~~~

:dokuwiki:`no-OS </resources/no-os>` is a software framework by
:adi:`Analog Devices Inc <en/index.html>` for systems that don"t include an
operating system (OS), otherwise known as baremetal. This framework defines a
:dokuwiki:`common interface (API) </resources/no-os/api>` for accessing typical
baremetal peripherals such as GPIO, SPI, I2C, RTC, Timer, Interrupt Controller,
and other. This common API may be then used to initialize and control these
peripherals in a common way across multiple microcontroller platforms. The
framework currently supports Intel and Xilinx microprocessors and SoC"s as well
as :adi:`Analog Devices <en/index.html>`" own precision microcontrollers,
several Maxim Integrated MAX32xxx microcontrollers, STMicroelectronics" STM32,
Raspberry Pi"s Pico, and mbedOS-based devices. By using this common driver API,
following its own :git-no-OS:`coding style <wiki/Code-Style-guidelines+>`, the
:dokuwiki:`no-OS </resources/no-os>` is able to provide reference projects for
Analog Devices Inc evaluation boards running on various underlying hardware.
Thanks to the :dokuwiki:`no-OS build system </resources/no-os/build>`, no-OS
users may generate standalone reference projects in a short period of time and
use them as the starting point for their own development. no-OS is an
open-source software, and its official repository is the
:git-no-OS:`no-OS Github Repository </>`. Users are free to use and distribute
no-OS, provided that they comply with the :git-no-OS:`license <LICENSE+>`. The
no-OS main drivers used in the firmware are the ones concerned with the
:adi:`MAX32655` microcontroller, the :adi:`ADE7913` isolated, 3-channel Σ-Δ ADC,
and the :adi:`ADT75` temperature monitoring system.

no-OS support for Maxim microcontrollers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The no-os framework supports several Maxim microcontrollers, including the
:adi:`MAX32655`, and implements the low-level functions for controlling the
hardware components of the device: GPIO, UART, NVIC, I2C, and SPI. The
:dokuwiki:`build </resources/no-OS/build>` guide provides the steps required for
creating and building an application based on a supported Maxim microcontroller
part.

ADE7913 no-OS driver
~~~~~~~~~~~~~~~~~~~~

The existing no-OS driver for the :adi:`ADE7913` ADC implements the
functionalities provided by the device through a comprehensive high-level API.
All the settings of the :adi:`ADE7913` ADC are accessed through separate
functions that perform SPI read and write operations on the corresponding device
registers. The driver provides the possibility of reading the acquired data at
moments in time specified by the application or depending on the state of the
Data Ready pin through an interrupt. Using the device requires populating the
initialization parameters structure, calling the ade7913_int API and then
reading the i_wav, v1_wav, and v2_wav members of the device structure. Depending
on the desired settings, these members are updated through an interrupt
triggered by the Data Ready pin or each time a long SPI read operation is
performed on one of the device"s registers.

.. code:: c

   // ADE7913 initialization structure
   struct ade7913_init_param ade7913_ip = { 0 };

   // ADE7913 dev SPI init params
   ade7913_ip.spi_init = &ade7913_spi_ip;
   // ADE7913 dev DATA_RDY init params
   ade7913_ip.gpio_rdy = &ade7913_gpio_rdy_ip;
   // ADE7913 dev RESET init params
   ade7913_ip.gpio_reset = &ade7913_gpio_reset_ip;
   // IRQ deviuce descriptor used to handle interrupt routine for GPIO RDY
   ade7913_ip.irq_ctrl = ade7913_irq_desc;

   // ADE7913 device initialization
   ret = ade7913_init(device, ade7913_ip);

   // Data updated automatically in the  i_wav, v1_wav, and v2_wav members of the device structure

ADT75 no-OS driver
~~~~~~~~~~~~~~~~~~

no-OS support for the :adi:`ADT75` provides an easy and straight-forward way of
obtaining temperature readings from the device. Using the device implies the
specification of the SPI communication parameters, the call of the adt75_init
function for initialization, and the adt75_get_single_temp API for getting the
current temperature value.

.. code:: c

   //ADT75 initialization structure
   struct adt75_init_param adt75_ip = {
       .comm_param = i2c_param,
   };

   // ADT75 device initialization
   ret = adt75_init(&adt75_desc, &adt75_ip);

   // ADT75 single temperature reading
   ret = adt75_get_single_temp(adt75_desc, &val);

Resources
---------

.. admonition:: Download

   - :git-no-OS:`Github resources <tree/master/projects/ad-acevsecrdset-sl+>`

   It is recommended to update the firmware to the latest firmware release.

Flashing and debugging the firmware for the AD-ACEVSECRDSET-SL using the max32625pico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What is needed:
^^^^^^^^^^^^^^^

max32625pico AD-ACEVSECRDSET-SL.hex AD-ACEVSECRDSET-SL board usb to micro usb
cable 10 pin Cortex Debug Cable 3 wire cable with mains plug attached Serial
terminal

Obs: The binary can be obtained following the steps presented at
:dokuwiki:`no-OS build guide </resources/no-os/build>`

STEP 1 max32625pico firmware update
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the MAX32655FTHR Firmware image from
`here <https://github.com/MaximIntegrated/max32625pico-firmware-images/>`__
Follow the procedure indicated at
`here <https://github.com/MaximIntegrated/max32625pico-firmware-images/#how-to-update-the-firmware>`__
to load the new firmware.

STEP 2 Connect the max32625pico to the board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect the Cortex Debug Cable to the :adi:`max32625pico` with the connector key
directed towards the outside of the board and to the :adi:`AD-ACEVSECRDSET-SL`
board directed downwards.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/ad-acevsecrdset-sl_soft1.jpg
   :width: 400px

Step 3 Connect the board to mains
'''''''''''''''''''''''''''''''''

Connect the NULL, PHASE and Earth as indicated on the enclosure. Power up the
board from 230V AC through the just attached cable.

Step 4 Flashing the firmware to the board
'''''''''''''''''''''''''''''''''''''''''

If the :adi:`max32625pico` is not connected to the PC USB port connect it. The
DAPLINK should appear as a storage device on the PC. Open the DAPLINK. Two files
should already be present as seen in the following image.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/ad-acevsecrdset-sl_soft2.jpg
   :width: 400px

Drag and drop the AD-ACEVSECRDSET-SL.hex into DAPLINK. The firmware will be
written on the target MCU.

Step 5 Verify that the firmware was written correctly.
''''''''''''''''''''''''''''''''''''''''''''''''''''''

Open the device manager and go to Ports. Find the COM port allocated to the
:adi:`max32625pico`. Use a serial terminal (e.g. PuTTY) to verify that the
firmware was correctly updated. If using PuTTY under the Terminal menu select
the :adi:``Implicit CR in every LF``. From the Window menu modify the ``Lines of
scrollback`` to a higher value (200000) than the default one. Open PuTTY and
under the ``Session`` menu insert the following data: The COM port indicated in
the device manager for the device and the baud rate of 57600. Hit the Open
button and after the terminal window opens reset the
`AD-ACEVSECRDSET-SL <AD-ACEVSECRDSET-SL>` board from the reset button. The
following messages should be displayed in the serial terminal window:

Revision A
~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/04_ad_bct2ade9113.png
   :width: 400px

Revision D
~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-acevsecrdset-sl/rev_d_debug_1.png
   :width: 400px

After the self-test passes the status LED 1 will be on.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bct2ade9113-sl/ad-acevsecrdset-sl_soft3.jpg
   :width: 200px

--------------

.. tip::

   **If you want to go back to the HARDWARE SETUP, click here:**
   :dokuwiki:`AD-ACEVSECRDSET-SL Hardware User Guide </resources/eval/user-guides/ad-acevsecrdset-sl/hardware>`
