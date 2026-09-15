.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad3029lz/example_project/joystick_example

.. _ev-cog-ad3029lz example_project joystick_example:

JOYSTICK INTERFACE WITH EV-COG-AD3029LZ
=======================================

Introduction
------------

This document explains about the hardware and software setup, which is required
to interface a joystick with the EV-COG-AD3029LZ using MCP23S17 as an
interfacing I/O expander chip. The entire setup is made simple with the use of
AD-GEAR-DISPLAY1Z, which contains the joystick and the expander IC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_joystick.png
   :width: 600px

The hardware details cover the COG jumper settings and also the pin mapping
between the joystick, MCP23S17 expander and the EV-COG-AD3029LZ. The software
details cover the software development kit required and the software
architecture of the code base written to interface the joystick with the
EV-COG-AD3029LZ.

Boards and Accessories required
-------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear.png
   :width: 700px

a.) EV-COG-AD3029LZ (left) b.) AD-GEAR-DISPLAY1Z (right)

Hardware interface
------------------

This section contains hardware related information about AD-GEAR-DISPLAY1Z and
the EV-COG-AD3029-LZ. Links are provided to the WiKi page of the target
COG-AD3029-LZ, the Schematics, BOMs and technical documentations at the end of
this page.

Connection Diagram
~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_joystick_pin.png
   :width: 600px

\* The joystick and the I/O expander-MCP23s17 are embedded on the
AD-GEAR-DISPLAY1Z.

Board Interface
~~~~~~~~~~~~~~~

#. Connect the AD-GEAR-DISPLAY1Z via it"s Cog connectors to the
   EV-COG-AD3029LZ"s expansion connectors.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_gear_connection.png
      :width: 600px

Pin Connection
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - EV-COG-AD3029LZ pins
     - MCP23S17 pins
     - Joystick
   * - GPIO22 / SPI1_CLK
     - SCL_SCK
     - -
   * - GPIO23 / SPI1_MOSI
     - SI
     - -
   * - GPIO24 / SPI1_MISO
     - SO
     - -
   * - GPIO34 / SPI1_CS2
     - CS_N
     - -
   * - GPIO15 / INT_WAKE0
     - INTA
     - -
   * - -
     - GPA0
     - SW1
   * - -
     - GPA1
     - SW2
   * - -
     - GPA2
     - SW3
   * - -
     - GPA3
     - SW4
   * - -
     - GPA4
     - SW5

\* A0, A1 and A2 of the I/O expander are connected to the ground.

\* RESET_N of the I/O expander is connected to EXT_VDD_OUT of the COG board.

Software Details
----------------

This section contains software related information about AD-GEAR-DISPLAY1Z and
the EV-COG-AD3029-LZ and the application. Links are provided to the user guides,
BSPs, software tool chains and the example project at the end of this page.

Application files
~~~~~~~~~~~~~~~~~

The example project provided consists mainly of the following,

#. mcp23s17_3.c
#. mcp23s17.h
#. SPI_PE.h
#. adi_spi_pe.h
#. IAR project files( \*.eww,\*.ewt, \*.ewt)

- The application uses the ADuCM302x-Rel 2.0.0 driver BSP for IAR.
- IAR Embedded Workbench 7.60.1 or higher is advised to be used.

Application flow
~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/joystick_flow.png
   :width: 800px

\* All the APIs for using the I/O expander is within the mcp23s17_3.c with
supporting definitions found in SPI_PE.h and adi_spi_pe.h. A separate driver
file to use the I/O expander is yet to be created.

IDE Setup and example application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section covers the various steps involved in getting the joystick_example
application code to run on EV-COG-AD3029LZ after the hardware setup is done.

Following are the steps involved,

#. Download and install IAR Embedded Workbench 7.60.1 or higher.

#. Download the joystick_example project from
   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/joystick_example.zip`

#. The joystick_example project is also available on
   :dokuwiki:`Bitbucket </resources/eval/user-guides/ev-cog-ad3029lz/example_project/Link to bitbucket has to be put here>`.
#. Import the source into IAR workspace and run the application software to
   generate interrupts by joystick press.

References and Links
--------------------

- :adi:`ADuCM3029 Hardware Reference Manual <media/en/dsp-documentation/processor-manuals/ADuCM302x-mixed-signal-control-processor-hardware-reference.pdf>`
- :dokuwiki:`EV-COG-AD3029LZ User guide with the BSP </resources/eval/user-guides/ev-cog-ad3029lz>`
- `MCP23s17 Datasheet <http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf>`__
- Schematics of EV-COG-AD3029LZ and AD-GEAR-DISPLAY1Z are found in the Docs
  folder of the joystick_example project.
