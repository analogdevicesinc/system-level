.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_adxrs290_pmod

.. _eval-adicup3029 reference_designs demo_adxrs290_pmod:

ADXRS290 Gyroscope PMOD Command Line Interface Demo
===================================================

The **ADuCM3029_demo_adxrs290** is a dual-axis angular rate sensor (gyroscope)
demo project that provides a solution to control the **EVAL-ADXRS290-PMDZ**
**PMOD** using a minimal **CLI** and the **no-OS** drivers for the
**EVAL-ADICUP3029** platform. It is a simple evaluation board that allows quick
evaluation of the performance of the ADXRS290.

General description
-------------------

This project is an example on how to use
:dokuwiki:`Eval-ADICUP3029 </resources/eval/user-guides/eval-adicup3029>`.

The ADuCM3029_demo_adxrs290_pmdz project uses the :adi:`EVAL-ADXRS290-PMDZ`
which has the **ADXRS290, a high performance pitch and roll (dual-axis in-plane)
angular rate sensor (gyroscope)** on board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/eval-adxrs290-pmdz_top.png
   :width: 300px

The application senses and reads the **X-axis** and **Y-axis** rate that is also
called a roll and pitch rate sensing device. It produces a positive output
voltage for clockwise rotation about the x-axis and y-axis.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/roll_and_pitch.png
   :width: 400px

The ADXRS290 provides an output full-scale range of ±100°/s with a sensitivity
of 200 LSB/°/s. Its resonating disk sensor structure enables angular rate
measurement about the axes normal to the sides of the package around an in-plane
axis. Angular rate data is formatted as 16-bit twos complement and is accessible
through a SPI digital interface. The ADXRS290 exhibits a low noise floor of
0.004°/s/√Hz and features programmable high-pass and lowpass filters.

In digital mode, the ADXRS290 communicates via 4-wire SPI and operates as a
slave. Ignore data transmitted from the ADXRS290 to the master device during
writes to the ADXRS290. Wire the ADXRS290 for SPI communication. The maximum SPI
clockspeed is 5 MHz, with 12 pF maximum loading.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/spi_comm.png
   :width: 400px

All the outputs are printed from the UART to the USER USB port and can be read
on the PC using a serial terminal program, such as Putty or Tera Term.

The application builds upon the **no-OS** device and platform drivers and a
minimal **CLI** module to provide a robust command set to set the range and
output value of the channels.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/software_architecture.png
   :width: 400px

The program first initializes the hardware system as well as the driver
handlers, then goes into the main process that just implements the **CLI**
process and waits for user commands. If a command is received, it is executed
and the program returns to the main loop.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/software_routine.png
   :width: 400px

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP3029
  - EVAL-ADXRS290-PMDZ
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - ADuCM3029_demo_adxrs290_pmdz software
  - CrossCore Embedded Studio (2.7.0 or higher)
  - ADuCM302x DFP (3.2.0 or higher)
  - ADICUP3029 BSP (1.1.0 or higher)
  - Serial Terminal Program

    - Such as Putty or Tera Term

Setting up the Hardware
-----------------------

#. Connect **EVAL-ADXRS290-PMDZ** board to the **EVAL-ADICUP3029** using
   connector **P8**.

#. Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adxrs290_pc.jpg

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP3029 with the software for the
ADXRS290.

#. Dragging and Dropping the .Hex to the Daplink drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADICUP3029_ADXRS290** demo can be found here:

.. admonition:: Download

   Prebuilt ADXRS290_CLI Hex File

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adxrs290_no_os_cli_demo.zip`

   Complete ADXRS290_CLI Source Files

   - `ADuCM3029_demo_adxrs290_pmdz at Github <https://github.com/kister-jimenez/ADuCM3029_demo_adxrs290pmdz>`__

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the
:dokuwiki:`Tools Overview page. </resources/eval/user-guides/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to import existing projects into your workspace </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_import_existing_projects_into_your_workspace>`
section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to configure the debug session </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_configure_the_debug_session_for_an_aducm3029_application>`
section.

Project Structure
~~~~~~~~~~~~~~~~~

Beside the IDE generated sources the project structure is divided into high
level software modules and low level software modules.

The high level modules are in the **src** folder and are:

- ADXRS290 device driver;
- CLI module;
- ADXRS290_PMDZ module (application source)
- ADuCM3029_demo_adxrs290_pmdz.c (main file)

The low level modules are the platform drivers and are included in the
**platform_source** and **platform_include** folders.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adxrs290_pmdz_project_struct.png

.. note::

   For more information on importing, debugging, or other tools related
   questions, please see the
   :dokuwiki:`tools user guide. </resources/eval/user-guides/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

Gyroscope range setting - *ADXRS290_RANGE* parameter - 2, 4, or 8 are
acceptable values to set the [g] range for the ADXRS290 (*ADXRS290.h*).

::

   #define ADXRS290_SENSE        2

Sensor activity and inactivity thresholds - *ACT_VALUE* and *INACT_VALUE*
paramaters used to determine at which acceleration values the sensor can react
at sleep/wake-up commands (*ADXRS290.h*):

::

   #define ACT_VALUE          50
   #define INACT_VALUE        50

Sensor activity and inactivity time - *ACT_TIMER* and *INACT_TIMER*
paramaters used to determine sleep/wake-up intervals(*ADXRS290.h*):

::

   #define ACT_TIMER          50
   #define INACT_TIMER        50

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

#. In order to view the data, you must flash the program to the EVAL-ADICUP3029.
#. Extract the zip file and drag and drop the provided hex file in the DAPLINK
   drive.
#. Once done, open a serial terminal program, such as Putty or Tera Term.
#. Then follow the UART configurations below.

Following is the UART configuration.

::

   Select COM Port
   Baud rate: 115200
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

It should now display the value similar to the image below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/screenshot_cli.png
   :width: 400px

The user must press the reset button on ADICUP3029 each time they want to
display the results.

Digital Communications
~~~~~~~~~~~~~~~~~~~~~~

The Digital communication on the EVAL-ADXRS290-PMDZ is accomplished using a
standard expanded SPI PMOD port.

.. list-table::
   :header-rows: 1

   * - Connector P1
     -
   * - Description
     - Pin(s)
   * - SS
     - 1
   * - MOSI
     - 2
   * - MISO
     - 3
   * - SCLK
     - 4
   * - GND
     - 5, 11
   * - IOVDD
     - 6, 12
   * - SYNC
     - 7

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/02_065300a_top.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/08_065300a.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/20-065300-01a.zip`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/bom.zip`

Additional Information and Useful Links
---------------------------------------

- :adi:`ADXRS290 Product Page <ADXRS290>`

Reference Demos & Software
--------------------------

- `ADXRS290 No-OS Build Instruction Guide <https://github.com/analogdevicesinc/no-OS/wiki>`__
- :git-no-OS:`ADXRS290 No-OS Drivers <projects/adxrs290-pmdz+>`


