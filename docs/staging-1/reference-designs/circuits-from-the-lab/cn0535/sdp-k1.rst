.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0535/sdp-k1

.. _circuits-from-the-lab cn0535 sdp-k1:

CN0535 and the SDP-K1
=====================

General Setup
-------------

The following sections on setup describe the steps for setting up the CN0535
board using the :adi:`SDP-K1` and the
`mbed Example program for CN0535-FMCZ <https://os.mbed.com/teams/AnalogDevices/code/EVAL-CN0535-FMCZ>`__.

Equipment
---------

- :adi:`SDP-K1` micro-controller board
- :adi:`EVAL-CN0535-FMCZ Evaluation Board <cn0535>`
- PC with a USB port and Windows 7 (32-bit) or higher
- Serial Terminal Software (Putty/TeraTerm or similar)
- USB Standard-A to Mini-B cable
- 6V wall wart power supply
- :adi:`SDP-K1 User Guide <media/en/technical-documentation/user-guides/EVAL-SDP-CK1Z-UG-1539.pdf>`

Hardware Setup
--------------

The following sections describe the process of setting up the hardware for both
the :adi:`SDP-K1` micro-controller board and the
:adi:`EVAL-CN0535-FMCZ <en/design-center/reference-designs/circuits-from-the-lab/cn0535.html#rd-overview>`
customer evaluation board.

EVAL-CN0535-FMCZ Prep for use with SDP-K1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-CN0535-FMCZ was designed
`to be evaluated <https://www.analog.com/en/design-center/reference-designs/circuits-from-the-lab/cn0535.html#rd-commonvariations>`__
using :adi:`SDP-H1`. On the other hand, if the user want to evaluate the CN0535
using :adi:`SDP-K1`, the following components needs to be installed. The table
below shows the components that the user must install to enable the use of the
EVAL-CN0535-FMCZ with the SDP-K1.

.. list-table::
   :header-rows: 1

   * -
     - Component
     - Manufacturing Part Number
   * -
     - 1. P2, P4
     - TSM-108-04-T-SV
   * -
     - 2. P3
     - TSM-110-04-T-SV
   * -
     - 3. R38, R5, R6, R7, R27
     - ERJ-3GEY0R00V or equivalent 0 ohm jumper
   * -
     - 4. C25
     - 0603YC104KAT2A or equivalent
   * -
     - 5. Y1
     - SIT8008BI-21-33E-16.38400G

Shown on below Figures the board setup for SDP-K1.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/board_top.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/board_bot.png

SDP-K1
~~~~~~

      Shown below is the **CN0535 board** mounted on the **SDP-K1 board** via
      the Arduino headers. The SDP-K1 only requires a single Standard-A to
      type-C USB cable to connect to the PC. Both the orange Connected LED and
      green SYS PWR should light on the SDP-K1 if connected correctly.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/setup_block_diagram2.png

Note: For SDP-K1 Rev E and Below, a 6V wall-wart power is needed on P15.

Software Setup
--------------

Importing the EVAL-CN0535-FMCZ MBED Example program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. If the user doesn"t have an mbed online id account, the user must create one
   at https://ide.mbed.com/.
#. After having a acount, open the Example program for EVAL-CN0535-FMCZ
   https://os.mbed.com/teams/AnalogDevices/code/EVAL-CN0535-FMCZ/

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/mbed_link.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/mbed_link_2.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/mbed_link_3.png

Connecting to a serial terminal application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to communicate with the board using the SDP-K1 the user needs to
install a serial terminal software on their PC. It is recommended to use PuTTY
which is available for free download on the internet. The following steps were
written with PuTTY in mind however any other serial terminal application should
follow a similar procedure. Following are the steps required to interface with
the board.

#. Open Device Manager through the Windows control panel and plug the
   micro-controller board into the PC, when the board is detected it will appear
   in device manager, displaying as USB Serial Device. This also displays which
   port the board is connected to. (COM4 in this case)

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/device_manager.png
      :width: 450px

