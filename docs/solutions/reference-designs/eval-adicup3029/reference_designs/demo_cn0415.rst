Solenoid Closed Loop Control Demo
=================================

The **ADuCM3029_demo_cn0415** provides a solution for controlling and monitoring solenoid actuator current, using an **EVAL-CN0415-ARDZ** shield installed on an **EVAL-ADICUP3029** base board. The user interface is implemented as a command line interface (CLI) through a serial UART connection. The project is created using **CrossCore Embedded Studio** and **GNU ARM compiler**.

General Description/Overview
----------------------------

The circuit can be divided into four parts for the purpose of analyzing
interaction with the software project: The supply block, the sense block, the
actuator block, and the overcurrent fault / reset block.

The supply block consists of DC-DC converters and protection circuits. This
block does not interact with the software.

Overcurrent fault and Overcurrent Reset block, controlled by general-purpose input/output (GPIO) pins on **ADICUP3029**. If the solenoid current exceeds a resistor-programmed threshold, a comparator trips off the MOSFET gate driver and notifies software via a GPIO signal. The user can then re-enable the driver once the fault condition is removed.

The sense block, consisting of a 0.1Ω current sense resistor, sense amplifier,
filtering, and 14-bit Analog to Digital converter (ADC). The ADC is connected to
the ADICUP3029 via Serial Peripheral Interface (SPI)

The voltage fed to the ADC with respect to current passing through the solenoid
is given by the equation:

::

          VADC = Isolenoid * Rsense * 20       Isolenoid - Current through solenoid
                                               Rsense    - Sense resistor (0.1Ω)

The code output by the ADC is then calculated:

::

                                               VADC - Voltage on the ADC input
                                               CODE = (VADC * 2^14) / Vref          CODE - Code output by the ADC
                                               Vref - Reference voltage of the ADC

Here **Vref** is the reference voltage of the ADC and depends on the chosen supply. **If** the **12V on P1** was selected the supply voltage of the ADC will be 5V and the corresponding reference is **4.096V**. **If** the ADC is powered from Arduino with **3.3V** the reference will be **2.048V**.

So the ADC code with respect to current sense will be:

::

          CODE = (Isolenoid * Rsense * 20 * 2^14) / Vref

The actuator block, consisting of a logic-level to MOSFET driver. The logic signal is driven by the **ADICUP3029**\ ’s PWM peripheral, allowing the the effective voltage across the solenoid to be varied.

The software implements several functions with the sense and actuator blocks.
PWM frequency and duty cycle can be controlled directly. This mode of operation
would normally be combined with an outer feedback loop in a control system. One
example would be a system in which the solenoid controls air pressure, that is
in turn measured by a pressure sensor, which is then used to determine a new
duty cycle value that brings the pressure closer to the desired setpoint.

A PID control loop allows the solenoid current to be accurately controlled,
compensating for variations in supply voltage and coil resistance. This mode of
operation allows for optimum drive current for 2-state solenoids, minimizing
power dissipation. An additional function allows a higher initial “pull in”
current to be applied for a short time, after which current drops back to a
lower “hold” current.

.. image:: ../images/pid_controller_equation.png
   :alt: PID equation
   :align: center

Using the data gathered form the sense block the a **PID controller** is implemented that can be used to set a specific current value or duty cycle. To use the **PID controller** it must be first tuned with the right values of **Kp**, **Ki** and **Kd**. Various methods can be used for tunning. The proposed method, which is easy, but does not yield perfect results, is:

-  Start increasing **Kp** constant while keeping **Ki** and **Kd** at 0. Increase **Kp** until the actuation time is reasonable and the current overshoot is within 5% of the wanted value.
-  Start increasing **Ki** constant until the actuation time is reasonable and the current overshoot is within 5% of the wanted value.
-  Pick **Kd** as 25% (1/4) of **Ki**.

A dither function allows a low-frequency AC signal to be superimposed,
minimizing mechanical “stiction” in proportional solenoid applications.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0415-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  Solenoid actuator
   -  12V and 1A limited power supply

