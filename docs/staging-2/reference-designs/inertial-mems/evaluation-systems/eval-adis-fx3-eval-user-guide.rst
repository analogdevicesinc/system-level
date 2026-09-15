.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis-fx3-eval-user-guide

.. _inertial-mems evaluation-systems eval-adis-fx3-eval-user-guide:

iSensor Eval GUI User Guide
===========================

.. warning::

   This guide assumes that you"ve connected your IMU to the :adi:`EVAL-ADIS-FX3`
   and that the Eval GUI software was able to verify communication with your IMU
   successfully. We recommend checking out the
   :dokuwiki:`Setup and Troubleshooting </resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis-fx3-setup-troubleshooting>`
   guide before continuing with the Eval GUI user guide.

Eval GUI Main Window
--------------------

The Eval GUI Main Window brings together many functions, utilities, and
subroutines useful when working with the :adi:`EVAL-ADIS-FX3` and ADI inertial
sensors. The image below summarizes the buttons, menus, and tabs available on
the main window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/main_screen_sections.jpg

#. **Reboot FX3** - This button commands the :adi:`EVAL-ADIS-FX3` to reboot,
   forcing USB re-enumeration and powering off the sensor supply (if powered
   through USB).
#. **FX3 Board Info** - This button displays information describing the
   :adi:`EVAL-ADIS-FX3` hardware and firmware and the active FX3Api version,
   build date and commit information.
#. **Select DUT Type** - This button calls the DUT Type Selection window,
   allowing you to quickly change the active device type configuration. Click
   :dokuwiki:`here </resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis-fx3-setup-troubleshooting#connecting_to_the_fx3_board>`
   for more information.
#. **Manual DUT Config** - This button calls the Manual DUT Configuration
   window. This window allows you to customize the communication protocol
   settings, sensor supply, active register map, GUI color scheme, and many
   other features. Click here for a detailed guide on using this window.
#. **Reset DUT** - This button will force the RESET pin to pulse for ~10ms,
   causing the sensor to reboot.
#. **Check DUT Connection** - This button will execute a series of SPI
   transactions that attempt to validate the sensor"s SPI configuration settings
   and connections.
#. **FX3/DUT Status** - This section displays the FX3 status, sensor status,
   sensor supply status, and the active device type.
#. **Evaluation GUI Functions** - These tabs group the :adi:`EVAL-ADIS-FX3`\ "s
   capabilities into different sections. Many of these capabilities are
   described in detail below.
#. **Evaluation GUI Main Window** - This section of the GUI will update as
   different tabs are selected.
#. **Evaluation GUI Metadata** - This section displays the Evaluation GUI
   version and active register map.
#. **Evaluation GUI Update and Issue Reporting** - Clicking on ``Check for
   Updates`` will query the official GitHub repository to look for a newer
   version of the Eval GUI. Clicking on ``Report Issue`` will navigate to the
   GitHub issue tracking page.

Reading and Writing to IMU Registers
------------------------------------

The FX3 Evaluation GUI provides several ways to read and write the IMU"s onboard
registers. The ``Register Access`` tab offers a quick way to modify IMU
registers, allowing for manual configuration of the IMU without the need to
develop any extra software. Hex-to-decimal conversion can be toggled by checking
the ``Scale Data`` checkbox in the screen"s upper-right corner. The ``Continuous
Read`` checkbox will toggle an automatic, periodic read of all the registers
listed on the current page.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/scale_data.png

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/continuous_read_dec_hex.gif`

Individual registers can be read by clicking on the corresponding register"s
cell in the table. The entire page may also be read by clicking the ``Read
Page`` button in the screen"s upper-right corner.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/read_registers.png

.. important::

   The Eval GUI will automatically append an extra 16-bit SPI transaction
   (reading 32 bits from the sensor in total) when reading any \*_LOW registers
   (this includes gyroscope, accelerometer, delta angle/velocity, and offset
   registers where applicable). The Eval GUI performs the 16-bit SPI
   transactions, transmits the data to the PC, and combines the two 16-bit
   numbers into a single 32-bit number. A single SPI transaction will look like
   the capture shown below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/spi_32bit.jpg

The active register page can be changed by clicking the drop-down shown below
and selecting a new page. Only valid pages for that particular sensor will be
shown. Sensors that do not have register page capabilities will only show
registers on page zero.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/register_pages.png

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/change_page_read_registers.gif`