#. Open the serial terminal application and enter the correct values to
   configure it to connect to the board. The serial line should be the COM port
   noted earlier and the speed should be set to 115200 to ensure data transfer
   works correctly. Also note the changes in the Terminal tab, this is required
   for the menu to display properly.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/putty1.png

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/putty2.png

#. Upon connection, the interface menu should appear. If not, press the reset
   button on the micro-controller board, this will call up the command menu for
   the user to interact with. **(Note: This does not work with the version A & B
   of the SDP-K1)**

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/putty_terminal.png

#. From here, the user should type the number corresponding to their desired
   choice and press "Enter". Note that many choices will create sub-menus,
   prompting the user to make another choice.

Command Summary
~~~~~~~~~~~~~~~

The following table shows every command along with a brief description. Some
commands have recommended settings to apply for optimal results for narrow
bandwidth measurements of 32 kHz.

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - 1. Set LTC6373 PGIA Gain/Mode
     - Change the :adi:`LTC6373` Gain or Mode. The available option are Shutdown
       mode and gains of 0.25 V/V, 0.5 V/V, 1 V/V, 2 V/V, 4 V/V, 8 V/V, 1 6V/V.
   * - 2. Set ADA4945 FDA Power Mode
     - Change the :adi:`ADA4945` Power Mode to: Full Power Mode or Low Power Mode.
   * - 3. Set AD7768-1 power mode
     - Change the :adi:`AD7768-1` to Low, Median or Fast. Low power mode is
       recommended.
   * - 4. Set AD7768-1 MCLK clock divider
     - Change the :adi:`AD7768-1` clock divider to: /16, /8, /4 or /2. /16 is
       recommended.
   * - 5. Set AD7768-1 filter type
     - Change the :adi:`AD7768-1` filter type used. Also allows for the
       oversampling ratio to be changed. Recommended is the Low ripple FIR
       Filter, oversampled by 32.
   * - 6. Set AD7768-1 AIN buffers
     - Adjust the :adi:`AD7768-1` buffers for both AIN+ and AIN-. It is
       recommended to turn on both AIN+ and AIN + precharge buffers.
   * - 7. Set AD7768-1 REF buffers
     - Adjust the :adi:`AD7768-1` buffers for both REF+ and REF-. It is
       recommended to turn on both REF+ and REF- precharge REF buffers.
   * - 8. Set AD7768-1 VCM output
     - Choose the :adi:`AD7768-1` VCM output voltage, recommended is (AVDD1 –
       AVSS)/2.
   * - 9. Set AD7768-1 data output mode
     - Set the :adi:`AD7768-1` data output mode.
   * - 10. Set AD7768-1 diagnostic mode
     - Change which diagnostic mode is used for the ADC.
   * - 11. Set AD7768-1 Gains and Offsets
     - Set :adi:`AD7768-1` Gain and Offset register.
   * - 12. Read AD7768-1 master status
     - Shows faults in :adi:`AD7768-1` master status register, allowing the user
       to pinpoint the source of problems.
   * - 13. Read AD7768-1 desired register
     - Reads desire :adi:`AD7768-1` register.
   * - 14. Read AD7768-1 data register
     - Reads :adi:`AD7768-1` data register.
   * - 15. Read AD7768-1 continuous mode data
     - Reads Raw data from the ADC over a user-defined number of samples.
   * - 16. Print AD7768-1 Continuous mode measured data
     - Prints previously read raw data to and converted into voltages, codes and
       read raw data the terminal. Logging the terminal will allow the user to
       use extract this data. Requires the "Read data" command to have been run.
   * - 17. AD7768-1 Scratchpad Check
     - Input an 8-bit number, if it is returned the ADC is interfacing with the
       software. This is a useful quick check for debugging and is good to run
       after setup.
   * - 18. Reset AD7768-1 ADC
     - Resets the ADC, either a soft reset over SPI or hard reset using the
       reset pin.
   * - 19. Set to Board Default Config
     - Set the board to default configurations.
   * - 20. Update Vref and MCLK values
     - Update the Vref and MCLK values.

*End of Document*