-  Software

   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  Serial Terminal Program (Required for running in release mode only)

      -  Such as Putty or Tera Term

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0415 demo application <projects/ADuCM3029_demo_cn0415>`

Setting up the Hardware
-----------------------

-  Connect **EVAL-CN0415-ARDZ** board to the **EVAL-ADICUP3029**.

.. image:: ../images/cn0415_adicup3029_dock.jpeg
   :alt: CN0415 docked on ADICUP3029
   :align: center

-  Connect a micro-USB cable to **P10** connector of the **EVAL-ADICUP3029** and connect it to a computer.
-  Connect a solenoid actuator to the **P8** connector with the positive wire on pin 1 and negative wire on pin 2.
-  Connect a 12V power supply to the **P1** connector with the positive wire on pin 1 and negative wire on pin 2.

.. image:: ../images/cn0415_fully_connected.jpeg
   :alt: CN0415 power up
   :align: center

-  Turn on power supply.

Configuring the Software
------------------------

The configuration parameters can be found in the **config.h** file.

**vref** - Reference voltage of the **ADC** set by supply method as described above. Set to **4.096** if the supply is the 12V on **P1** or to **2.048** if supply is the **Arduino** 3.3V.

============== ==========
Supply voltage vref value
============== ==========
3.3V           2.048
12V            4.096
============== ==========

::

      /* Reference voltage of the ADC */
      float vref = 4.096;

Outputting Data
---------------

Serial Terminal Setup
~~~~~~~~~~~~~~~~~~~~~

A serial terminal is an application that runs on a PC or laptop that is used to
display data and interact with a connected device (including many of the
Circuits from the Lab reference designs). The device's UART peripheral is most
often connected to a UART to USB interface IC, which appears as a traditional
COM port on the host PC/ laptop. (Traditionally, the device's UART port would
have been connected to an RS-232 line driver / receiver and connected to the PC
via a 9-pin or 25-pin serial port.) There are many open-source applications,
and while there are many choices, typically we use one of the following:

- `Tera Term <https://ttssh2.osdn.jp/index.html.en>`_
- `PuTTY <https://www.putty.org/>`_
- `RealTerm <https://realterm.sourceforge.io/>`_

Before continuing, please make sure you download and install one of the above
programs.

There are several parameters on all serial terminal programs that must be setup
properly in order for the PC and the connected device to communicate. Below are
the common settings that must match on both the PC side and the connected UART
device.

- **COM Port** - This is the physical connection made to your PC or Laptop,
  typically made through a USB cable but can be any serial communications cable.
  You can determine the COM port assigned to your device by visiting the device
  manager on your computer. Another method for identifying which COM port is
  associated with a USB-based device is to look at which COM ports are present
  before plugging in your device, then plug in your device, and look for a new
  COM port.
- **Baud Rate** - This is the speed at which data is being transferred from the
  connected device to your PC. These parameters must be the same on both devices
  or data will be corrupted. The default setting for most of the reference
  designs is 115200.
- **Data Bits** - The number of data bits per transfer. Typically UART transmits
  ASCII codes back to the serial port so by default this is almost always set to
  8-Bits.
- **Stop Bits** - The number of "stop" conditions per transmission. This is
  usually set to 1, but can be set to 2 for redundancy.
- **Parity** - Is a way to check for errors during the UART transmission.
  Unless otherwise specified, set parity to "none".
- **Flow Control** - Is a way to ensure that data between fast and slow devices
  on the same UART bus is not lost during transmission. This is typically not
  implemented in a simple system, and unless otherwise specified, set to "none".

In many instances there are other options that each of the different serial
terminal applications provide, such as **local line echo** or **local line
editing**, and features like this can be turned on or off depending on your
preferences.

**Example setup using PuTTY**

#. Plug in your connected device using a USB cable or other serial cable.
#. Wait for the device driver of the connected device to install on your PC or
   Laptop.
#. Open your device manager, and find out which COM port was assigned to your
   device.
#. Open up your serial terminal program (PuTTY for this example).
#. Click on the serial configuration tab or window, and input the settings to
   match the requirements of your connected device. The default baud rate for
   most of the reference designs is 115200. Make sure that you use the correct
   baud rate for your application.
#. Ensure you click on the checkboxes for **Implicit CR in every LF** and
   **Implicit LF in every CF**.
#. Ensure that local echo and line editing are enabled, so that you can see what
   you type and are able to correct mistakes. (Some devices may echo typed
   characters - if so, you will see each typed character twice. If this happens,
   turn off local echo.)

.. tip::

   If you see nothing in the serial terminal, try hitting the reset button on
   the embedded development board.

Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the list of commands and their short versions. Below is the short command list:

