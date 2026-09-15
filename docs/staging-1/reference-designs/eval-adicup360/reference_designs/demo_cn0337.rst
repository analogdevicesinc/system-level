.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/reference_designs/demo_cn0337

.. _eval-adicup360 reference_designs demo_cn0337:

RTD Temperature Measurement Demo
================================

The **ADuCM360_demo_cn0337** is a RTD temperature measurement demo project for
the EVAL-ADICUP360 base board with additional EVAL-CN0337-PMDZ pmod, created
using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General description
-------------------

This project is a good example for how to use
:dokuwiki:`EVAL-ADICUP360 board </resources/eval/user-guides/eval-adicup360/hardware/base_board>`
in different combinations with pmod boards. It expand the list of possible
applications that can be done with the base board.

The **ADuCM360_demo_cn0337** project uses the
:adi:`EVAL-CN0337-PMDZ pmod <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0337>`
which is a completely isolated **12-bits**, **300 kSPS RTD** temperature
measuring system (with only three active devices) that processes the output of a
**Pt100 RTD** and includes an innovative circuit for lead-wire compensation
using a standard **3-wire** connection.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0337_demo_1.png
   :width: 550px

The CN0337 circuit translates the **RTD** input **resistance** range (**100 Ω**
- **212.05 Ω** for a **0°C** - **300°C** temperature) into **voltage** levels
compatible with the input range of the ADC (**0 V** - **2.5 V**). The 12-bits
ADC value is received via SPI interface of the EVAL-ADICUP360 board.

The **EVAL-CN0337-PMDZ** comes with an evaluation software which can help you to
test and to calibrate your pmod before you use it with an RTD sensor.

.. note::

   Please visit
   :dokuwiki:`CN0337 Software User Guide page </resources/eval/user-guides/circuits-from-the-lab/cn0337>`
   to find out how to get and how to use the **CN0337 evaluation software**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0337_demo_2.png
   :width: 550px

The **ADuCM360_demo_cn0337** application processes ADC output value and make all
necessary conversions in order to provide RTD measure results. A UART interface
(9600 baud rate and 8-bits data length) is used to send the results to terminal
window: RTD **temperature** and **resistance** values, **voltage** calculation
and **ADC code**. If the resistance and temperature values are out of range you
get an error message which means that you need to check your settings.

The output values are displayed when you press ENTER key (CR) from the keyboard.
Also you can decide how often the measurements take place (see *SCAN_TIME*
parameter).

The project offers two method to calculate the RTD resistance, giving you the
possibility to get more accurate RTD measurement results (see
:adi:`CN0337 circuit note <cn0337>`).

You can use :green:`\ **transfer function**\ ` of the circuit which calculate
RTD resistance based on voltage changed value and circuit gain:

::

   Rrtd = (Vout - Voffset)/Gain

Or you can use the :green:`\ **two-point calibration**\ ` method which used the
ADC output values for 2 different measurements: first using Rmin = 100 Ω (ADC1)
precision resistor and second with Rmax = 212.05 Ω (ADC2) resistor.

::

   Rrtd = Rmin + [(Rmax - Rmin)/(ADC2 - ADC1)]*(ADCrtd - ADC1)

Because the transfer function of the RTD (resistance vs. temperature) is
nonlinear is needed a software linearization to eliminate the nonlinearity error
of the RTD Pt100 sensor. This project used so called **Piecewise Linear
Approximation** method.

Piecewise Linear Approximation Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method characterized by taking linear approximation one step further, one
can conceptualize any number of linear segments strung together to better
approximate the nonlinear RTD transfer function. Generating this series of
linear segments so that each segment"s endpoints meet those of neighboring
segments results in what can be viewed as a number of points connected by
straight lines.

These coefficients is calculated once to best match the RTD"s nonlinear transfer
function and then stored permanently in a look-up table (see *C_rtd[]* table).
From this table of coefficients, the software can perform simple linear
interpolation to determine temperature based on measured RTD resistance.

The look-up table can have how many coefficients you needed depending how
accurate you want to be. For this project the RTD resistance range is separated
into 100 linearization segments.

.. note::

   This method is also used in the
   :adi:`AN-709 application note <media/en/technical-documentation/application-notes/AN709_0.pdf>`
   which provide also an
   :adi:`RTD coefficient generator tool <media/en/technical-documentation/application-notes/AN-709_files.zip>`
   that you also can use.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP360
  - EVAL-CN0337-PMDZ
  - 3-Wire PT100 RTD
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - ADuCM360_demo_cn0337 software
  - CrossCore Embedded Studio (2.7.0 or higher)
  - ADuCM36x DFP (1.0.2 or higher)
  - CMSIS ARM Pack (4.3.0 or higher)
  - Serial Terminal Program

    - Such as Putty or Tera Term

