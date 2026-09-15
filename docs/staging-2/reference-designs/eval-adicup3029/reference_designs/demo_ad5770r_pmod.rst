.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_ad5770r_pmod

.. _eval-adicup3029 reference_designs demo_ad5770r_pmod:

AD5770R PMOD Demo
=================

The **ADuCM3029_demo_ad5770rpmdz** project provides a solution to control the
**EVAL-AD5770R-PMDZ** **PMOD** using a minimal **CLI** and the **no-OS** drivers
for the **EVAL-ADICUP3029** platform.

General Description/Overview
----------------------------

The :adi:`AD5770R` is a 6-channel, 14-bit, multi-range, current output **DAC**
designed for use in communications systems, instrumentation and industrial
applications; specifically for photonics control and current mode biasing. It
has 6 programmable output channels with 1 channel capable of sinking up to 60 mA
of current. The **EVAL-AD5770R-PMDZ** is a board designed to be a compact and
low cost solution to evaluate the part.

The application builds upon the **no-OS** device and platform drivers and a
minimal **CLI** module to provide a robust command set to set the range and
output value of the channels.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5770r_layer.png

The program first initializes the hardware system as well as the driver
handlers, then goes into the main process that just implements the **CLI**
process and waits for user commands. If a command is received, it is executed
and the program returns to the main loop.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5770r_process.png

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP3029
  - EVAL-AD5770R-PMDZ
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad5770rpmdz <projects/ADuCM3029_demo_ad5770rpmdz+>`
  - CrossCore Embedded Studio (2.9.1 or higher)
  - ADuCM302x DFP (3.2.0 or higher)
  - ADICUP3029 BSP (1.1.0 or higher)
  - Serial Terminal Program

    - Such as Putty or Tera Term

Setting up the Hardware
-----------------------

#. Connect **EVAL-AD5770R-PMDZ** board to the **EVAL-ADICUP3029** using
   connector **P8**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5770r_connect.jpg

#. Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5770r_pc.jpg

Outputting Data
---------------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-serial-terminal-setup
   :end-before: .. end-serial-terminal-setup

Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the
list of commands and their short versions. Bellow is the short command list:

.. list-table::
   :header-rows: 1

   * - Function
     - Command
     - Description
     - Example
     -
   * - General commands
     -
     -
     -
     -
   * -
     - *h*
     - Display available commands.
     -
     -
   * -
     - *t*
     - Set channels at production test levels.
     -
     -
   * - DAC commands
     -
     -
     -
     -
   * -
     - *sir*
     - Set the input register of the chosen DAC channel.
       <*chan*> = channel to update; values are: c0, c1, c2, c3, c4, c5.
       <*value*> = update value in decimal; between 0 and 16383.
     - sir c0 8192
     -
   * -
     - *uo*
     - Update the DAC output with the channel input registers value.
       This is done with the nLDAC GPIO if it"s available and with the SW register otherwise.
     -
     -
   * -
     - *sc*
     - Set the value of the chosen DAC channel.
       <*chan*> = channel to update; values are: c0, c1, c2, c3, c4, c5;
       <*value*> = update value in decimal; between 0 and 16383.
     - sc c0 8192
     -
   * -
     - *sr*
     - Set the range of the DAC output channels.
       <*chan*> = channel to update; values are: c0, c1, c2, c3, c4, c5;
       <*opt*> = option chosen for the channel. values are: opt1 - only for
       channels 0 and 1, opt2, opt3.
       Those correspond to the options in
       :adi:`the datasheet <media/en/technical-documentation/data-sheets/AD5770R.pdf>`.
     - sr c0 opt1
     -

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
AD5770 PMOD.

#. Dragging and Dropping the .Hex to the Daplink drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_ad5770** can be found here:

.. admonition:: Download

   Prebuilt AD5770 PMOD Hex File

   - :git-EVAL-ADICUP3029:`AduCM3029_demo_ad5770rpmdz.Hex <Latest/ADuCM3029_demo_ad5770rpmdz.hex+>`

   Complete AD5770 PMOD Source Files

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad5770rpmdz Source Code <projects/ADuCM3029_demo_ad5770rpmdz+>`

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

- AD5770R device driver;
- CLI module;
- AD5770R_PMDZ module (application source)
- ADuCM3029_demo_ad5770rpmdz.c (main file)

The low level modules are the platform drivers and are included in the
**platform_source** and **platform_include** folders.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad5770r_pmdz_project_struct.png