+--------------+------------------------------+-----------------------------------------------------------------------+
| Type         | Command                      | Description                                                           |
+==============+==============================+=======================================================================+
| System       | *h*                          | Display available commands                                            |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *rst*                        | Reset controller, parameters and faults                               |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *stts*                       | Show application status and parameters                                |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *clb*                        | Run calibration sequence                                              |
+--------------+------------------------------+-----------------------------------------------------------------------+
| Control      | *f*                          | Set frequency to the specified value                                  |
|              | ex: **f 5000<enter>**        | <*freq*> = value of the new frequency                                 |
|              | (set frequency to 5kHz)      | 1Hz to 4MHz frequency is possible.                                    |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *d*                          | Set duty cycle to the specified value                                 |
|              | ex: **d 5234<enter>**        | <*duty*> = value of the new duty cycle                                |
|              | (set duty cycle to 52.34%.)  | The duty cycle is from 0 representing 0% and 10000 representing 100%. |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *r*                          | Read and display the value of the ADC                                 |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *ad*                         | Activate PWM dither functionality                                     |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *rd*                         | Deactivate PWM dither functionality                                   |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *df*                         | Set dither frequency to the given value                               |
|              | ex: **df 50<enter>**         | <*freq*> = value of the new frequency                                 |
|              | (set dither freq. to 50Hz)   | Recommended maximum value of the PWM frequency divided by 10.         |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *da*                         | Set dither amplitude                                                  |
|              | ex: **da 200<enter>**        | <*duty*> = value of the amplitude in duty cycle variation             |
|              | (set dither amplitude to 2%) | Any value between 0 and 10000, same as duty cycle.                    |
|              |                              | Recommended to be lower than the lowest value needed                  |
|              |                              | for the duty cycle to be 0 or full scale.                             |
+--------------+------------------------------+-----------------------------------------------------------------------+
| PID          | *ap*                         | Activate PID controller                                               |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *rp*                         | Deactivate PID controller                                             |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *kp*                         | Set PID Kp constant                                                   |
|              | ex: **kp 5000.0<enter>**     | <*kp*> = value of the new Kp constant                                 |
|              | (set kp to 5000)             | From zero to maximum number represented by a 32 bit float value.      |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *ki*                         | Set PID Ki constant                                                   |
|              | ex: **ki 1.5<enter>**        | <*ki*> = value of the new Ki constant                                 |
|              | (set ki to 1.5)              | From zero to maximum number represented by a 32 bit float value.      |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *kd*                         | Set PID Kd constant                                                   |
|              | ex: **kd 0.25<enter>**       | <*kd*> = value of the new Kd constant                                 |
|              | (set kd to 0.25)             | From zero to maximum number represented by a 32 bit float value.      |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *spf*                        | Set PID sampling frequency                                            |
|              | ex: **spf 100<enter>**       | <*freq*> = value of the new frequency                                 |
|              | (set sample freq. to 100Hz)  | Recommended to be at most equal with the dither frequency.            |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *sps*                        | Set PID set point(hold value)                                         |
|              | ex: **sps 2500<enter>**      | <*sp*> = new hold value in A or 0.01%(duty cycle)                     |
|              | (setpoint to 25%)            | From 0 to 1 amperes or from 1 to 10000 as duty cycle.                 |
+--------------+------------------------------+-----------------------------------------------------------------------+
| Digital      | *dson*                       | Set digital solenoid high                                             |
+--------------+------------------------------+-----------------------------------------------------------------------+
|              | *dsof*                       | Set digital solenoid low                                              |
+--------------+------------------------------+-----------------------------------------------------------------------+
| Proportional | *pss*                        | Set and activate proportional solenoid                                |
|              | ex: **pss 2500<enter>**      | <*val*> = value of the current or duty cycle                          |
|              | (setpoint to 25%)            | from 0 to 1 amperes.                                                  |
+--------------+------------------------------+-----------------------------------------------------------------------+

.. image:: ../images/wiki_pic.png
   :alt: Terminal example
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0415.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0415** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0415 Hex File

   -  `AduCM3029_demo_cn0415.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0415.hex>`_

   Complete CN0415 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0415 Source Code <projects/ADuCM3029_demo_cn0415>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

The program is composed of three main parts:

-  Board setup, with initialization;
-  Calibration;
-  Main process.

.. image:: ../images/cn0415_sw_main_flowchart.png
   :alt: Software main flow chart
   :align: center

The boards initial parameters can be given in the software in the main function or the **FLASH_INIT_PARAMETERS** define in the **config.h** file can be uncommented and the relevant parameters can be changed in program from the command line and the program will retain these parameters in the non-volatile memory. The program initializes timers and UART, SPI, GPIO and FLASH controllers.

.. image:: ../images/cn0415_sw_board_setup_flow.png
   :alt: Software board setup flow chart
   :align: center

**Calibration** is done to minimize full scale error. It sets control signal to **logic "1"** and measures the current, then prompts the user for a manual measurement with a precision tool. The difference between these two measurements is stored and used in calculating future values from ADC codes.

.. image:: ../images/cn0415_sw_calibration_flow.png
   :alt: Software calibration flow chart
   :align: center

The **main process** is the infinite loop in which the program implements **CLI**, **PID** and **dither** functionality. The **UART** is used for the **CLI** and three different timers implement the **PWM** signal, the **PID** periodic calculation and the **dither** functionality.

.. image:: ../images/cn0415_sw_process_flow.png
   :alt: Software process flow chart
   :align: center

*End of Document*