Setting up the hardware
-----------------------

#. To program the base board, set the jumpers/switches as shown in the next
   figure. The important jumpers/switches are highlighted in red.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0337_demo_3.png
      :width: 500px

#. Plug the EVAL-CN0337-PMDZ PMOD in the EVAL-ADICUP360 base board, via the
   PMOD_SPI port (P4).
#. Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0337.

#. Dragging and Dropping the .Bin to the MBED drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0337** demo can be found here:

.. admonition:: Download

   Prebuilt CN0337 Bin File

   - :git-EVAL-ADICUP360:`ADuCM360_demo_cn0337.Bin <Release-1.0/ADuCM360_demo_cn0337.bin+>`

   Complete CN0337 Source Files

   - :git-EVAL-ADICUP360:`ADuCM360_demo_cn0337 Source Code <projects/ADuCM360_demo_cn0337+>`

.. note::

   For more information on importing, debugging, or other tools related
   questions, please see the
   :dokuwiki:`tools user guide. </resources/eval/user-guides/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

Converter operation mode - :green:`AD7091R_OPERATION_MODE` - POWER_DOWN to
select power-down AD7091R mode of operation or NORMAL for normal mode
(*AD7091R.h*).

::

   #define AD7091R_OPERATION_MODE      POWER_DOWN

Converter scan time - :green:`SCAN_TIME` - how often (msec) to read conversion
results (*AD7091R.h*).

::

   #define SCAN_TIME          500

Converter reference voltage - :green:`VREF` - reference voltage (V) for
AD7091R converter (*AD7091R.h*).

::

   #define VREF              2.5

RTD resistance calculation method - :green:`RTD_FORMULA` - this parameter can
be set as TRANSFER_FUNCTION or TWO_POINT_CALIBRATION (*CN0337.h*).

::

   #define RTD_FORMULA     TRANSFER_FUNCTION

RTD parameters - all needed parameters for RTD calculations (*CN0337.h*).

::

   #define  TMIN         (0)            /*Tmin [˚C]*/
   #define  TMAX         (300)          /*Tmax [˚C]*/
   #define  RMIN         (100)          /*Resistance [Ohms] at Tmin*/
   #define  RMAX         (212.052)      /*Resistance [Ohms] at Tmax*/
   #define  NSEG         100            /*Nr. of sections in look-up table*/
   #define  RSEG         1.12052        /*Resistance of each segment*/
   #define  ADC_MIN      152            /*ADC min for RMIN*/
   #define  ADC_MAX      4095           /*ADC max for RMAX*/

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

#. In order to view the data, you must flash the program to the EVAL-ADICUP360.
#. Once complete you will need to switch the USB cable from the DEBUG USB (P14)
   to the USER USB (P13).
#. Then follow the UART settings below with the serial terminal program.

Following is the UART configuration.

::

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

- The user must press the <ENTER> key every time they want new data.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0337_demo_2.png
   :width: 550px

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the
:dokuwiki:`Tools Overview page. </resources/eval/user-guides/eval-adicup360/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to import existing projects into your workspace </resources/eval/user-guides/eval-adicup360/tools/cces_user_guide#how_to_import_existing_projects_into_your_workspace>`
section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to configure the debug session </resources/eval/user-guides/eval-adicup360/tools/cces_user_guide#how_to_configure_the_debug_session_for_an_aducm360_application>`
section.

Project structure
-----------------

The **ADuCM360_demo_cn0337** project use ADuCM36x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for SPI0, UART
via P0.1/P0.2; SPI, UART read/write functions; AD7091R control and RTD
conversions.

In the **src** and **include** folders you will find the source and header files
related to CN0337 software application. The *Communication.c/h* files contain
SPI and UART specific data, meanwhile the *AD7091R.c/h* files contain the ADC
control data and the *CN0337.c/h* files contain the RTD measurements management.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0337_demo_5.png
   :width: 340px

The **RTE** folder contains device and system related files:

- Device Folder – contains low levels drivers for ADuCM360 microcontroller.(try
  not to edit these files)
- system.rteconfig - Allows the user to select the peripherial components they
  need, along with the startup and ARM cmsis files needed for the project.


