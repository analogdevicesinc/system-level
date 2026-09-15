.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0326

.. _eval-adicup3029 reference_designs demo_cn0326:

pH Monitor with Temperature Compensation Demo
=============================================

The **ADuCM3029_demo_cn0326** is a pH monitor with automatic temperature
compensation demo project, for the **EVAL-ADICUP3029** base board with
additional EVAL-CN0326-PMDZ PMod, created using the CrossCore Embedded Studio
with GNU ARM compiler.

General Description/Overview
----------------------------

This project is a good example for how to use **EVAL-ADICUP3029** in different
combinations with pmod boards. It expand the list of possible applications that
can be done with the base board.

The **ADuCM3029_demo_cn0326** project uses the
:adi:`EVAL-CN0326-PMDZ pmod <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0326>`
which is a pH sensor signal conditioner and digitizer with automatic temperature
compensation.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adicup3029_front_cn0326_attached.jpg
   :width: 600px

The CN0326 circuit provides a complete solution for pH sensors with internal
resistance between **1 MΩ** and several **GΩ**. It consist of **pH probe**
buffer, **Pt1000 RTD** for temperature compensation and **24-bits ADC** with 3
differential analog inputs.

The pH probe consists of a glass measuring electrode and a reference electrode,
which is analogous to a battery. When the probe is place in a solution, the
measuring electrode generates a voltage depending on the hydrogen activity of
the solution, which is compared to the potential of the reference electrode. As
the solution becomes more **acidic** (pH < 7) the potential of the glass
electrode becomes more positive (**+mV**) in comparison to the reference
electrode; and as the solution becomes more **alkaline** (pH > 7) the potential
of the glass electrode becomes more negative (**−mV**) in comparison to the
reference electrode.

The change in temperature of the solution changes the activity of its hydrogen
ions. When the solution is heated, the hydrogen ions move faster which result in
an increase in potential difference across the two electrodes. In addition, when
the solution is cooled, the hydrogen activity decreases causing a decrease in
the potential difference. Electrodes are designed ideally to produce a zero volt
(**0 V**) potential when placed in a buffer solution with a pH of 7 (**neutral**
pH).

The **EVAL-CN0326-PMDZ** comes with an evaluation software which can help you to
test and to calibrate your pmod before you use it.

The potential changes are outputted as ADC 24-bits value which is received via
SPI interface of the EVAL-ADICUP3039 board. The ADC analog differential channels
are:

- AIN1(+)/AIN1(-) - pH probe (voltage full range: ±414 mV at 25°C to ±490 mV at
  80°C)
- AIN2(+)/AIN2(-) - Pt1000 RTD (voltage full range: 210 mV to 290 mV with 210 μA
  excitation current)
- AIN3(+)/AIN3(-) - Bias current (used to minimized tne voltage errors)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0326_demo_2.png
   :width: 549px

The **ADuCM3029_demo_cn0326** application purchase ADC outputs from input
channels, calculates voltage, temperature and pH values. You can choose to use
internal excitation current of the ADC (IOUT2) or calculate bias current of the
circuit (see *USE_IOUT2* parameter).

A UART interface (9600 baud rate and 8-bits data length) is used, as a command
line interpreter, to send the results to terminal window: **temperature** and
**ph** values. Beside this two the interpreter process other three commands:
**help**, **calibrate** channel/channels and ADC **reset**.

To start the command line interpreter you need to press ENTER key (CR) from the
keyboard and after that just type in <help> to see available commands. The
output data are send via UART using semihosting.

.. note::

   The **calibrate** command perform an **internal zero and full scale
   calibration** of the selected channel/channels
   (:adi:`AD7793 Datasheet <media/en/technical-documentation/data-sheets/AD7792_7793.pdf>`).

The project uses below formula to determine output **ADC code** for an input
voltage on either channel:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0326_demo_2_1.png
   :width: 250px

**AIN** - analog input voltage

**GAIN** - gain value in the in-amp setting

**N** - ADC resolution (24)

The **temperature** value is calculated using RTD resistance value and it varies
from 0°C (1000 Ω) to 100°C (1385 Ω):

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0326_demo_2_2.png
   :width: 240px

**Rrtd** - RTD resistance at T°C

**Rmin** - RTD resistance at 0°C

**α** - temperature coefficient (0.00385 Ω/Ω/°C)

To calculate **pH** value is used Nernst equation:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0326_demo_2_3.png
   :width: 361px

**E** - voltage of the hydrogen electrode with unknown activity

**α** - zero point tolerance (±30 mV)

**T** - ambient temperature in °C

**n** - valence, number of charges on ion (1 at 25 °C)

**F** - Faraday constant (96485 coulombs/mol)

**R** - Avogadro"s number (8314 mV-coulombs /°K mol)

**pHiso** - reference hydrogen ion concentration (7)

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP3029
  - EVAL-CN0326-PMDZ
  - pH Probe
  - PT100 Temperature Probe
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - ADuCM3029_demo_cn0326 software
  - CrossCore Embedded Studio (2.6.0 or higher)
  - ADuCM302x DFP (2.0.0 or higher)
  - ADICUP3029 BSP (1.0.0 or higher)
  - Serial Terminal Program (Required for running in release mode only)

    - Such as Putty or Tera Term

Setting up the Hardware
-----------------------

#. Make sure the switches are in the position indicated in the picture(**S2** in
   position **1(USB)**)

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/hardware/adicup3029_front_refrence_s2_position_for_usb.jpg
      :width: 800px

#. Connect the EVAL-CN0326-PMDZ to the SPI PMOD connector **P8** of the
   **EVAL-ADICUP3029** board.
#. Plug in the USB cable from the PC to the **EVAL-ADICUP3029** base board via
   the USB connector.(**P10**)

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0326.

#. Dragging and Dropping the .Hex to the Daplink drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0326** can be found here:

.. admonition:: Download

   Pre-built CN0326 Hex File

   - :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0326.Hex <Latest/ADuCM3029_demo_cn0326.hex+>`

   Complete CN0326 Source Files

   - :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0326 Source Code <projects/ADuCM3029_demo_cn0326+>`

.. note::

   For more information on importing, debugging, or other tools related
   questions, please see the
   :dokuwiki:`tools user guide. </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide>`

Configuring the Software
------------------------

- ADC gain - :green:`AD7793_GAIN` - set gain value for AD7793 converter
  (*AD7793.h*).

::

   #define AD7793_GAIN              AD7793_GAIN_1

- Excitation current - :green:`USE_IOUT2` - select if you want to use bias
  current from the AIN3 channel: YES or you want to use internal excitation
  current, 210 µA: NO(*CN0326.h*).

::

   #define  USE_IOUT2         NO

- Zero point tolerance - :green:`TOLERANCE` - tolerance used in Nernst equation
  (*CN0326.h*).

::

   #define  TOLERANCE            0

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

#. In order to view the data, you must flash the program to the EVAL-ADICUP360.
#. Then follow the UART settings below with the serial terminal program.

Following is the UART configuration.

::

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

- The user must press the <ENTER> key to start the program.
- To get to the command menu the user must type <help> into the serial program.
- Semihosting must be enabled to see data at the console window.

Available commands
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - *help*
     - Display available commands
   * - *calibrate*
     - Calibrate selected channels or all channels
       <*ch*> = AIN1, AIN2, AIN3, or all
   * - *ph*
     - Display pH value
   * - *temperature*
     - Display temperature value
   * - *reset*
     - Reset ADC converter

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0326_demo_2.png
   :width: 549px

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