Registers can be written in either hexadecimal or decimal format by selecting
the target register, typing the new value in the ``New Value`` text box, and
clicking on ``Write.`` Write-only registers will display a ``Write Only``
message in the status box above the ``New Value`` text box. Read-only registers
will not display any message unless attempting to be written to.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/write_only.png

The ``Register Access`` tab can also measure the data ready output rate
dynamically by clicking on the ``Measure Data Ready`` checkbox. It"s possible
for this feature not to detect the data ready signal if a non-default data ready
setting is configured.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/decimate_measure_dr_1.gif`

Streaming/Logging Sensor Data to a File
---------------------------------------

The ``Data Logging`` tab provides the tools necessary for reliably streaming
sensor data to the host PC. Data is saved to disk in .csv format.

Register Logging
~~~~~~~~~~~~~~~~

The register logging form allows you to capture a custom list of registers from
the target IMU. Registers can be added in any order, irrespective of page. The
register list can also be saved to a file to easily recall an elaborate list of
registers on different systems.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/add_stream_registers.gif`

Setting the :adi:``DR Active`` check box configures the
`EVAL-ADIS-FX3 <EVAL-ADIS-FX3>` to wait for a data ready signal before
initiating a SPI transfer. Data captures may be performed without data ready
synchronization, but this configuration is not recommended since invalid data
may be read from the IMU. The images below show the differences between data
captures performed with and without ``DR Active`` enabled.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/dr_active_inactive.jpg

The IMU data rate (data ready) can be read from this form to verify that the
sensor configuration is valid before kicking off a data stream.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/logging_data_ready.gif`

Setting the ``Validate DR Period`` checkbox will notify the Eval GUI to measure
the sensor output data rate and verify that the registers" requested list does
not exceed the IMU data valid period. The SPI SCLK, SPI stall, number of
registers, and protocol overhead are all taken into account in the calculation.
The image below shows a SPI transaction that exceeds the data ready period.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/too_much_data.jpg

The three text boxes near the bottom of the window configure the data write
behavior for the stream.

::

   *# Samples To Capture sets the total number of samples to capture. For example, if the sensor data rate were set to  2,000 samples per second (SPS), and you wanted to capture 1 hour of data, the number of samples to capture would be 2,000* 3,600 = 7,200,000.
   *# Samples Per Write sets the number of samples to buffer between writes to the disk. This is particularly useful on slower machines or very long-term tests. For example, if the sensor data rate was set to 20SPS and you wanted to capture data for 30 days but only write to the disk once per hour, the samples per write setting would be 20* 3,600 = 72,000 and the samples to capture setting would be 20(SPS) *3,600(seconds per hour)* 24(hours per day) * 30(days) = 51,840,000.
   * # Lines Per File sets the number of rows to write per file. The default 1,000,000 is a good compromise between file growth and usability and was chosen to work around an issue with Microsoft Excel, where the software will struggle when opening files with more than one million rows.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/capture_config_fx3.jpg

Once the sensor is configured and ready, click ``Start Capture`` to begin the
data capture.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/logging_data.gif`

The data capture can be canceled if necessary. Any data that is pending a write
to the disk will be written.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/logging_data_cancel.gif`

GPIO Interfacing with the Pin Access Tab
----------------------------------------

The ``Pin Access`` tab allows you to interface with the FX3 Eval Board"s GPIOs,
including the four IMU GPIO pins (DIO1, DIO2, DIO3, and DIO4) that are routed
from the IMU breakout board to the FX3 Eval Board via the ribbon cable.
Depending on the specific IMU and its GPIO settings, the IMU may have each DIO
pin configured as an IMU input, output, or be unused, so the user should take
care to configure the corresponding FX3 GPIO pins appropriately to avoid GPIO
contention.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/pin_access.jpg

Example use cases:

- If the IMU is configured to output a Data Ready signal on DIO1, you can
  measure the frequency by clicking on DIO1 and then hitting ``Measure
  Frequency``.
- If the IMU is configured to accept an external sync signal on DIO2, you can
  generate a PWM signal from the FX3 GPIO pin to drive the external sync by
  clicking on DIO2 and entering the desired frequency and duty cycle in the PWM
  Setup window, then clicking ``Start PWM``

.. warning::

   Be cautious to avoid driving an IMU output pin with the FX3, as this can
   cause permanent damage!
